from django.db import models

from django.contrib.auth.models import models, User
# Create your models here.

class Player(models.Model):
    user_id = models.OneToOneField(User, null=True)


class Fighter(models.Model):
    name = models.CharField(max_length=255)


class Game(models.Model):
    name = models.CharField(max_length=255)


class Record(models.Model):
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    game = models.ForeignKey(Game)
    fighter_id = models.ForeignKey(Fighter)
    player_id = models.ForeignKey(Player)
