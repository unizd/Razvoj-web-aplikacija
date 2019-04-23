from django.contrib import admin

# Register your models here.
from .models import Nekretnina


admin.site.register(
    [
        Nekretnina
	]
)