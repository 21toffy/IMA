# Generated by Django 3.1.1 on 2020-10-02 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'HomeView',
                'verbose_name_plural': 'HomeViews',
                'db_table': '',
                'managed': True,
            },
        ),
    ]