from celery import shared_task
from Task1 import settings
from django.conf import settings 
from django.contrib.auth.models import User
from .models import *
from datetime import date
import datetime
import holidays
import requests
import json
from requests import get
 

@shared_task(bind=True)
def helper(self,uuid):
    print("shubham")
    ip_address = get('https://api.ipify.org').text 
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    countryy = result['country_code']
    # date = datetime.datetime.now().date()
    date = datetime.date(2021, 1, 14)
    yearr = int(date.strftime('%Y'))
    dateList = holidays.CountryHoliday(countryy, years=yearr)
    if date in dateList:
        # import pdb;pdb.set_trace()
        instance = UserCountryHolidayInfo()
        instance.geolocation_info = result,
        instance.holidays_info = dateList
        instance.user_uuid = User.objects.get(uuid = uuid)
        instance.save()
    return "done"

