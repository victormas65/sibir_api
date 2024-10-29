from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import CustomerModel, PostModel

@admin.register(CustomerModel)
class CustomerAdmin(ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'address', 'document_number', 'email', 'status')
  list_filter = ('status',)
  search_fields = ('first_name', 'last_name', 'email')
  ordering = ('first_name',)
  fieldsets = (
    (None, {'fields': ('first_name', 'last_name', 'address', 'document_number', 'email')}),
    ('Estado', {'fields': ('status',)}),
  )

@admin.register(PostModel)
class PostAdmin(ModelAdmin):
  list_display = ('id', 'title', 'description', 'status', 'customer', 'holding')
  list_filter = ('status',)
  search_fields = ('customer', 'holding', 'title', 'description')
  ordering = ('holding','customer')
  fieldsets = (
    (None, {'fields': ('title', 'description')}),
    ('Estado', {'fields': ('status',)}),
    ('Fechas', {'fields': ('created_at', 'updated_at')}),
  )
  readonly_fields = ('created_at', 'updated_at')

# Register your models here.
