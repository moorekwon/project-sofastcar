from django.db import models


# Create your models here.
class CarZone(models.Model):
    zone_id = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=20, default='seoul')

    # 위도, 경도 (단위: Degree)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    sub_info = models.CharField(max_length=100, default='')
    detail_info = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=10, default='')
    operating_time = models.CharField(max_length=10, default='24시간')


