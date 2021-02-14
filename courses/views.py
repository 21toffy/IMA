from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CourseForm, UserCourseForm
from .models import Course, UserCourse
from users.models import User
from django.urls import reverse
from core.models import ViewCount


def course_list(request):
    homeview = ViewCount.objects.create(page='Courses')
    homeview.save()
    courses = Course.objects.all()
    context = {'courses':courses}
    # template = 'courses/course_list.html'
    template = 'courses/package.html'
    return render(request, template, context)
    

def course_detail (request, id):
    course = get_object_or_404(Course,  id=id)
    course_image = course.course_image.all()
    what_you_will_learn = course.what_you_will_learn.all()
    about_course = course.about_course.all()

    # if request.user.is_authenticated():
    request.session['course'] = course.id
    context = {'course':course, 'course_image':course_image, 'about_course':about_course , 'what_you_will_learn':what_you_will_learn}
    template = 'courses/course_detail.html'
    return render(request, template, context)

from django.shortcuts import redirect

# @login_required
def course_register(request, id):
    
    if request.user.is_authenticated:



        # try:
        #     course_id = Course.objects.get(id=form_id)
        #     print(course_id)
        #     print(course_id.pk)
        # except (KeyError, Course.DoesNotExist):
        #     course_id = None
        #     print('course id is none')



        try:
            course_id = Course.objects.get(id=request.session['course'])

        except (KeyError, Course.DoesNotExist):
            course_id = None
        
        user = User.objects.get(id = request.user.id)

        user=request.user
        if_user_has_paid_for_current_course = UserCourse.objects.filter(user=user, course=course_id)
        print(if_user_has_paid_for_current_course)
        # print('-------------------------------------------------------------------------')
        # print('-------------------------------------------------------------------------')
        # print('-------------------------------------------------------------------------') 
        if request.method == 'POST':
            user_form = UserCourseForm(request.POST, instance=user)
            c_form = CourseForm(request.POST, instance=course_id)
            
            if user_form.is_valid() and c_form.is_valid():
                u_form = user_form.save(commit=False)
                u_form.user = request.user
                u_form.course = course_id

                u_form.save()
                # u_form.save()
                c_form.save()

                return render(request, 'courses/payment.html', {'user':user, 'course_id':course_id, 'if_user_has_paid_for_current_course':if_user_has_paid_for_current_course})
            else:
                return HttpResponse('Sorry refresh page and try again!!')
        else:
            u_form = UserCourseForm(instance=user)
            c_form = CourseForm(instance=course_id)
            
        context = {
            'course_id':course_id,
            'user':user,
            'u_form':u_form,
            'c_form':c_form, 'if_user_has_paid_for_current_course':if_user_has_paid_for_current_course
        }
        return render(request, 'courses/payment.html', context)

        # return render(request, 'courses/register_course.html', context)
    else:
        messages.error(request, 'You Need to be logged in or sign up to register', "alert alert-error alert-dismissible")

        return redirect(reverse('users:login'))


from .models import UserCourse
from django.http import JsonResponse
from django.http import HttpResponseRedirect

def usercourse(request):
    if request.method=='POST':
        user = request.POST.get('user')
        coursee = request.POST.get('usercourse')
        course = Course.objects.get(name = coursee)
        paid=True
        if UserCourse.objects.filter(user=request.user, course=course):
            print('already there')
            messages.error(request, 'you have already registered for this course ', extra_tags='alert alert-error alert-dismissible fade show')
            return HttpResponseRedirect(reverse('courses:usercourse'))
        else:
            usercourse=UserCourse(user=request.user, course=course, paid=paid)
            usercourse.save()

        # return x



