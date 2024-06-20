from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Report, Constant

# Определяем админ-класс для модели CustomUser
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('user_type',)}),
    )

# Регистрируем модель CustomUser с кастомным админ-классом
admin.site.register(CustomUser, CustomUserAdmin)

# Регистрируем модель Report
admin.site.register(Report)

# Определяем админ-класс для модели Constant
@admin.register(Constant)
class ConstantAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'comment')  # Поля для отображения в списке
    search_fields = ('name',)  # Поля для поиска



# admin.py
from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'org_form', 'inn', 'contract_price', 'tax_system', 'contract_details', 'contact_person', 'phone', 'email', 'postal_address', 'comments')

admin.site.register(Client, ClientAdmin)
