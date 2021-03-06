# Generated by Django 4.0 on 2022-01-18 19:13

from django.db import migrations, models
import settings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('url', models.URLField()),
                ('image', models.ImageField(max_length=255, upload_to=settings.models.slider_image_uploader)),
            ],
        ),
    ]
