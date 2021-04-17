from django.contrib import admin

# Register your models here.
from .models import User, Barrel, Account, Note, Alert

admin.site.register(User)
admin.site.register(Barrel)
admin.site.register(Account)
admin.site.register(Note)
admin.site.register(Alert)
