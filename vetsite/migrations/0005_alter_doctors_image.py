# Generated by Django 4.2 on 2023-04-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetsite', '0004_alter_doctors_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='image',
            field=models.ImageField(default='defaultimage.png', upload_to='media/', verbose_name='Фотографии'),
        ),
    ]
