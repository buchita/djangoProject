from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from projectApp.templates.form import UserForm
from projectApp.models import Flower
from .form import Image_uploader

from djangoProject import settings
import base64

def home(request):
    current_user = "Thomas"
    # return HttpResponse(index_home)

    obj1 = Flower.objects.get(id=1)
    # obj = Flower.objects.all()
    image_data1 = base64.b64encode(obj1.img).decode()

    data1 = {
        'flowerName': obj1.flowerName,
        'image': image_data1
    }

    obj2 = Flower.objects.get(id=2)
    image_data2 = base64.b64encode(obj2.img).decode()

    data2 = {
        'flowerName': obj2.flowerName,
        'image': image_data2
    }
    data_array = [data1, data2]
    data_dict = {}
    index = 0
    for x in data_array:
        key = "key" + '_' + str(index)
        data_dict[key] = x
        index = index + 1



    return render(request, 'home.html',
                  data_dict)

# write to db
def upload_file(request):
    # return HttpResponse(index_home)
# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
    # creates a request for POST
    if request.method == "POST":
        form = Image_uploader(request.POST, request.FILES)

        # form is validated
        if form.is_valid():
            try:
                # form is saved
                form.save()
                # then redirected to /view
                return redirect('home')
            except:
                pass
    # if something is wrong, will be directed back to html page
    else:
        form = Image_uploader()
        return render(request, 'uploader.html', {'form': form})


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

