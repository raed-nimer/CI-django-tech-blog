# Generated by Django 5.1.3 on 2024-12-29 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
    ]
