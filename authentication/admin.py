from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import RoleModel, UserModel

@admin.register(RoleModel)
class RoleAdmin(ModelAdmin):
    list_display = ('id', 'name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    ordering = ('id',)

@admin.register(UserModel)
class UserAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'status', 'is_staff', 'is_superuser', 'role')
    list_filter = ('status', 'is_staff', 'is_superuser', 'role')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('id',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name')}),
        ('Permisos', {'fields': ('is_staff', 'is_superuser', 'role')}),
        ('Estado', {'fields': ('status',)}),
        ('Fechas', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')