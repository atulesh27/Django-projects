from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserData

# Create your views here.

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'userapp/user_form.html', {'form': form})

def success(request):
    return render(request, 'userapp/success.html')

