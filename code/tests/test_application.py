import pytest
import os, sys
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\application")
from app_helper import AppHelper 

appHelp = AppHelper()
adls_connect_obj = appHelp.connect_adls()

def test_adls_access():
    """
    Test that we have proper credentials to connect to ADLS.
    """
    all_dirs = adls_connect_obj.ls(".")
    # there must be a 'raw' directory in our lake
    check_dir = False
    if 'raw' in all_dirs:
        check_dir = True

    assert check_dir == True


def test_weather_api():
    """
    Test that we have proper credentials to connect to the weather API.
    """
    # check to see if we are able to successfully get one weather data point
    r = requests.get("http://api.openweathermap.org/data/2.5/group?id=5747882&appid=" + appHelp.weather_api_token)

    assert r.status_code < 300



