# Generated by Django 3.2.8 on 2021-12-15 08:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]