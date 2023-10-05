from django.db import models


# Create your models here.


class cosmetics(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cost = models.CharField(max_length=255)
    seller = models.CharField(max_length=255)
    image_pic = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date_created = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # get, filter, exclude, order_by - для БД ORM
    # database.objects.create - сохранение без подтверждения
