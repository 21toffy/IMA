# Generated by Django 2.2.5 on 2020-09-22 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('text', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('landing_image', models.ImageField(blank=True, default='https://i.ibb.co/8P7ycd3/devops-3155973-1920.jpg', null=True, upload_to='blog_images/')),
                ('img2', models.ImageField(blank=True, default='https://i.ibb.co/8P7ycd3/devops-3155973-1920.jpg', null=True, upload_to='blog_images/')),
                ('img3', models.ImageField(blank=True, default='https://i.ibb.co/8P7ycd3/devops-3155973-1920.jpg', null=True, upload_to='blog_images/')),
                ('img4', models.ImageField(blank=True, default='https://i.ibb.co/8P7ycd3/devops-3155973-1920.jpg', null=True, upload_to='blog_images/')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('img6', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
                ('vid', models.FileField(blank=True, null=True, upload_to='blog_video/')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('category', models.CharField(choices=[('Event', 'Event'), ('Training', 'Training'), ('Blog Post', 'Blog Post'), ('Tutorial', 'Tutorial')], default='Blog Post', max_length=20)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
