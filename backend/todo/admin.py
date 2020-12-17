
# todo/admin.py
    
from django.contrib import admin
from .models import Jobapps # add this
    
class JobappsAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description', 'company', 'myLocation', 'myDate', 'completed') # add this
        
# Register your models here.
admin.site.register(Jobapps, JobappsAdmin) # add this