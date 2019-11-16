from django.contrib import admin
from django.urls import path
import enboard.views
from . import views
from . import settings
from django.conf.urls.static import static

admin.site.site_header = 'MANOHAR AUTHENTICATION'                    # default: "Django Administration"
admin.site.index_title = 'UPLOAD YOUR IMAGES OR TEXT'                 # default: "Site administration"
admin.site.site_title = 'MANOHAR'               # default: "Django site admin"


urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', views.home, name='home1'),
    path('about/', enboard.views.about, name='about'),
    path('display/', enboard.views.display,name='display'),
    path('screen1/', enboard.views.screen1, name='screen1'),
    path('screen2/', enboard.views.screen2, name='screen2'),
    path('screen3/', enboard.views.screen3, name='screen3'),

              ] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
