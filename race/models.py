from django.db import models
from TyprrrUser.models import TyprrrUser
from django.utils import timezone
from django.db.models.signals import pre_save
from datetime import datetime
from typrrr.utils import code_generator


class Race(models.Model):
    code = models.IntegerField(primary_key=True, editable=False)
    started = models.DateTimeField(auto_now_add=True)
    host = models.ForeignKey(TyprrrUser, on_delete=models.CASCADE, related_name='host')
    users_joined = models.ManyToManyField(TyprrrUser, related_name='users_joined')

    def before_save(sender, instance, *args, **kwargs):
        instance.code = code_generator()

    def __str__(self) -> str:
        return str(f'Race {self.code}')


pre_save.connect(Race.before_save, sender=Race)
