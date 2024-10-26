from .models import CartItem

def cart_item_count(request):
    count = CartItem.objects.filter(cart__user=request.user).count() if request.user.is_authenticated else 0
    return {'cart_item_count': count}