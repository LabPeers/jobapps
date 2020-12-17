

from django.db import models
# Create your models here.

# add this
class Jobapps(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  company = models.CharField(max_length=120, default = None)
  myLocation = models.CharField(max_length=120, default = None)
  myDate = models.DateTimeField(auto_now=True)
  completed = models.BooleanField(default=False)
      
  def __str__(self):
    return self.title