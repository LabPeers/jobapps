
# todo/serializers.py

from rest_framework import serializers
from .models import Jobapps
      
class JobappsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Jobapps
    fields = ('id', 'title', 'description', 'company', 'myLocation', 'myDate', 'completed')