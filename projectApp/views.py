from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    current_user = "Thomas"

    # return HttpResponse(index_home)

    return render(request, 'home.html',
                  {'login': current_user})