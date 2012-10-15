from django.db import models

class Route(models.Model):
  link_id = models.CharField(max_length=8)
  user_name = models.CharField(max_length=40)
  message = models.CharField(max_length=140)
  start_lat = models.FloatField()
  start_lng = models.FloatField()
  end_lat = models.FloatField()
  end_lng = models.FloatField()
  end_name = models.CharField(max_length=100)
  effective_time = models.DateTimeField()
  created_time = models.DateTimeField(auto_now=True)
