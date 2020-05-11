from django.contrib import admin
# Register your models here.
from django.forms import ModelForm
from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from suit_ckeditor.widgets import CKEditorWidget
from main.models import Master, Reception, UserProfile, MasterUsl, ContactsForm, Stock, StockReserv
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# from .models import UserProfile

class ReceptionInline(TabularInline):
    model = Reception


class MasterForm(ModelForm):
    class Meta:
        widgets = {
            'info': CKEditorWidget(editor_options={'startupFocus': True})
        }


class MasterAdmin(ModelAdmin):
    form = MasterForm
    inlines = [ReceptionInline,]


class ReceptionForm(ModelForm):
    class Meta:
        widgets = {
            'client_info': CKEditorWidget(editor_options={'startupFocus': True})
        }


class ReceptionAdmin(ModelAdmin):
    form = ReceptionForm



class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)

class MasterUslAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    verbose_name_plural = 'Услуги мастера'

class ContactsFormAdmin(admin.ModelAdmin):
    list_display = ['person', 'mail', 'message']
    verbose_name_plural = 'Форма обратной связи'

class StockFormResAdmin(admin.ModelAdmin):
    list_display = ['persons','phone', 'mail', 'stockId']

    verbose_name_plural = 'Запись на Акции'

class StockFormAdmin(admin.ModelAdmin):
    list_display = ['nameStock', 'price', 'info']
    verbose_name_plural = 'Акции'

admin.site.register(StockReserv, StockFormResAdmin)
admin.site.register(Stock, StockFormAdmin)
admin.site.register(MasterUsl, MasterUslAdmin)
admin.site.register(ContactsForm, ContactsFormAdmin)

# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(Master,MasterAdmin)
admin.site.register(Reception,ReceptionAdmin)
