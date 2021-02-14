from django.db import models


class HomeView(models.Model):
    time = models.DateTimeField(auto_now_add=True)

    def number(self):
        return HomeView.objects.all().count()

    def __str__(self):
        return self.time, ' Number of views Home page views: ',self.number()
    


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'HomeView'
        verbose_name_plural = 'HomeViews'







PAGE = (
    ("Home","Home"),
    ("About","About"),
    ("Courses","Courses"),
    ("Blog","Blog"),
    ("Contact","Contact"),
    ("Event","Event"),
)

class ViewCount(models.Model):

    page = models.CharField(choices=PAGE, max_length=20, default="Home")

    time = models.DateTimeField(auto_now_add=True)

    @property
    def home_count(self):
        return ViewCount.objects.filter(page='Home').count()

    @property
    def about_count(self):
        return ViewCount.objects.filter(page='About').count()

    @property
    def courses_count(self):
        return ViewCount.objects.filter(page='Courses').count()

    @property
    def blog_count(self):
        return ViewCount.objects.filter(page='Blog').count()
        
    @property
    def contact_count(self):
        return ViewCount.objects.filter(page='Contact').count()

    def __str__(self):
        return self.page
    


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ViewCount'
        verbose_name_plural = 'ViewCounts'