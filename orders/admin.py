from django.contrib import admin
from .models import Cart, CartItem, Coupon


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at', 'updated_at')
    inlines = [CartItemInline]


class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active',)


admin.site.register(Cart, CartAdmin)
admin.site.register(Coupon, CouponAdmin)
