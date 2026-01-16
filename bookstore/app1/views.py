from django.shortcuts import render,redirect
from .forms import ReguserForm,AddcartForm
from django.contrib.auth import authenticate,login,logout
from .models import Books,Add_cart
# Create your views here.

def homepage(request):
    book = Books.objects.all()
    return render(request,'home.html',{'book':book})

def UserRegistration(request):
    if request.method == 'POST':
        form = ReguserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(homepage)
    else:
        form = ReguserForm()
    return render(request,'user_reg.html',{'form':form})

def AdminRegistration(request):
    if request.method == 'POST':
        form = ReguserForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.role = 'admin'
            data.save()
            return redirect(homepage)
    else:
        form = ReguserForm()
    return render(request,'admin_reg.html',{'form':form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if user.role == 'user':
                return redirect(user_dashboard)
            if user.role == 'admin':
                return redirect(admin_dashboard)
    return render(request,'login.html')

def user_dashboard(request):
    book = Books.objects.all()
    return render(request,'user_page.html',{'book':book})

def admin_dashboard(request):
    return render(request,'admin_page.html')

def detail_page(request,bid):
    book = Books.objects.get(id=bid)
    return render(request,'detail_page.html',{'book':book})

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect(homepage)
    else:
        return render(request,'logout.html')
    
def Addcart_page(request,bid):
    book = Books.objects.get(id=bid)
    if request.method == 'POST':
        form = AddcartForm(request.POST)    
        if form.is_valid():
            data = form.save(commit=False)
            data.b_name = book
            data.userr = request.user
            data.save()
            return redirect(user_dashboard)
    else:
        form = AddcartForm()    
    return render(request,'Addcart.html',{'form':form})

def Cart_items(request):
    CartItem = Add_cart.objects.filter(userr=request.user)
    return render(request,'cart_items.html',{'CartItem':CartItem})
    

