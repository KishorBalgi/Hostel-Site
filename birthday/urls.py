from django.contrib import admin
from django.urls import path
from wishes.views import wishes
from .views import homepage, gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wishes/', wishes, name='wishes'),
    path('gallery/', gallery, name='gallery'),
    path('', homepage, name='home'),
]
