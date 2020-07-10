from django.forms import ModelForm
from cart.models import Order

class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('name','phone','email','doc',)
        exclude = ()