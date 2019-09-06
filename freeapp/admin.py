from django.contrib import admin
from .models import Activity, Comment, ActivityPart
# Register your models here.
admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(ActivityPart)
