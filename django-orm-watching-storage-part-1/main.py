from datetime import timedelta
import os

import django
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    visits = Visit.objects.all()
    for visit in visits:
        diff_time = localtime() - localtime(visit.entered_at)
        print(f'Зашел в хранилище,  время по Москве:\n{localtime(visit.entered_at)}\n'
              f'Находится в хранилище:\n{diff_time}\n')
    active_passcards = Passcard.objects.filter(is_active=True).count()
    print(f'Активных пропусков: {active_passcards}')
    # visits = Visit.objects.filter(leaved_at__isnull=True)
