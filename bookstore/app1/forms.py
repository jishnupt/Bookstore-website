from django import forms
from .models import CustomUser,Add_cart
from django.contrib.auth.forms import UserCreationForm


class ReguserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email']

class AddcartForm(forms.ModelForm):
    class Meta:
        model = Add_cart
        fields = ['quantity']

