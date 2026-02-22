from datetime import timedelta
import os

import django
from django.utils.timezone import localtime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit

if __name__ == '__main__':
    passcards = Passcard.objects.all().count()
    print(f'Всего пропусков: {passcards}')
    active_passcards = Passcard.objects.filter(is_active=True).count()
    print(f'Активных пропусков: {active_passcards}')
        