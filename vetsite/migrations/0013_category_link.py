# Generated by Django 4.2 on 2023-05-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetsite', '0012_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='link',
            field=models.CharField(blank=True, max_length=50, verbose_name='URL'),
        ),
    ]
