from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # DB에 저장되지 않도록 abstract 설정을 해줌
