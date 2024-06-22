from django.contrib import admin
from .models import *

admin.site.register(Post) #showUpTablePostOnAdminPage
admin.site.register(Tag)
