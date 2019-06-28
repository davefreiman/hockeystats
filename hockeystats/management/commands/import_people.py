from django.core.management.base import BaseCommand
import requests
from hockeystats.models import Team, Season, Person

class Command(BaseCommand):
    """NHL.com stats scraper"""
    help = 'imports players info from NHL.com api'

    def handle(self, *args, **kwargs):
        """
        imports teams info from NHL.com api based on existing seasons
        :param args:
        :param kwargs:
        :return:
        """
        endpoint = 'https://statsapi.web.nhl.com/api/v1/people/'
        for person in Person.objects.all():
            response = requests.get(f'{endpoint}{person.external_id}')
            json = response.json()
            person_data = json['people'][0]
            person.first_name = person_data['firstName']
            person.last_name = person_data['lastName']
            person.birth_year, person.birth_month, person.birth_day = [
                int(num) for num in person_data['birthDate'].split('-')
            ]
            person.home_town = person_data['birthCity']
            person.home_region = person_data.get('birthStateProvince')
            person.home_country = person_data['birthCountry']
            person.shoots = person_data.get('shootsCatches')
            person.primary_position = person_data['primaryPosition']['abbreviation']
            person.save()
