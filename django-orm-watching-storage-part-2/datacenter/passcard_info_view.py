from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.timezone import localtime

from .storage_information_view import format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits_by_passcard = Visit.objects.filter(passcard=passcard)    
    this_passcard_visits = []
    
    for visit in visits_by_passcard:
        duration = Visit.get_duration(visit)
        is_strange = Visit.is_visit_long(visit)
        this_passcard_visits.append(
            {
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(duration),
                'is_strange': is_strange,
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
