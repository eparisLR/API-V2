from  django.core.management.base import BaseCommand
from heroapi.models import Creator, Hero, Superpowers
import csv

class Command(BaseCommand):
    def handle(self, **options):
        print("Importing data..")
        superpowers_name= []
        with open("superhero_dataset_full/test.csv") as f:
            items = [{k: v for k, v in row.items()}
                            for row in csv.DictReader(f, skipinitialspace=True)]
            creator = Creator(1, "DC Comics")
            creator.save()
            print(f"{creator.name} created !")
                
            creator = Creator(2, "Marvel")
            creator.save()
            print(f"{creator.name} created !")

            for item in items:
                hero_params = {
                    "name": item['name'],
                    "alias": item['real_name']
                }
                hero = Hero(**hero_params)
                hero.save()
                print(f"{hero.name} created !")

                for i in item: 
                    if 'has' in i:
                        superpowers_name.append(i)

            iterator=1
            for superpower in superpowers_name:
                superpower_to_create = Superpowers(iterator, superpower)
                superpower_to_create.save()
                print(f"{superpower_to_create.name} created !")
                iterator = iterator + 1

                

