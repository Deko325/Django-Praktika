# Generated by Django 4.2 on 2023-05-11 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetsite', '0013_category_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
        ),
    ]
