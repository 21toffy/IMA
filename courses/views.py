from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CourseForm, UserCourseForm
from .models import Course, UserCourse


def course_list(request):
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


@login_required
def course_register(request, id):
    try:
        course_id = Course.objects.get(id=request.session['course'])
    except (KeyError, Course.DoesNotExist):
        course_id = None
    # print(course_id)
    # print(course_id)
    print('-------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------')
    
    if request.method == 'POST':
        user_form = UserCourseForm(request.POST)
        c_form = CourseForm(request.POST, instance=course_id)
        print(user_form)
        print(c_form)
        
        if user_form.is_valid() and c_form.is_valid():
            print('valid data')
            u_form = user_form.save(commit=False)
            u_form.user = request.user
            u_form.course = course_id

            print(u_form.user)
            u_form.save()
            u_form.save()
            c_form.save()

            return render(request, 'courses/payment.html', {'email':request.user.email, 'price':course_id.price})
        else:
            return HttpResponse('Sorry refresh page and try again!!')
    else:
        u_form = UserCourseForm(instance=request.user)
        c_form = CourseForm(instance=course_id)
        print('not shit')
        print(u_form)
        print(c_form)
    context = {
        'u_form':u_form,
        'c_form':c_form
    }
    return render(request, 'courses/register_course.html', context)

    




