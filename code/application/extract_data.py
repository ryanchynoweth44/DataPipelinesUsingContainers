import requests
import os, sys
import datetime
import time

while True:
    # reconfigure the app helper
    from app_helper import AppHelper
    appHelp = AppHelper()
    adls_connect_obj = appHelp.connect_adls()

    # set api query params
    city_ids = ['5747882', '5809844', '5799841', '5816449', '5812944', '5786882']
    city_batch = ",".join(city_ids)
    cities = ['Redmond, WA, USA','Seattle, WA, USA', 'Kirkland, WA, USA', 'Woodinville, WA, USA', 'Tacoma, WA, USA', 'Bellevue, WA, USA']

    # get request to get weather info
    r = requests.get("http://api.openweathermap.org/data/2.5/group?id=" + city_batch + "&appid=" + appHelp.weather_api_token)

    # format output path by date
    output_datetime = datetime.datetime.utcnow()
    data_output_path = "raw/weather_data/{}/{}/{}/{}/{}/weather_data.json".format(output_datetime.year, output_datetime.month, output_datetime.day, output_datetime.hour, output_datetime.minute)

    # write json file to adls
    appHelp.write_json_file(adls_connect_obj, data_output_path, r.content.decode('utf8'))

    # Open Weather Map gets new data about every 10 minutes. So we will sleep for 10. 
    time.sleep(600)
