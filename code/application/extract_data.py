import requests
import os, sys
import datetime

#sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname('__file__'))) + '/code/application')
from app_helper import AppHelper


appHelp = AppHelper()
adls_connect_obj = appHelp.connect_adls()


city_ids = ['5747882', '5809844', '5799841', '5816449', '5812944', '5786882']
city_batch = ",".join(city_ids)
cities = ['Redmond, WA, USA','Seattle, WA, USA', 'Kirkland, WA, USA', 'Woodinville, WA, USA', 'Tacoma, WA, USA', 'Bellevue, WA, USA']

r = requests.get("http://api.openweathermap.org/data/2.5/group?id=" + city_batch + "&appid=" + appHelp.weather_api_token)

output_datetime = datetime.datetime.utcnow()
data_output_path = "raw/weather_data/{}/{}/{}/{}/{}".format(output_datetime.year, output_datetime.month, output_datetime.day, output_datetime.hour, output_datetime.minute)

appHelp.write_json_file(adls_connect_obj, data_output_path, r.content.decode('utf8'))

