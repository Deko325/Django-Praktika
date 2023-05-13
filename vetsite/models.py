from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return f'Сообщение от {self.name} (email: {self.email})'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Категории")
    image = models.ImageField(upload_to="media/", verbose_name="Изображение", default="defaultimage.png")
    link = models.CharField(max_length=50, verbose_name="URL", blank=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=245, verbose_name="Название услуги")
    price = models.IntegerField(default=999, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default='')

    def __str__(self):
        return self.name


class Doctors(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    description = models.TextField(verbose_name="Описание")
    education = models.CharField(max_length=50, verbose_name="Образование")
    image = models.ImageField(upload_to="media/", verbose_name="Фотографии", default="defaultimage.png")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default='')

    def __str__(self):
        return f'{self.surname} {self.name}'

