# Generated by Django 3.1.1 on 2020-09-22 12:09

import Post.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0013_post_save_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files', validators=[Post.models.file_size]),
        ),
    ]
