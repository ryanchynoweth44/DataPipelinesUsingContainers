# Writing a Data Extractor in Python



## Create an application helper
As with all development you may have different classes or functions. Since this is a simply data extraction application we will create an `app_helper.py` class to make it easier for us to load environment variables or secrets, connect to azure data lake store, and write our data to the store. 


1. In your project's root directory create a folder called "application". This folder will container all the code that extracts data from source and land it in our data lake. 

1. In the "application" folder create `app_helper.py`. 

1. Paste the following requirements into the file. 
    ```python 
    import sys, os
    from azure.datalake.store import core, lib
    import json
    import configparser
    ```

1. Next we will create our class and `init` function. In this case the `init` function just loads the default environment variable values.  
    ```python
    class AppHelper(object):
    """
    This class is a helper class for the data extractor. It supplies function to extract data and write it to adls. 
    """

    def __init__(self, config_file=os.path.dirname(os.path.realpath(__file__)) + "\\app_config.conf", env="WeatherConfig"):
        self.weather_api_token = None
        self.azure_tenant_id = None
        self.adls_client_id = None
        self.adls_client_secret = None
        self.adls_resource = None
        self.adls_name = None
        self.set_config(config_file)
    ```

1. Next we will write a `set_config` function that loads information from our congig file to be used during our process. Paste the following code beneath the `init` function inside the class.   
    ```python
    def set_config(self, config_file,  env="WeatherConfig"):
        """
        Sets configuration variables for the application
        :param config_file: the path to the configuration file
        :param env: the environment string to parse in config file
        :return None
        """
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read(filenames = [config_file])
        ### Setting values here ###
        self.weather_api_token = config.get(env, "WEATHER_API_TOKEN")
        self.azure_tenant_id = config.get(env, "AZURE_TENANT_ID")
        self.adls_client_id = config.get(env, "ADLS_CLIENT_ID")
        self.adls_client_secret = config.get(env, "ADLS_CLIENT_SECRET")
        self.adls_name = config.get(env, "ADLS_NAME")
    ```
1. This is a great time to create our config file. My gitignore file ensures that my config file is not inside my repository, however, you will want to create a config file in `application\app_config.conf`. The config file has the following format: 
    ```
    [WeatherConfig]
    WEATHER_API_TOKEN = <Weather API Token>
    AZURE_TENANT_ID = <Tenant Id>
    AZURE_SUBSCRIPTION_ID = <Subscription Id>
    ADLS_CLIENT_ID = <Service Principle/Client Id>
    ADLS_CLIENT_SECRET = <Client Secret>
    ADLS_NAME = <Data Lake Name>
    ```
1. Finally we have helper functions for azure data lake store. Paste the following functions below the setup_config function.  
    ```python
    def connect_adls(self):
        """
        Creates a connection to Azure Data Lake Store
        """
        adls = None
        try:
            token = lib.auth(tenant_id=self.azure_tenant_id, 
                client_id=self.adls_client_id, 
                client_secret=self.adls_client_secret, 
                resource='https://datalake.azure.net/')

            adls = core.AzureDLFileSystem(token, store_name=self.adls_name)

        except Exception as ex:
            print("Unable to connect to Azure Data Lake! Error: %s" % (str(ex)))

        return adls

    def write_json_file(self, adls, output_path, data):
        """
        Writes json files to Azure Data Lake Store
        :param adls: Instance of ADLS
        :param output_path: the file path to write to in ADLS
        :param data: data to write in file. Data must be decoded using .decode('utf8').
        :return string saying if it successfully wrote data
        """
        try:
            with adls.open(output_path, 'ab') as outfile:
                outfile.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')).encode())
            return "Wrote to ADLS"
        except IOError as iex:
            print("ADL Write to File: Error while writing data to file on ADL " + str(iex))
            return "Unable to write to ADLS"
    ```

1. You now created your helper class!

## Create data extractor
Create a file called `application\extract_data.py`. The following code extracts data from our weather API, and writes it to your Azure Data Lake Store.  
```python
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

    # format output path by date raw/weather_data/yyyy/mm/dd/hh/mm
    output_datetime = datetime.datetime.utcnow()
    data_output_path = "raw/weather_data/{}/{}/{}/{}/{}/weather_data.json".format(output_datetime.year, output_datetime.month, output_datetime.day, output_datetime.hour, output_datetime.minute)

    # write json file to adls
    appHelp.write_json_file(adls_connect_obj, data_output_path, r.content.decode('utf8'))

    # Open Weather Map gets new data about every 10 minutes. So we will sleep for 10. 
    time.sleep(600)
```

You have created a data extractor! I would recommend running this script locally for manual testing purposes. It is set up to pull new weather data every 10 minutes.  