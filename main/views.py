from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Country, Bet, BetResult
from .forms import BetForm
from django.db.models import Count, Max, Q

# Create your views here.
@login_required
def index(request):
    return render(request, 'countries.html')

@login_required
def fetchCountry(request, country):
    hasVoted = False  # Initialize hasVoted variable
    countryObject = Country.objects.get(country=country)
    results = BetResult.objects.filter(country=countryObject).order_by('-accuracy')
    placement_queryset = results.order_by('bet_placement')
    score_queryset = results.order_by('bet_score')
   
    
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
        'hasVoted': hasVoted,
        'placement_results': placement_queryset,
        'score_results': score_queryset,
    }

    return render(request, 'country.html', context)


def global_leaderboard_view(request):
    # Query for users who have guessed the most countries right
    most_countries_guessed = BetResult.objects.values('user__username').annotate(
        total_correct_guesses=Count('id', filter=Q(correct_guess=True))
    ).order_by('-total_correct_guesses')

    # Query for users who have guessed the best on the score
    best_score_guessed = BetResult.objects.values('user__username').annotate(
        best_score=Max('accuracy')
    ).order_by('-best_score')

    context = {
            'page': 'leaderboard',
            'most_countries_guessed': most_countries_guessed,
            'best_score_guessed': best_score_guessed,
        }

    return render(request, 'leaderboard.html', context)