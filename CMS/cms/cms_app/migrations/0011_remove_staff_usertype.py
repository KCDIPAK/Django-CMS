# Generated by Django 4.0.3 on 2024-12-23 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0010_staff_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='usertype',
        ),
    ]
