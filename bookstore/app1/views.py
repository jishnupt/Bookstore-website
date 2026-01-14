from django.shortcuts import render,redirect
from .forms import ReguserForm
# Create your views here.

def homepage(request):
    return render(request,'home.html')


def UserRegistration(request):
    if request.method == 'POST':
        form = ReguserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(homepage)
    else:
        form = ReguserForm()
    return render(request,'user_reg.html',{'form':form})
