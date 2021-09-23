import csv
from models import Hero

with open('../../superhero_dataset_full/test.csv', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Hero.objects.get_or_create(
                name=row[1],
                alias=row[0],
                )
            # creates a tuple of the new object or
            # current object and a boolean of if it was created
