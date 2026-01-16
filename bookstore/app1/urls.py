from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homepage,name='homepage'),
    path('UserRegistration',UserRegistration,name='UserReg'),
    path('AdminRegistration',AdminRegistration,name='AdminReg'),
    path('loginpage',loginpage,name='login'),
    path('user_dashboard',user_dashboard,name='user_dashboard'),
    path('admin_dashboard',admin_dashboard),
    path('detail_page/<int:bid>',detail_page,name='detail_page'),
    path('logout_page',logout_page,name='logout'),
    path('Addcart_page/<int:bid>',Addcart_page,name='Addcart'),
    path('Cart_items',Cart_items,name='Cart_items')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)