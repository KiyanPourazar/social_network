import uuid

from django.db import models
from django.conf import settings

class Country(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=5)
    is_enabled = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Countries'
        verbose_name_plural = 'Countries'
        db_table = 'countries'

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(to = settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(blank= True, null=True , unique=True)
    country = models.ForeignKey(to = Country, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', blank=True)

class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4
    DEVICE_CHOICES = (
        (DEVICE_WEB, 'web'),
        (DEVICE_IOS, 'ios'),
        (DEVICE_ANDROID, 'android'),
        (DEVICE_PC, 'pc'),
    )

    user = models.ForeignKey(to = settings.AUTH_USER_MODEL,related_name='devices' ,on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device UUID',default=uuid.uuid4, editable=False, unique=True)
    last_login = models.DateTimeField('last login date',auto_now=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_CHOICES, default=DEVICE_WEB)
    device_os = models.IntegerField('device os',max_length=20, blank=True)
    device_model = models.IntegerField('device model',max_length=50, blank=True)
    app_version = models.IntegerField('app version',max_length=20, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
