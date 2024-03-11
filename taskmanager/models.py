from django.db import models
from utils.models import BaseModel
# Create your models here.


class BaseTask(BaseModel):
    COLOE_CHOICES = [
        ('#FF0000','Red')
    ]
    STATUS_CHOICES = [
        ('PENDING','Pending')
        ('DONE','Done'),
    ]
    title = models.TextField()
    description = models.TextField()
    color = models.CharField( max_length=50)
    date = models.DateField()
    status = models.CharField(max_length = 20)

    class Meta:
        abstaract = True

    def __str__(self) -> str:
        return self.title


class Task(BaseTask):
    pass


class RepeatingTask(BaseTask):
    TIME_FRAME_CHOICES = [
    ('DAILY','daily'),
    ('WEEKLY','weekly'),
    ('MONTHLY','monthly'),
    ('YEARLY','yearly')
]
    timeframe = models.CharField(max_length=50,choices = TIME_FRAME_CHOICES)



    


