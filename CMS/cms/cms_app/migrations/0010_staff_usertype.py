# Generated by Django 4.0.3 on 2024-12-23 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0009_remove_staff_email_remove_staff_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='usertype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_type', to=settings.AUTH_USER_MODEL),
        ),
    ]
