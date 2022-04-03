from django.contrib import admin
from .models import Order, ProductInOrder, Contact


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]


admin.site.register(ProductInOrder)
admin.site.register(Contact)
