from  django.core.management.base import BaseCommand
from heroapi.models import Hero
import csv

class Command(BaseCommand):
    def handle(self, **options):
        print("Importing data..")
        with open("superhero_dataset_full/test.csv") as f:
            herolist = [{k: v for k, v in row.items()}
                            for row in csv.DictReader(f, skipinitialspace=True)]
            for item in herolist:
                hero_params = {
                    "name": item['name'],
                    "alias": item['real_name']
                }
                hero = Hero(**hero_params)
                hero.save()
                print(f"{hero.name} created !")