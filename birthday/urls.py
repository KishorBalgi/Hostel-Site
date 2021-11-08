from django.contrib import admin
from django.urls import path
from wishes.views import memories
from .views import homepage, moments

urlpatterns = [
    path('admin/', admin.site.urls),
    path('memories/', memories, name='memories'),
    path('moments/', moments, name='moments'),
    path('', homepage, name='home'),
]
