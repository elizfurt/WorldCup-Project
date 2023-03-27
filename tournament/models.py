##Tournament

from django.db import models
from django.db.models import fields
from userMgmt.models import CustomUser

class Tournament(models.Model):
    tournament_id = models.BigAutoField(auto_created = True,
                  primary_key = True,
                  serialize = False)
    tournament_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    active_status = models.BooleanField()
    is_public = models.BooleanField()

    def __str__(self):
        return self.tournament_id

class Song(models.Model):
    song_id = models.BigAutoField(auto_created = True,
                primary_key = True,
                serialize = False)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    spotify_ID = models.CharField(max_length=100)

    def __str__(self):
        return self.song_id

class Tournament_song(models.Model):
    tourament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    song = models.ManyToManyField(Song)
    tournament_song_id = models.BigAutoField(auto_created = True,
                         primary_key = True,
                         serialize = False)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.tournament_song_id

class Tournament_bracket(models.Model):
    tourmament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    bracket_id = models.BigAutoField(auto_created = True,
                        primary_key = True,
                        serialize = False)
    Is_final = models.BooleanField()

    def __str__(self):
        return self.bracket_id

class Tournament_user(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    user = models.ForeignKey('userMgmt.CustomUser', on_delete=models.SET('deleted_user'))
    tournament_user_id = models.BigAutoField(auto_created = True,
                         primary_key = True,
                         serialize = False)
    is_Creator = models.BooleanField()

class Vote(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    user = models.ForeignKey('userMgmt.CustomUser', on_delete=models.SET('deleted_user'))
    tournament_song_id = models.ForeignKey(Tournament_song, on_delete=models.CASCADE)
    vote_id = models.BigAutoField(auto_created = True,
              primary_key = True,
              serialize = False)

    def __str__(self):
        return self.vote_id

class Round(models.Model):
    round_id = models.BigAutoField(auto_created = True,
               primary_key = True,
               serialize = False)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    bracket_id = models.ForeignKey(Tournament_bracket, on_delete=models.CASCADE)
    round_number = models.IntegerField()
    deadline = models.DateField()

    def __str__(self):
        return self.round_id

class Bracket_song(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    bracket_id = models.ForeignKey(Tournament_bracket, on_delete=models.CASCADE)
    tournament_song_id = models.ForeignKey(Tournament_song, on_delete=models.CASCADE)
    rank = models.IntegerField()

class Round_vote(models.Model):
    round_vote_id = models.BigAutoField(auto_created = True,
               primary_key = True,
               serialize = False)
    round_id = models.ForeignKey(Round, on_delete=models.CASCADE)
    vote_id = models.ForeignKey(Vote, on_delete=models.CASCADE)

class Bracket_winner(models.Model):
    bracket_winner_id = models.BigAutoField(auto_created = True,
               primary_key = True,
               serialize = False)
    bracket_id = models.ForeignKey(Tournament_bracket, on_delete=models.CASCADE)
    tournament_song_id = models.ForeignKey(Tournament_song, on_delete=models.CASCADE)
    rank = models.IntegerField()
