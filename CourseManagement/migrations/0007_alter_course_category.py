# Generated by Django 3.2.8 on 2021-12-30 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseManagement', '0006_auto_20211222_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='CourseManagement.Category', verbose_name='category of course'),
        ),
    ]
