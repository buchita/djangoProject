from django.shortcuts import render, redirect
from django.http import HttpResponse
# from projectApp.templates.form import UserForm
from projectApp.models import Flower
from djangoProject import settings
import base64

def home(request):
    current_user = "Thomas"
    # return HttpResponse(index_home)

    # return render(request, 'home.html',
    #               {'flowers': current_user})
    return render(request, 'home.html',
                  {'flowers': current_user})

# # write to db
# def UserFormView(request):
#     # return HttpResponse(index_home)
#
#     # creates a request for POST
#     if request.method == "POST":
#         form = UserForm(request.POST)
#
#         # form is validated
#         if form.is_valid():
#             try:
#                 # form is saved
#                 form.save()
#                 # then redirected to /view
#                 return redirect('/view')
#             except:
#                 pass
#     # if something is wrong, will be directed back to html page
#     else:
#         form = UserForm()
#
#     return render(request, 'UserFormEntering.html', {'form': form})


def DaisyInformation(request):
    # return HttpResponse(index_home)
    # https: // stackoverflow.com / questions / 56138525 / how - to - show - a - blob - image - on - html - page - in -django
    obj = Flower.objects.get(id=1)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.img).decode()

    data = {
        'caption': obj.caption,
        'flowerName': obj.flowerName,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'daisyInformation.html', data)


def BeardIrisInformation(request):
    # return HttpResponse(index_home)
    # https: // stackoverflow.com / questions / 56138525 / how - to - show - a - blob - image - on - html - page - in -django
    obj = Flower.objects.get(id=2)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.img).decode()

    data = {
        'caption': obj.caption,
        'flowerName': obj.flowerName,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'beardediris.html', data)




def readDB(request):
    flowers = Flower.objects.all()
    return render(request, 'display.html', {'flowers': flowers})

