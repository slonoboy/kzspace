from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(BurialPlace)
admin.site.register(Deceased)
admin.site.register(Account)
admin.site.register(Cemetery)
admin.site.register(Application)