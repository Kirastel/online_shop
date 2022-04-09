from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Product, ProductImage, Categories


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4


class ProductAdminForm(forms.ModelForm):
    short_description = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'





@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]





@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ProductImage)
