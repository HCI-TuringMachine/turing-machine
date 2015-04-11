from django.contrib import admin

# Register your models here.
from .models import Requestor
from .models import Worker

admin.site.register(Requestor)
admin.site.register(Worker)