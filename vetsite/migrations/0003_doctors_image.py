# Generated by Django 4.2 on 2023-04-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetsite', '0002_doctors_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='image',
            field=models.ImageField(default='defaultimage.png', upload_to='doctors/', verbose_name='Фотографии'),
        ),
    ]
