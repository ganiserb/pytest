# coding=utf-8
__author__ = 'gabriel'

from django.core.management.base import BaseCommand
from devotionals.models import Devotional
from datetime import date
import csv


class Command(BaseCommand):
    args = 'path_to_csv'
    help = 'Imports the given devotionals CSV to the ' \
           'database (title, month, day, body)'

    def handle(self, *args, **options):
        # self.stdout.write(args[0])
        with open(args[0], 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, skipinitialspace=True)
            next(reader)
            for line in reader:
                # day and month are in the wrong order in the CSV
                title, day, month, body = line


                Devotional.objects.get_or_create(title=title,
                                                 date=date(date.today().year,
                                                           int(month),
                                                           int(day)),
                                                 body=body)