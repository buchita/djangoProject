from django.contrib import admin
from .models import Flower
from .form import Image_uploader

# Register your models here.
admin.site.register(Flower)
admin.site.register(Image_uploader)
