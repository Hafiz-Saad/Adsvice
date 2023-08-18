from django.shortcuts import render
from django.http import HttpResponse


def view_login(request):
    return render(request, 'login.html')
    
def view_callback(request):
    print(request)
    print(request.GET)

    return HttpResponse('Done')

def privacy_policy(request):
    return HttpResponse('Privacy')
