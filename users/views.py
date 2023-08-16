from django.shortcuts import render


def view_login(request):
    return render(request, 'login.html')
    