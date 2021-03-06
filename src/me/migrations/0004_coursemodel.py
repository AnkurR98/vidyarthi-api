# Generated by Django 3.0.3 on 2020-06-15 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0003_auto_20200615_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('courseId', models.AutoField(primary_key=True, serialize=False)),
                ('courseTitle', models.CharField(max_length=512)),
                ('courseLink', models.CharField(max_length=512)),
                ('coursePublisher', models.CharField(max_length=512)),
                ('primaryTrack', models.CharField(max_length=512)),
                ('rating', models.IntegerField()),
                ('difficulty', models.IntegerField()),
                ('userId', models.CharField(max_length=512)),
            ],
        ),
    ]
