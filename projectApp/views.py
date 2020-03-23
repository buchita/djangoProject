import os

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from projectApp.models import Flower, TrainModel

# from .form import DocumentForm
from django.core.files.storage import FileSystemStorage
from projectApp.MachineLearning import image_quality_assessment, random_forest #import image_quality
from djangoProject import settings
import base64
# from .MachineLearning.random_forest import classifier

def home(request):
    obj1 = Flower.objects.get(id=1)
    # obj = Flower.objects.all()
    image_data1 = base64.b64encode(obj1.image).decode()

    data1 = {
        'flowerName': obj1.name,
        'image': image_data1
    }

    obj2 = Flower.objects.get(id=2)
    image_data2 = base64.b64encode(obj2.image).decode()

    data2 = {
        'flowerName': obj2.name,
        'image': image_data2
    }

    obj3 = Flower.objects.get(id=3)
    image_data3 = base64.b64encode(obj3.image).decode()

    data3 = {
        'flowerName': obj3.name,
        'image': image_data3
    }

    obj4 = Flower.objects.get(id=4)
    image_data4 = base64.b64encode(obj4.image).decode()

    data4 = {
        'flowerName': obj4.name,
        'image': image_data4
    }

    obj5 = Flower.objects.get(id=5)
    image_data5 = base64.b64encode(obj5.image).decode()

    data5 = {
        'flowerName': obj5.name,
        'image': image_data5
    }

    obj6 = Flower.objects.get(id=6)
    image_data6 = base64.b64encode(obj6.image).decode()

    data6 = {
        'flowerName': obj6.name,
        'image': image_data6
    }


    obj7 = Flower.objects.get(id=7)
    image_data7 = base64.b64encode(obj7.image).decode()

    data7 = {
        'flowerName': obj7.name,
        'image': image_data7
    }


    obj8 = Flower.objects.get(id=8)
    image_data8 = base64.b64encode(obj8.image).decode()

    data8 = {
        'flowerName': obj8.name,
        'image': image_data8
    }



    obj9 = Flower.objects.get(id=9)
    image_data9 = base64.b64encode(obj9.image).decode()

    data9 = {
        'flowerName': obj9.name,
        'image': image_data9
    }

    obj10 = Flower.objects.get(id=10)
    image_data10 = base64.b64encode(obj10.image).decode()

    data10 = {
        'flowerName': obj10.name,
        'image': image_data10
    }


    data_array = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]
    data_dict = {}
    index = 1
    for x in data_array:
        key = "key" + '_' + str(index)
        data_dict[key] = x
        index = index + 1

    return render(request, 'home.html',
                  data_dict)


# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
def upload_file(request):
    # using form and model
    # if request.method == 'POST':
    #     form = DocumentForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('display/')
    # else:
    #     # if its a get method
    #     # empty form to b filled in
    #     form = DocumentForm()
    # return render(request, 'uploader.html', {
    #     'form': form
    # })
    # basic file upload


    # this is the path to sace the image to /media/images directory
    image_root = os.path.join(settings.MEDIA_ROOT, 'images/')

    # this is for accessing the image after saved
    image_url = os.path.join(settings.MEDIA_URL, 'images/')

    # remove the \\ to /
    # image_root = image_root.replace("\\", "/")
    context = {}
    # when submitted
    # https://github.com/sibtc/django-upload-example/blob/master/mysite/core/views.py
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage(location=image_root, base_url=image_url)
        name = fs.save(uploaded_file.name, uploaded_file)
    #---------------------------------------------------
        uploade_url = image_url + name

        url = fs.url(name)
        print(url)
        print(uploade_url)
        # print("current directory")
        # print(os.getcwd())
        result = image_quality_assessment.image_quality(url)
        predict_result, percent = random_forest.classifier(url)

        context = { 'url': url, 'result': result, 'predict_result': predict_result, 'percent': percent}

    return render(request, 'uploader.html', context)


def display(request):
    im_ar = []
    for i in TrainModel.objects.all():
        image_data = ""
        print(i.id)
        image_data = base64.b64encode(i.image_dataset).decode()
        # print(image_data)
        image_quality_assessment.stringToRGB(image_data)
        im_ar.append(image_data)



    return render(request, 'display.html', {'flowers': im_ar})



# this is the beginning of the reading flower from the database
def DaisyInformation(request):
    # return HttpResponse(index_home)
    # https: // stackoverflow.com / questions / 56138525 / how - to - show - a - blob - image - on - html - page - in -django
    obj = Flower.objects.get(id=1)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'daisyInformation.html', data)


def BlanketFlower(request):
    # return HttpResponse(index_home)
    # https: // stackoverflow.com / questions / 56138525 / how - to - show - a - blob - image - on - html - page - in -django
    obj = Flower.objects.get(id=2)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'blanketFlower.html', data)


def Buttercup(request):
    obj = Flower.objects.get(id=3)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'buttercup.html', data)



def Carnation(request):
    obj = Flower.objects.get(id=4)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'carnation.html', data)


def Dandelion(request):
    obj = Flower.objects.get(id=5)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'carnation.html', data)


def CornPoppy(request):
    obj = Flower.objects.get(id=6)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'carnation.html', data)


def Lotus(request):
    obj = Flower.objects.get(id=7)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'lotus.html', data)


def Marigold(request):
    obj = Flower.objects.get(id=8)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'marigold.html', data)


def Sunflower(request):
    obj = Flower.objects.get(id=9)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'sunflower.html', data)


def Rose(request):
    obj = Flower.objects.get(id=10)
    # obj = Flower.objects.all()
    image_data = base64.b64encode(obj.image).decode()

    data = {
        'description': obj.description,
        'name': obj.name,
        'image': image_data
    }
    # flowers = Flower.objects.all()
    return render(request, 'rose.html', data)
