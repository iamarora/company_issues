import csv

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from djangoapp.models import Companies


column_mapping = {
    'Company Name': 'name',
    'Animal Testing': 'animal_testing',
    'Nuclear Weapons': 'nuclear_weapons',
    'Coal Power': 'coal_power',
    'Rainforest Destruction': 'rainforest_destruction'
}
boolean_fields = ('animal_testing', 'nuclear_weapons', 'coal_power', 'rainforest_destruction', )

def create_super_user():
    try:
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    except IntegrityError:
        pass


class Command(BaseCommand):
    help = 'Load companies data'

    def handle(self, *args, **options):
        create_super_user()
        with open('data/company_exclusions.csv') as f:
            cr = csv.DictReader(f)
            for row in cr:
                ticker_symbol = row.pop('Ticker Symbol')
                data = {v: row.pop(k) for k, v in column_mapping.items()}
                data = {
                    k: True
                    if (k in boolean_fields and v.lower() == 'true') 
                    else False 
                    if (k in boolean_fields and v.lower() == 'false')
                    else v
                    for k,v in data.items()    
                }
                Companies.objects.update_or_create(ticker_symbol=ticker_symbol, defaults=data)
        print("Total companies = {}".format(Companies.objects.count()))