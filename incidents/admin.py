from django.contrib import admin

# Register your models here.
from django.contrib import admin


from incidents.models import Incident

admin.site.register(Incident)
