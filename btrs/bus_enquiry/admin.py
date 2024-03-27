from django.contrib import admin

# Register your models here.

# Register your models here.
# bus_enquiry/admin.py

from django.contrib import admin
from bus_enquiry.models import Bus, User, Book

admin.site.register(Bus)
admin.site.register(User)
admin.site.register(Book)


