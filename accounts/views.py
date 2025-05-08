from django.shortcuts import render, redirect
from django.contrib import messages
from . models import RegisterTable

def Home(request):
    return render(request, 'accounts/basepage.html')

#--------------------------------------------------------------------------------------

def AdminLoginPage(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("Admin:" , username , password)
        if username == 'admin' and password == 'admin':
            messages.success(request,'Welcome Admin')
            return redirect('admins:admin-home')
        else:
            messages.error(request,'Please Enter valid Details')
            return redirect('accounts:admin-login')
         
     return render(request, 'accounts/adminlogin.html')

#---------------------------------------------------------------------------------------

def UserLoginPage(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            loguser = RegisterTable.objects.get(username=username, password=password)
            if loguser.is_active:
                request.session['username'] = username
                messages.success(request, f'Welcome-{username}')
                return redirect('users:user-base')
            else:
                messages.error(request, 'Account is not activated')
                return redirect('accounts:user-login')
        except RegisterTable.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return redirect('accounts:user-login')
    return render(request, 'accounts/login.html')

#---------------------------------------------------------------------------------------


def UserRegisterPage(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        address = request.POST['address']

        if RegisterTable.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif RegisterTable.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            user = RegisterTable(name=name,username=username,password=password,email=email,address=address,)
            user.save()
            messages.success(request, 'User registered successfully')
            print('registration success....................')
    print('Problem with Rgister..')   
    return render(request, 'accounts/register.html')

#--------------------------------------------------------------------------------------------------------------------------