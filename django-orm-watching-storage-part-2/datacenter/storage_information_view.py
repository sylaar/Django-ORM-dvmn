from datetime import timedelta

from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

from .models import Visit


def format_duration(duration):
    '''Returns duration without microseconds'''
    return timedelta(seconds=int(duration))


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at__isnull=True)

    for visit in visits:
        duration = Visit.get_duration(visit)
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(duration),
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
