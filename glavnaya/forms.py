
from django.forms import ModelForm
from .models import Zakaz

class ZakazForm(ModelForm):
    class Meta:
        model = Zakaz
        fields = ['name', 'email', 'city', 'otpravka', 'payment', 'koment']