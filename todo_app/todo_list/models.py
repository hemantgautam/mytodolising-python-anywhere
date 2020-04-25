from django.db import models
from django.contrib.auth.models import User, auth
from django.conf import settings


# Create your models here.
class TodoList(models.Model):
    item = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)
    userid = models.IntegerField(default=1, null=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    board_id = models.ForeignKey('BoardList', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.item


class BoardList(models.Model):
    board_name = models.CharField(max_length=50)
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )

    def __str__(self):
        return self.board_name
