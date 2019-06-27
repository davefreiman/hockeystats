from django.core.management.base import BaseCommand
from selenium import webdriver


class Command(BaseCommand):
    """NHL.com stats scraper"""
    help = 'pulls in stats from NHL.com and saves them locally'

    def __init__(self):
        self._keys = []
        super().__init__()

    def __build_record(self, elements):
        """
        Transforms a series of selenium elements into a dict
        :param elements: list
        :return: dict
        """
        player = {}
        for index, element in enumerate(elements):
            player[self._keys[index]] = element.text
        print(player)
        return player

    def handle(self, *args, **kwargs):
        """
        entrypoint for scraper command
        :param args:
        :param kwargs:
        :return:
        """
        driver = webdriver.Firefox()
        driver.get('http://www.nhl.com/stats/player?report=skaterpercentages&reportType=season&seasonFrom=20182019&seasonTo=20182019&gameType=2&position=D&filter=gamesPlayed,gte,30&sort=shotAttemptsPctg')
        try:
            elements = driver.find_elements_by_css_selector('.rt-tr')
            for index, element in enumerate(elements):
                if index == 0:
                    subs = element.find_elements_by_css_selector('.rt-th')
                    self._keys = [sub.text for sub in subs]
                else:
                    subs = element.find_elements_by_css_selector('.rt-td')
                    self.__build_record(subs)

        finally:
            driver.quit()
