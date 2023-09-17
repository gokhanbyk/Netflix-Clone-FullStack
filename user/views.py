from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_request(request):
    # if request.method == 'POST':
        # email = request.POST['email']
        # password = request.POST['password']
        # username = CustomUser.objects.get(email = email).username

    if request.user.is_authenticated:
        return redirect('profile_page')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            username = CustomUser.objects.get(email = email).username

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('profile_page')
            else:
                return render(request, 'login.html', {
                    'form': form,
                })
        else:
            return render(request, 'login.html', {
                'form': form,
            })
    form = UserLoginForm()

    return render(request, 'login.html', {
        'form': form,
    })

def register_request(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect('profile_page')
        else:   
            form = RegisterForm()
            return render(request, 'register.html', {
                'form':form
            })
            
    form = RegisterForm()
    return render(request, 'register.html', {
        'form':form
    })



@login_required(login_url="/login/")
def profile_request(request):

    if request.method == 'POST':
        id = request.POST['silinecek']
        sil = Profile.objects.get(pk = id)

        sil.delete()
        return redirect('profile_page')


    profiller = request.user.profile_set.all()

    return render(request, 'profile.html', {
        'profiller': profiller
    })


@login_required(login_url="/login/")
def profile_manage(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            if request.user.profile_count() >= 5:
                #Hata Mesajı
                return redirect('profile_page')
    
            user = form.save(commit=False)
            user.owner = request.user
            user.save()
            return redirect('profile_page')
        else:
            return render(request, 'profile-yonetimi.html', {
                'form': form
            })
        
    form = UserProfileForm()
    return render(request, 'profile-yonetimi.html', {
        'form': form
    })

@login_required(login_url="/login/")
def hesap_ayarlari(request):
    profiller = request.user.profile_set.all()

    return render(request, 'hesap.html', {
        'profiller': profiller,
    })

@login_required(login_url="/login/")
def change_pass(request):
    form = ChangePass(request.user)

    if request.method == 'POST':
        form = ChangePass(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            id = request.user.id
            return redirect('profile_page')

    return render(request, 'changepass.html', {
        'form': form
    })

def logout_request(request):
    logout(request)

    return redirect('index')