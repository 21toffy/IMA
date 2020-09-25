from django.contrib import admin

from .models import Course, UserCourse, UserCourseProfile, WhatYouWillLearn ,AboutCourse, CourseImage, CourseTestimonial


admin.site.register(Course)

admin.site.register(UserCourse)

admin.site.register(UserCourseProfile)

admin.site.register(WhatYouWillLearn)

admin.site.register(AboutCourse)

admin.site.register(CourseImage)

admin.site.register(CourseTestimonial)


