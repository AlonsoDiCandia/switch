import json
import requests
from datetime import datetime, timedelta

class SunsetSynchronizer():
    def __init__(self, house):
        self.house = house
        self.time_now = datetime.now()
        self.date = self.time_now.strftime('%Y-%m-%d')

    def get_sunset_info(self):
        url = f'https://api.sunrise-sunset.org/json?lat={self.house.latitude}&lng={self.house.longitude}&date={self.date}&formatted=0'
        response = requests.get(url)
        body = response.json()
        sunset = datetime.strptime(body['results']['sunset'], '%Y-%m-%dT%H:%M:%S+00:00') + timedelta(hours=-3)

        data = {}
        data['date'] = self.date
        data['sunset'] = sunset

        return data 