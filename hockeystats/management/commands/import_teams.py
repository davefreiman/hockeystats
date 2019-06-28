from django.core.management.base import BaseCommand
import requests
from hockeystats.models import Team, Season, Person

class Command(BaseCommand):
    """NHL.com stats scraper"""
    help = 'imports teams info from NHL.com api based on existing seasons'

    def handle(self, *args, **kwargs):
        """
        imports teams info from NHL.com api based on existing seasons
        :param args:
        :param kwargs:
        :return:
        """
        endpoint = 'https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster&season='
        for season in Season.objects.all():
            response = requests.get(f'{endpoint}{season.year}')
            json = response.json()
            for team in json['teams']:
                try:
                    Team.objects.get(external_id=team['id'])
                except Team.DoesNotExist:
                    Team.objects.create(external_id=team['id'], name=team['name'])
                for person in team['roster']['roster']:
                    try:
                        Person.objects.get(external_id=person['person']['id'])
                    except Person.DoesNotExist:
                        Person.objects.create(external_id=person['person']['id'])
