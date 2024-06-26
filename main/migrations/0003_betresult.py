# Generated by Django 5.0.1 on 2024-05-11 12:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_country_flag'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BetResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_placement', models.IntegerField()),
                ('actual_placement', models.IntegerField()),
                ('bet_score', models.IntegerField()),
                ('actual_score', models.IntegerField()),
                ('accuracy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('correct_guess', models.BooleanField(default=False)),
                ('close_guess', models.BooleanField(default=False)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
