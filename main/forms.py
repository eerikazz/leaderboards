from django import forms
from .models import Bet

class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = ['bet_placement', 'bet_score']
