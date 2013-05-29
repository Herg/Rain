

import pprint
import urllib2
import json
import sys

DEFAULT_LAT = '37.76323'
DEFAULT_LONG = '-122.423187'
DEFAULT_UNITS = 'auto'

class forecast_service(object):

    def __init__(self, lat = DEFAULT_LAT, long = DEFAULT_LONG):
        self.lat = lat
        self.long = long
        self.base_url = 'https://api.forecast.io/forecast/ccf49b956bef54467829baac11bc1bc1/'


    def get_daily_forecast(self, lat = None, long = None):
        if lat is not None:
            self.lat = lat
        if long is not None:
            self.long = long
        url = '%s%s,%s?units=%s' % (self.base_url, self.lat, self.long, DEFAULT_UNITS)
        try:
            data = json.load(urllib2.urlopen(url))
            daily_data = data['daily']['data']
        except:
            return None
        forecast = []
        for day in daily_data:
            day_data = {}
            day_data['time'] = day['time']
            day_data['temp_max'] = day['temperatureMax']
            day_data['temp_mix'] = day['temperatureMin']
            day_data['summary'] = day['summary']
            if day['precipIntensity'] > 0.0 and 'precipType' in day:
                day_data['precip_type'] = day['precipType']
                if day['precipIntensity'] < 0.17:
                    day_data['precip_intensity'] = 'sprinkling'
                elif day['precipIntensity'] < 0.1:
                    day_data['precip_intensity'] = 'light'
                elif day['precipIntesity'] < 0.4:
                    day_data['precip_intensity'] = 'moderate'
                else:
                    day_data['precip_intensity'] = 'heavy'
            forecast.append(day_data)
        return { 'data' : forecast }


fs = forecast_service()
w = fs.get_daily_forecast()
pprint.pprint(w)
