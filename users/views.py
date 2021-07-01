
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, UserUpadateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
# Create your views here.
def register(request):
    if request.method =="POST":
        data = UserRegisterForm(request.POST)
        if data.is_valid():
            username = data.cleaned_data.get('username')
            messages.success(request, 'Your New account has been created. LogIn.....')
            data.save()
            return redirect('login')
        else:
            return render(request, 'register.html',{'forms':data})
    
    else:
        data = UserRegisterForm()        
    return render(request, 'register.html',{'forms':data})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpadateForm(request.POST,instance =request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your Account has been updated')
            redirect ('profile')
    else:
        u_form = UserUpadateForm(instance =request.user)
        p_form = ProfileUpdateForm(request.FILES, instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'profile.html', context)

