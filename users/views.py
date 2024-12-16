from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterform

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can login now.')
            return redirect('login')
    else:
        form = UserRegisterform()
    return render(request, 'users/register.html', {'form': form})

