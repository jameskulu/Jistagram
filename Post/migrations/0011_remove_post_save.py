# Generated by Django 3.1.1 on 2020-09-21 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0010_remove_post_archive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='save',
        ),
    ]
