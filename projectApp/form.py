from django.db import models


# file uploader
class Image_uploader(models.Model):
    file = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "prediction"

    def __str__(self):
        return self.file
