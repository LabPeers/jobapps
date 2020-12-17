
# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import JobappsSerializer      # add this
from .models import Jobapps                     # add this
        
class JobappsView(viewsets.ModelViewSet):       # add this
  serializer_class = JobappsSerializer          # add this
  queryset = Jobapps.objects.all()              # add this