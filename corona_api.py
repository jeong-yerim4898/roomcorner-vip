import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt_back.settings')

import django
django.setup()

import requests

from naver_movie.models import Corona

import json


api_key = 'ff61fc1d22cce0082e1bd91ebffb1e4b9'


corona_url = f'https://api.corona-19.kr/korea/country/new/?serviceKey={api_key}'
print(corona_url)
corona_response = requests.get(corona_url).json()
# print(corona_response['resultMessage'])
del(corona_response['resultMessage'])
del(corona_response['resultCode'])

# print(corona_response)


county_li = ['korea','seoul','busan','daegu','incheon','gwangju','daejeon','ulsan','sejong','gyeonggi','gangwon','chungbuk','chungnam','jeonbuk','jeonnam','gyeongbuk','gyeongnam','jeju']
for country in county_li:
    corona = Corona()
    corona.city = corona_response.get(country)['countryName']
    corona.corona_case = int(corona_response.get(country)['newCcase'])+int(corona_response.get(country)['newFcase'])
    corona.save()
    