from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    flag = models.FileField(upload_to='flags/')
    hero = models.ImageField(upload_to='heros/')
    country = models.CharField(max_length=256)
    song = models.CharField(max_length=512)
    placement = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return self.country
    
class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    bet_placement = models.IntegerField()
    bet_score = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.country}"

class BetResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    bet_placement = models.IntegerField()
    actual_placement = models.IntegerField()
    bet_score = models.IntegerField()
    actual_score = models.IntegerField()
    accuracy = models.DecimalField(max_digits=5, decimal_places=2)
    correct_guess = models.BooleanField(default=False)
    close_guess = models.BooleanField(default=False)

    def calculate_accuracy(self):
        total_bets = Bet.objects.filter(user=self.user).count()
        correct_bets = Bet.objects.filter(
            user=self.user,
            country=self.country,
            bet_placement=self.actual_placement
        ).count()

        if total_bets == 0:
            self.accuracy = 0.0
        else:
            self.accuracy = (correct_bets / total_bets) * 100.0


    def save(self, *args, **kwargs):
        # Override save method to automatically calculate accuracy before saving
        self.calculate_accuracy()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.country}"
