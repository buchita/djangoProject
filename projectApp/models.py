from django.db import models

class Flower(models.Model):
    # id = models.CharField(max_length=3)
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=2000, default='please add description')
    name = models.CharField(max_length=100)
    image = models.TextField(null=True)    # blob

    class Meta:
        db_table = "flower"

    def __str__(self):
        return self.name


class TrainModel(models.Model):
    image_id = models.IntegerField(primary_key=True)
    image_dataset = models.TextField(null=True)    # blob
    # id = models.ForeignKey(Flower, on_delete=models.CASCADE)
    id = models.IntegerField()

    class Meta:
        db_table = "dataset"

    def __str__(self):
        return self.image_dataset