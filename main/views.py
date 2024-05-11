from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Country, Bet
from .forms import BetForm

# Create your views here.
def index(request):
    return render(request, 'countries.html')

def fetchCountry(request, country):
    hasVoted = False  # Initialize hasVoted variable
    countryObject = Country.objects.get(country=country)
    
    if request.method == 'POST':
        form = BetForm(request.POST)
        if form.is_valid():
            bet = form.save(commit=False)
            bet.user = request.user  # Assuming user is logged in
            bet.country = Country.objects.get(country=country)

            # Check if the user has already made a bet for this country
            if Bet.objects.filter(user=request.user, country=countryObject).exists():
                hasVoted = True
            else:
                bet.save()
                return redirect('fetchCountry', country)  # Redirect to a success page
    else:
        form = BetForm()

        # Check if the user has already made a bet for this country
        if Bet.objects.filter(user=request.user, country=countryObject).exists():
            hasVoted = True

    context = {
        'country': country,
        'form': form,
        'page': country,
        'hasVoted': hasVoted
    }
    return render(request, 'country.html', context)