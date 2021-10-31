from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Organization)
admin.site.register(OrganizationPosts)
admin.site.register(DVDBenchTrainingData)

admin.site.register(DVDBenchTestingData)
admin.site.register(NDBenchTrainingData)
admin.site.register(NDBenchTestingData)
