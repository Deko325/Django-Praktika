from django.contrib import admin

from vetsite.models import *


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']


class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'education']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ContactFormsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

    class Meta:
        verbose_name = 'Формы контакты'


admin.site.register(Services, ServicesAdmin)
admin.site.register(Contact, ContactFormsAdmin)
admin.site.register(Doctors, DoctorsAdmin)
admin.site.register(Category, CategoryAdmin)
