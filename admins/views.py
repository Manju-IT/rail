from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.models import RegisterTable

# def AdminBasePage(request):
#     return render(request, 'admins/adminbase.html')

#----------------------------------------------------------------------------------------

def AdminHomePage(request):
    return render(request, 'admins/adminhome.html')


#---------------------------------------------------------------------------------------

def UserListView(request):
    users = RegisterTable.objects.all()
    context ={
        'users':users,
    }
    return render(request, 'admins/userlist.html', context)

#---------------------------------------------------------------------------------------

def ActivateUser(request, pk):
    user = get_object_or_404(RegisterTable, id=pk)
    if user:
        user.is_active = True
        user.save()
        messages.success(request, f'User {user.username} has been activated.')

    return redirect('admins:user-list-view')

    # return render(request, 'admins/userlist.html')

#---------------------------------------------------------------------------------------

def DeactivteUser(request, pk):
    user = get_object_or_404(RegisterTable, id=pk)
    if user:
        user.is_active = False
        user.save()
        messages.success(request, f'User {user.username} has been Deactivated.')

    return redirect('admins:user-list-view')

#---------------------------------------------------------------------------------------

def AdminLogout(request):
    return render(request, 'accounts/index.html')

#---------------------------------------------------------------------------------------
