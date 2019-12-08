
from django.core.management.base import BaseCommand, CommandError
import datetime, csv
from sightings.models import Squirrel
from django.apps import apps


class Command(BaseCommand):
    help = 'exports files'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        with open(options['path'], 'w', newline='') as f:
            names = ['X',
                     'Y',
                     'Unique_Squirrel_ID',
                     'Shift',
                     'Date',
                     'Age',
                     'Primary_Fur_Color',
                     'Location',
                     'Specific_Location',
                     'Running',
                     'Chasing',
                     'Climbing',
                     'Eating',
                     'Foraging',
                     'Other_Activities',
                     'Kuks',
                     'Quaas',
                     'Moans',
                     'Tail_Flags',
                     'Tail_Twitches',
                     'Approaches',
                     'Indifferent',
                     'Runs_From']
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(names)
            for i in Squirrel.objects.all():
                writer.writerow([getattr(i, name) for name in names])
    print('Success!')
















































































