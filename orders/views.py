from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Product, Coupon
from .forms import CartItemForm, CouponForm


@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cart_items.all()
    cart_total = cart.total_price

    coupon_form = CouponForm()
    if request.method == 'POST':
        coupon_form = CouponForm(request.POST)
        if coupon_form.is_valid():
            coupon = coupon_form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code=coupon, is_active=True)
                cart.total_price = cart.total_price * (1 - coupon.discount_percent / 100)
                cart.save()
            except Coupon.DoesNotExist:
                pass

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'coupon_form': coupon_form
    }
    return render(request, 'orders/cart.html', context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item_form = CartItemForm(request.POST, instance=cart_item)
        if cart_item_form.is_valid():
            cart_item_form.save()
    else:
        cart.total_price += product.price
        cart.save()
    return redirect('orders:cart')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart = cart_item.cart
    cart.total_price -= cart_item.product.price * cart_item.quantity
    cart.save()
    cart_item.delete()
    return redirect('orders:cart')


@login_required
def update_cart_item(request, cart_item_id):
    """
    Update the quantity of an item in the cart.
    """
    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity'))

        # Update the quantity of the cart item
        cart_item.quantity = new_quantity
        cart_item.save()

        return redirect('cart')

    context = {
        'cart_item': cart_item
    }

    return render(request, 'orders/update_cart_item.html', context)
