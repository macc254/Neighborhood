from django.contrib import admin
from .models import NeighbourHood, Profile,Post
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(NeighbourHood)

