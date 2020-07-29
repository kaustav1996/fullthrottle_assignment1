from django.db import models

from timezone_field import TimeZoneField

class User(models.Model):
   id = models.CharField(primary_key=True,max_length=9)
   real_name = models.CharField(max_length=20)
   tz = TimeZoneField(default='Asia/Kolkata')


class ActivityPeriod(models.Model):
   # Should delete activity period once User is deleted 
   User = models.ForeignKey(User, on_delete=models.CASCADE)
   start_time = models.DateTimeField()
   end_time = models.DateTimeField()