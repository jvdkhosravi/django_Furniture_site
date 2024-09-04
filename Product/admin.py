from django.contrib import admin

from Product.models import ProductTag, Product, ProductBrand, ProductCategory

# Register your models here.

admin.site.register(ProductTag)
admin.site.register(Product)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
