from django.contrib import admin
from .models import DiscountCode,Product,Cart,CartItem
# Register your models here.

admin.site.register(DiscountCode)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
