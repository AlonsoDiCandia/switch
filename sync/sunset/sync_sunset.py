import os, sys

current_path = os.path.abspath(os.path.dirname(__file__))
current_path = current_path[:current_path.find(os.path.dirname(__file__))]
sys.path.append(current_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "switch.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from backend.synchronizer.sunset.SunsetSynchronizer import SunsetSynchronizer
from backend.models.models import House

house = House.objects.get(name='Los Corregidores')
sync = SunsetSynchronizer(house)
print(sync.get_sunset_info())