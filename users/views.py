
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method =="POST":
        data = UserCreationForm(request.POST)
        if data.is_valid():
            username = data.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created 🥳')
            data.save()
            return redirect('blogs-home')
        else:
            return render(request, 'register.html',{'forms':data})
    
    else:
        data = UserCreationForm()        
    return render(request, 'register.html',{'forms':data})
    