from django.contrib import admin
from .models import Wishes

@admin.register(Wishes)
class WishesAdmin(admin.ModelAdmin):
    pass