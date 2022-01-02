# Generated by Django 3.2.8 on 2021-12-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseManagement', '0002_billingaddress_coupon_order_ordercourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='course',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(null=True, to='CourseManagement.Category', verbose_name='category of course'),
        ),
    ]
