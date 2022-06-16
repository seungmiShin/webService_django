from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField('제품명', max_length=100, blank=True)
    price = models.IntegerField()
    category = models.CharField('카테고리', max_length=100, blank=True) # Best, New, all
    release_date = models.CharField('발매일', max_length=100, blank=True) # 발매
    created_date = models.DateTimeField(auto_now_add=True)
    image_name = models.CharField('이미지명', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

    def __str__(self):
        return '제품명: {0}\n 가격: {1}원\n 발매일: {2}\n'.format(self.name, self.price, self.release_date)

    def getImagePath(self):
        if(self.image_name):
            imagePath = "/static/images/"+self.image_name
        else:
            imagePath = "/static/images/noImage.jpg"
        return imagePath
