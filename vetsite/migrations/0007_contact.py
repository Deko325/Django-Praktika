# Generated by Django 4.2 on 2023-05-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetsite', '0006_remove_doctors_category_remove_services_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
