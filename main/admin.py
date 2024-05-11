from django.contrib import admin
from .models import Country, BetResult, Bet

# Register your models here.
admin.site.register(Country)
admin.site.register(Bet)
admin.site.register(BetResult)