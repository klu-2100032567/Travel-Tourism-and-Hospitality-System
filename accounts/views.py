from django.shortcuts import render, redirect,HttpResponseRedirect,Products
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404\


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials...')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken...")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "user created...")
                return redirect('login')
        else:
            messages.info(request, "password not matched...")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def destinations(request):
    return render(request, 'destinations.html')

def packages(request):
    return render(request, 'packages.html')

def northindia(request):
    return render(request, 'northindia.html')

def southindia(request):
    return render(request, 'southindia.html')

def eastindia(request):
    return render(request, 'eastindia.html')

def westindia(request):
    return render(request, 'westindia.html')

def kashmirbook(request):
    return render(request, 'kashmirbook.html')

def punjabbook(request):
    return render(request, 'punjabbook.html')

def himachalpradeshbook(request):
    return render(request, 'himachalpradeshbook.html')

def delhibook(request):
    return render(request, 'delhibook.html')




def keralabook(request):
    return render(request, 'keralabook.html')

def biharbook(request):
    return render(request, 'biharbook.html')

def rajasthanbook(request):
    return render(request, 'rajasthanbook.html')

def andhrapradeshbook(request):
    return render(request, 'andhrapradeshbook.html')

def karnatakabook(request):
    return render(request, 'karnatakabook.html')

def tamilnadubook(request):
    return render(request, 'tamilnadubook.html')

def jharkhandbook(request):
    return render(request, 'jharkhandbook.html')

def orissabook(request):
    return render(request, 'orissabook.html')

def westbengalbook(request):
    return render(request, 'westbengalbook.html')

def gujaratbook(request):
    return render(request, 'gujaratbook.html')

def maharashtrabook(request):
    return render(request, 'maharashtrabook.html')

def madhyapradeshbook(request):
    return render(request, 'madhyapradeshbook.html')








