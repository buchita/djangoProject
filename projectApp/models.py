from django.db import models

# class BlobImg(models.Model):
#     photo = models.TextField(null=True)

class Flower(models.Model):
    # id = models.CharField(max_length=3)
    # description = models.CharField(max_length=100)
    caption = models.CharField(max_length=100, default='')
    flowerName = models.CharField(max_length=100)
    # id = models.IntegerField(default=0)

    # img = models.ImageField(upload_to='flower_folder', default='')
    # blob
    img = models.TextField(null=True)

    #------------------------------------
    # converting blob to base 64
    # _img = models.TextField(db_column='image', blank=True)
    # def set_data(self, data):
    #     self._img = base64.encodebytes(data)
    #
    # def get_data(self, data):
    #     return base64.decodebytes(self._img)
    # img = property(get_data, set_data)

    # ------------------
    # def __init__(self):
    #     return self.description

    class Meta:
        db_table = "image"

    def __str__(self):
        #return self.description

        return self.flowerName



# file uploader
class ImageForm(models.Model):
    file = models.ImageField(upload_to='images/%Y/%m/%d')

    # class Meta:
    #     db_table = "prediction"

    def __str__(self):
        return self.file
