# Generated by Django 3.2.8 on 2021-12-03 08:12

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default title !!!', max_length=450)),
                ('image', models.ImageField(blank=True, default='CourseDefault.jpg', null=True, upload_to='Course/%Y/%m/%d/', verbose_name='Main Image')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='Course/%Y/%m/%d/', verbose_name='2nd Image')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='Course/%Y/%m/%d/', verbose_name='3rd Image')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='Course/%Y/%m/%d/', verbose_name='4th Image')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Course Price')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Discount Price')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('additional_info', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False, verbose_name='Featured Course')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalCourse',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(default='Default title !!!', max_length=450)),
                ('image', models.TextField(blank=True, default='CourseDefault.jpg', max_length=100, null=True, verbose_name='Main Image')),
                ('image1', models.TextField(blank=True, max_length=100, null=True, verbose_name='2nd Image')),
                ('image2', models.TextField(blank=True, max_length=100, null=True, verbose_name='3rd Image')),
                ('image3', models.TextField(blank=True, max_length=100, null=True, verbose_name='4th Image')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Course Price')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Discount Price')),
                ('slug', models.SlugField(blank=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('additional_info', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False, verbose_name='Featured Course')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical course',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]