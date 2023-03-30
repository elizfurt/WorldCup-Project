# Assuming you have already imported the Result model and have a database connection 


# Create some users
jessie = CustomUser.objects.create_user(username='JessieErnster', password='password', email="jessieA@example.com")
lizzie = CustomUser.objects.create_user(username='LizzieFurtado', password='password', email="lizzieF@example.com")

# Create a tournament
tournament = Tournament.objects.create(tournament_name='Sample Tournament 2',start_date="2023-11-11", end_date="2023-12-12", active_status=True, is_public=True)

from userMgmt.models import CustomUser
from tournament.models import Tournament, Song, Resultz

# Create some songs
song_a = Song.objects.create(title='SongA', points=100)
song_b = Song.objects.create(title='SongB', points=90)
song_c = Song.objects.create(title='SongC',points=90)
song_d = Song.objects.create(title='SongD', points=120)
song_e = Song.objects.create(title='SongE', points=120)

# Create some results
result1 = Resultz.objects.create(user=jessie, tournament_song=song_a, points=100)
result2 = Resultz.objects.create(user=jessie, tournament_song=song_b, points=90)
result3 = Resultz.objects.create(user=lizzie, tournament_song=song_c, points=90)
result4 = Resultz.objects.create(user=lizzie, tournament_song=song_d, points=120)
result5 = Resultz.objects.create(user=jessie, tournament_song=song_e, points=120)


# Get existing users
jessie = CustomUser.objects.get(username='JessieA')
lizzie = CustomUser.objects.get(username='LizzieA')

# Create a tournament
tournament = Tournament.objects.create(tournament_name='Sample Tournament',
                                        start_date="2023-11-11",
                                        end_date="2023-12-12",
                                        active_status=True,
                                        is_public=True)


from userMgmt.models import CustomUser
from tournament.models import Tournament, Song, Resultz, Tournament_song

# Create some users
lizzie = CustomUser.objects.get(username='LizzieF')
jessie = CustomUser.objects.get(username='JessieE')

# Create a tournament
tournament = Tournament.objects.create(tournament_name='Sample Tournament 2',start_date="2023-11-11", end_date="2023-12-12", active_status=True, is_public=True)
tournament_songs = []

# Create a set of songs
all_songs = []

for i in range(8):
    song = Song.objects.create(title=f'Song{i}', artist=f'Artist{i}', spotify_ID=f'123456789{i}')
    print(f"Created song: {song}")
    all_songs.append(song)

tournament_song_points = [100,90,95,120,80]
users = [lizzie, jessie, jessie, lizzie, jessie]

# Add the tournament songs to the tournament 
for i, song in enumerate(all_songs[:5]):
    Tournament_song.objects.create(tournament=tournament, user=users[i]).song.set([song])
    tournament_songs.append(tournament_song)
    Resultz.objects.create(user=users[i], tournament_song=tournament_song, points=tournament_song_points[i]).save()