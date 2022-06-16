from django.db import models

# Create your models here.
from django.db import models

class Device(models.Model):
    name = models.CharField('제품명', max_length=100, blank=True)
    price = models.IntegerField()
    release_date = models.CharField('발매일', max_length=100, blank=True) # 발매
    image_name = models.CharField('이미지명', max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '제품명: {0}\n 가격: {1}원\n'.format(self.name, self.price)

    def getImagePath(self):
        if(self.image_name):
            imagePath = "/static/images/"+self.image_name
        else:
            imagePath = "/static/images/noImage.jpg"
        return imagePath
