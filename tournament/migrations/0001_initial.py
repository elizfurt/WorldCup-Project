# Generated by Django 4.1.7 on 2023-03-29 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bracket_song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rank", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Bracket_winner",
            fields=[
                (
                    "bracket_winner_id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("rank", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Resultz",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Round",
            fields=[
                (
                    "round_id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("round_number", models.IntegerField()),
                ("deadline", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Round_vote",
            fields=[
                (
                    "round_vote_id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "song_id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("artist", models.CharField(max_length=100)),
                ("spotify_ID", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Tournament",
            fields=[
                (
                    "tournament_id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("tournament_name", models.CharField(max_length=50)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("active_status", models.BooleanField()),
                ("is_public", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Tournament_bracket",
            fields=[
                (
                    "bracket_id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("Is_final", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Tournament_song",
            fields=[
                (
                    "tournament_song_id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("points", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Tournament_user",
            fields=[
                (
                    "tournament_user_id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("is_Creator", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                (
                    "vote_id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tournament.tournament",
                    ),
                ),
                (
                    "tournament_song_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tournament.tournament_song",
                    ),
                ),
            ],
        ),
    ]
