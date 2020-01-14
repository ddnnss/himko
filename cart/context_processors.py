from .models import Cart

def items_in_cart(request):
    s_key = request.session.session_key
    all_items_in_cart = Cart.objects.filter(client=s_key)
    count_items_in_cart = all_items_in_cart.count()
    all = 'all'



    return locals()