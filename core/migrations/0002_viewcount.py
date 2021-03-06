# Generated by Django 3.1.1 on 2020-10-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(choices=[('Home', 'Home'), ('About', 'About'), ('Courses', 'Courses'), ('Blog', 'Blog'), ('Contact', 'Contact'), ('Event', 'Event')], default='Home', max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'ViewCount',
                'verbose_name_plural': 'ViewCounts',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
