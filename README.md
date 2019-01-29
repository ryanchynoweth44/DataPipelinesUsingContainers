# Create Data Pipelines Using Docker Containers
This repository shows an end to end implementation using containers to extract data, land it in an Azure Data Lake Store, and transform data. For this example, we will be extract data from the [Open Weather Map](https://openweathermap.org) website using their free APIs.  

## Prerequisites
 - [Azure Subscription](https://azure.microsoft.com/en-us/free/search/?&OCID=AID719825_SEM_KX8R84uR&lnkd=Bing_Azure_Brand&msclkid=6e706d7f2c60158ed7103168c2415255&dclid=CNmloKvCp98CFVJgwQodwMcKKQ)
    - You must have the Subscription Id, Tenant Id, and [create an service principal with a client secret](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal). 
 - [Open Weather Map Free Account](https://openweathermap.org/appid)
 - [Visual Studio Code](https://code.visualstudio.com/) or another IDE
 - Local installation of [Python](https://www.anaconda.com/download/)
 - Local installation of [Docker](https://docs.docker.com/install/)
 - Local installation of the [Azure CLI Tool](https://docs.microsoft.com/cli/azure/install-azure-cli)


## Running the project 
The main part of this repository is the containerized code have written to extract weather data. The code is located in the "[code](./code)" folder path of this repository. If you wish to run the code you will need to do the following:
1. Satisfy prerequisites above 
1. Create a configuration file to store your secrets. I ignore my config file in git so that the secrets stay local. Please save you config as `code\application\app_config.conf`. You config file should look like the following:
   ```
   [WeatherConfig]
   WEATHER_API_TOKEN = <Weather API Token>
   AZURE_TENANT_ID = <Tenant Id>
   AZURE_SUBSCRIPTION_ID = <Subscription Id>
   ADLS_CLIENT_ID = <Service Principle/Client Id>
   ADLS_CLIENT_SECRET = <Client Secret>
   ADLS_NAME = <Data Lake Name>
   ``` 
1. Create docker image locally
1. Run docker image

## Blog
Check out the [blog](./blog/ContainersAndDataPipelines.md) about why python and containers are a great way to implement the data extraction for you data pipelines!


## Walkthrough
Please complete the following in order for an end to end implementation:  
1. [Deploy Resources](walkthrough/00_DeployingAzureResources.md)
1. [Create Data extractor](walkthrough/01_WritingDataExtractors.md)
1. [Deploy to Azure Container Instance](walkthrough/02_DeployToACI.md)


## Conclusion
If there are any confusing steps or errors please let me know. Any other comments or questions you can contact me at rchynoweth@10thmagnitude.com. 

Coming soon is another repository the shows basic devops (AI/Data Ops) workflows for data containers! Containers are an excellent and easy way deploy your data pipelines, and allow developers to simply augment their workflow instead of a complete change.  