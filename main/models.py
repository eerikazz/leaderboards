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
        total_countries = Country.objects.count()

        if self.bet_placement == self.actual_placement:
            self.correct_guess = True
            self.accuracy = 100.0
        else:
            difference = abs(self.actual_placement - self.bet_placement)
            max_difference = total_countries - 1  # Since placement starts from 1
            self.accuracy = ((max_difference - difference) / max_difference) * 100.0

            if self.accuracy > 0:
                self.close_guess = True

    def save(self, *args, **kwargs):
        self.calculate_accuracy()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.country}"
