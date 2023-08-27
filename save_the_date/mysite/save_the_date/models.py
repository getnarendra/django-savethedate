
# Create your models here.
from django.db import models

class SaveTheDate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    # date = models.DateField()
    # time = models.TimeField()
    event_date = models.DateTimeField("event_date")
    venue = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("pub_date")
    # pub_date = models.DateTimeField()