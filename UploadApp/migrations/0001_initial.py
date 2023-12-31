# Generated by Django 4.1.5 on 2023-05-23 11:41

import UploadApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=UploadApp.models.extension_directory_path)),
                ('size', models.PositiveBigIntegerField()),
                ('uploaded', models.DateField(auto_now=True)),
            ],
        ),
    ]
