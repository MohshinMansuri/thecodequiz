from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return redirect('/quiz/already-registered/')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('quiz/')
    logout(request)
    return render(request, 'login.html')