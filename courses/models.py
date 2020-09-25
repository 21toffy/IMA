from django.db import models
from django.conf import settings



class Course (models.Model):
    LEVEL = (
    ("Early Professionals","Early Professionals"),
    ("Professionals","Professionals"),
    ("Starters","Starters"),
    ("Experienced Professionals","Experienced Professionals"),
    ("Enthusiast","Enthusiasts"),
    ("Everyone","Everyone"),
    )
    name = models.CharField(max_length=100)
    details = models.TextField()
    price = models.IntegerField(default=15)
    level = models.CharField(choices=LEVEL, default="Starters", max_length=200)
    duration = models.CharField(max_length=200)
    perks = models.CharField(max_length=200)
    image = models.URLField(default="https://i.ibb.co/8P7ycd3/devops-3155973-1920.jpg", null=True, blank=True)
    
    def __str__ (self):
        return self.name


class UserCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid  = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.course}, {self.user.username}, {self.paid}"
        # return "usercourse" + self.user.username + self.course




class UserCourseProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paystack_ref_id = models.CharField(max_length=50)
    user_training_id = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username + self.course




class WhatYouWillLearn(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='what_you_will_learn')
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=300)
    def __str__(self):
        return self.title                                  



class AboutCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='about_course')
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=300)
    def __str__(self):
        return self.title

class CourseImage(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_image')
    image = models.URLField(default="https://i.ibb.co/8P7ycd3/devops-3155973-1920.jpg", null=True, blank=True)


class CourseTestimonial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_testimonials')
    name = models.CharField(max_length=300)
    text = models.CharField(max_length=300)




# the Truth 	
# Tesla 	
# Cut Throat City
# Juliet, Naked
#  	Valerian and the City of a Thousand Planets 
#      Maggie's Plan
#      BoyhoodBoyhood 	
# First Reformed