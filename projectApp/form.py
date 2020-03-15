from django.db import models
from django import forms
from .models import ImageModel


class DocmentForm(forms.Form):
    file = forms.ImageField(label="select image", help_text="only .jpg or .png")



# https://stackoverflow.com/questions/25479254/in-django-restrict-image-file-upload-by-file-type
def clean_image(self):
    cleaned_data = super(ImageModel, self).clean()
    photo = cleaned_data.get("photo")
    if photo:
        if not photo.name[-3:].lower() in ['jpg']:
            raise forms.ValidationError("Your file extension was not recongized")
    return photo