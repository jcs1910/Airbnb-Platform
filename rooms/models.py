
from django.db import models
from django_countries.fields import CountryField

from core                    import models as core_models
from users                   import models as user_models

class CommonInfo(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class RoomType(CommonInfo):

    pass

class Rooms(core_models.TimeStampedModel):

    name            = models.CharField(max_length= 60)
    description     = models.TextField()
    price           = models.IntegerField()
    address         = models.CharField(max_length= 150)
    country         = CountryField()
    city            = models.CharField(max_length= 80)
    guests          = models.IntegerField()
    beds            = models.IntegerField()
    bedrooms        = models.IntegerField()
    baths           = models.IntegerField()
    check_in        = models.TimeField()
    check_out       = models.TimeField()
    instant_booking = models.BooleanField(default= False)
    host            = models.ForeignKey(user_models.User, on_delete = models.CASCADE)
    room_type       = models.ManyToManyField(RoomType, blank= True)

    def __str__(self):
        return self.name

