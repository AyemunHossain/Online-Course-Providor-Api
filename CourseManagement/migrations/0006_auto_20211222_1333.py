# Generated by Django 3.2.8 on 2021-12-22 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CourseManagement', '0005_auto_20211217_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='coupon',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ordercourse',
            name='item',
        ),
        migrations.RemoveField(
            model_name='ordercourse',
            name='user',
        ),
        migrations.DeleteModel(
            name='BillingAddress',
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderCourse',
        ),
    ]
