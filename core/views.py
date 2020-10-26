from django.shortcuts import render

# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(password)