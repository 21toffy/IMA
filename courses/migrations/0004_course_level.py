# Generated by Django 2.2.5 on 2020-09-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Early Professionals', 'Early Professionals'), ('Professionals', 'Professionals'), ('Starters', 'Starters'), ('Experienced Professionals', 'Experienced Professionals'), ('Enthusiast', 'Enthusiasts'), ('Everyone', 'Everyone')], default='Starters', max_length=200),
        ),
    ]
