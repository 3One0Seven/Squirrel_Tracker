
from django.core.management.base import BaseCommand, CommandError
import datetime, csv
from squdata.models import Squirreldata
from django.apps import apps


class Command(BaseCommand):
    help = 'exports all information to csv files'

    def add_arguments(self, parser):
        parser.add_argument('website_path', type=str)

    def handle(self, *args, **options):
        with open(options['website_path'], 'w', newline='') as csvfile:
            names = ['latitude',
                     'longitude', 
                     'unique_squirrel_id',
                     'shift',
                     'date',
                     'age',
                     'fur_color',
                     'location',
                     'specific_location',
                     'running',
                     'chasing',
                     'climbing',
                     'eating',
                     'foraging',
                     'other_activities',
                     'kuks',
                     'quaas',
                     'moans',
                     'tail_flags',
                     'tail_twitches',
                     'approaches',
                     'indifferent',
                     'runs_from']
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(names)
            for i in Squirreldata.objects.all():
                writer.writerow([getattr(i, name) for name in names])
















































































