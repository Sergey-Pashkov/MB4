"""""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Report, Constant
from django.contrib import admin
from .models import Client, WorkType, Constant, UnusualOperationLog 
from django.contrib import admin
from .models import Client, WorkType, Constant, UnusualOperationLog
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

from django.contrib import admin
from .models import WorkType


@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_norm', 'price_category', 'comments')
    list_filter = ('price_category',)
    search_fields = ('name', 'comments')

from django.contrib import admin
from .models import Client, WorkType, Constants, UnusualOperationLog

@admin.register(UnusualOperationLog)
class UnusualOperationLogAdmin(admin.ModelAdmin):
    list_display = ('operation_content', 'duration_minutes', 'client', 'price_category', 'operation_cost', 'timestamp')
    list_filter = ('client', 'price_category', 'timestamp')
    search_fields = ('operation_content', 'client__name', 'client__inn')

"""
from django.contrib import admin
from .models import Client, WorkType, Constant, UnusualOperationLog, Report, CustomUser

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'contract_price')
    search_fields = ('name', 'inn')

@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_category', 'time_norm', 'comments')
    list_filter = ('price_category',)
    search_fields = ('name', 'comments')

@admin.register(Constant)
class ConstantAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    search_fields = ('name',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')
    search_fields = ('username', 'email')

from django.contrib import admin
from .models import UnusualOperationLog

class UnusualOperationLogAdmin(admin.ModelAdmin):
    list_display = ('operation_content', 'duration_minutes', 'operation_cost', 'client', 'price_category', 'author', 'timestamp')

admin.site.register(UnusualOperationLog, UnusualOperationLogAdmin)


from django.contrib import admin
from .models import StandardOperationLog

@admin.register(StandardOperationLog)
class StandardOperationLogAdmin(admin.ModelAdmin):
    list_display = ('client', 'worktype', 'time_norm', 'price_category', 'cost_per_minute', 'operation_cost', 'author', 'timestamp')
    list_filter = ('client', 'worktype', 'price_category', 'author')
    search_fields = ('client__name', 'worktype__name', 'author__username')
    readonly_fields = ('time_norm', 'price_category', 'cost_per_minute', 'operation_cost', 'author')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)
