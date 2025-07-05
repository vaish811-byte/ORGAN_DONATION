from django.contrib import admin
from .models import Donor, Recipient

admin.site.register(Donor)
admin.site.register(Recipient)
