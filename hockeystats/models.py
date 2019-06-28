from django.db import models

POSITIONS = (
    ('RW', 'RW'),
    ('LW', 'LW'),
    ('C', 'C'),
    ('D', 'D'),
    ('G', 'G')
)

class Person(models.Model):
    """A Person!"""
    external_id = models.CharField(max_length=50, db_index=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    home_town = models.CharField(max_length=100, null=True)
    home_region = models.CharField(max_length=100, null=True)
    home_country = models.CharField(max_length=100, null=True)
    home_latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    home_longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    birth_day = models.IntegerField(null=True)
    birth_month = models.IntegerField(null=True)
    birth_year = models.IntegerField(null=True)
    shoots = models.CharField(max_length=2, choices=(('R', 'R'), ('L', 'L')), null=True)
    primary_position = models.CharField(max_length=2, choices=POSITIONS, null=True)


class Season(models.Model):
    """A season!"""
    year = models.CharField(max_length=8)


class Team(models.Model):
    """A Team!"""
    name = models.CharField(max_length=255)
    external_id = models.IntegerField(db_index=True)


class StatLine(models.Model):
    """A statline for a given season, team, and player"""

    class Meta:
        """Model metadata"""
        indexes = [
            models.Index(fields=['person', 'team', 'season'])
        ]

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    games = models.IntegerField(null=True)
    goals = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    pim = models.IntegerField(null=True)
    shots = models.IntegerField(null=True)
    hits = models.IntegerField(null=True)
    pp_goals = models.IntegerField(null=True)
    pp_assists = models.IntegerField(null=True)
    pp_toi = models.IntegerField(null=True)
    ev_toi = models.IntegerField(null=True)
    faceoff_pct = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    shooting_pct = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    gw_goals = models.IntegerField(null=True)
    ot_goals = models.IntegerField(null=True)
    sh_goals = models.IntegerField(null=True)
    sh_points = models.IntegerField(null=True)
    sh_toi = models.IntegerField(null=True)
    blocks = models.IntegerField(null=True)
    plus_minus = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    shifts = models.IntegerField(null=True)



