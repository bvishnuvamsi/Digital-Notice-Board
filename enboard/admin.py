from django.contrib import admin

from .models import Image
from . models import Video
from . models import Text

admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Text)


