from django.contrib import admin
from .models import CustomUser,Books,Add_cart

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Books)
admin.site.register(Add_cart)
