from django import forms
from .models import CartItem, Coupon


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['code']
