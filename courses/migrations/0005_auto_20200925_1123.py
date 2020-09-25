# Generated by Django 2.2.5 on 2020-09-25 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_course', to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='coursetestimonial',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_testimonials', to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='whatyouwilllearn',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='what_you_will_learn', to='courses.Course'),
        ),
    ]