from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
  CategoryModel,
  HoldingModel,
)

@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin):
  list_display = ('id', 'name', 'status')
  list_filter = ('status',)
  search_fields = ('name',)
  ordering = ('name',)

@admin.register(HoldingModel)
class HoldingAdmin(ModelAdmin):
  list_display = ('id', 'name', 'status')
  list_filter = ('status', 'bedr', 'bath', 'park')
  search_fields = ('name', 'bedr', 'bath', 'park')
  ordering = ('id',)
  fieldsets = (
    (None, {'fields': ('name', 'description', 'address')}),
    ('Información personal', {'fields': ('image', 'price', 'bedr', 'bath', 'park')}),
    ('Estado', {'fields': ('status',)}),
    ('Fechas', {'fields': ('created_at', 'updated_at')}),
  )
  readonly_fields = ('created_at', 'updated_at')