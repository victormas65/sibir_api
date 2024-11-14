from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import CategoryModel, HoldingModel
from cloudinary.uploader import upload

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
        (None, {'fields': ('name', 'description', 'address', 'category')}),
        ('Información personal', {'fields': ('image', 'price', 'bedr', 'bath', 'park')}),
        ('Estado', {'fields': ('status',)}),
        ('Fechas', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')

    # Sobrescribir el método save para subir la imagen a Cloudinary
    def save_model(self, request, obj, form, change):
        if 'image' in form.changed_data and form.cleaned_data['image']:
            image_file = form.cleaned_data['image']
            # Sube la imagen a Cloudinary
            upload_result = upload(image_file)
            # Guarda la URL pública de la imagen en el campo image
            obj.image = upload_result['url']
        super().save_model(request, obj, form, change)
