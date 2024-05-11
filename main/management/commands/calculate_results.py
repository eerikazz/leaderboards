# myapp/management/commands/calculate_results.py

from django.core.management.base import BaseCommand
from user.models import Bet
from main.models import BetResult

class Command(BaseCommand):
    help = 'Calculate betting results after Eurovision final'

    def handle(self, *args, **options):
        # Retrieve all Bet objects
        bets = Bet.objects.all()

        # Loop through each Bet object
        for bet in bets:
            # Calculate accuracy and create BetResult object
            bet_result = BetResult(
                user=bet.user,
                country=bet.country,
                bet_placement=bet.bet_placement,
                actual_placement=bet.country.placement,  # Set actual placement from Country model
                bet_score=bet.bet_score,
                actual_score=bet.country.points,  # Set actual score from Country model
            )
            # Calculate accuracy and other statistics
            bet_result.calculate_accuracy()
            # Save BetResult object
            bet_result.save()

        self.stdout.write(self.style.SUCCESS('Results calculated and saved successfully'))
