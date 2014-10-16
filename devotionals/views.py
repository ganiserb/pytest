from django.shortcuts import render
from devotionals.models import Devotional
from datetime import date


def show_devotional(request, year, month, day):
    date_provided = date(int(year), int(month), int(day))
    devotional = Devotional.objects.get(date=date_provided)
    return render(request,
                  'devotionals/show_devotional.html',
                  {'devotional': devotional})
