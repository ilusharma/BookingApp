from django.db import models
from datetime import timedelta

# Create your models here.
class ConferenceRoom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    def __str__(self):
        return self.name

class Reservation(models.Model):
    room = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    def __str__(self):
        return self.room.name + " " + str(self.date) + " " + str(self.start_time) + " " + str(self.end_time)