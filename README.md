# Create Data Pipelines Using Docker Containers --- UNDER DEVELOPMENT
This repository shows an end to end implementation using containers to extract data, land it in an Azure Data Lake Store, and transform data. For this example, we will be extract data from the [Open Weather Map](https://openweathermap.org) website using their free APIs.  

## Prerequisites
 - [Azure Subscription](https://azure.microsoft.com/en-us/free/search/?&OCID=AID719825_SEM_KX8R84uR&lnkd=Bing_Azure_Brand&msclkid=6e706d7f2c60158ed7103168c2415255&dclid=CNmloKvCp98CFVJgwQodwMcKKQ)
    - You must have the subscription's Tenant Id, and [create an service principal with a client secret](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal). 
 - [Open Weather Map Free Account](https://openweathermap.org/appid)
 - Basic knowledge and local installation of [Python](https://www.anaconda.com/download/)
 - Python IDE. I use [Visual Studio Code]()
 - Basic knowledge and local installation of [Docker](https://docs.docker.com/install/)


## Running the project 
The main part of this repository is the containerized code have written to extract weather data. The code is located in the "[code](./code)" folder path of this repository. If you wish to run the code you will need to do the following:
1. Satisfy prerequisites
1. Supply values in the [configuration file](code/application/app_config.conf). 
1. Create docker image locally
1. Run docker image

## Blog
Check out the [blog](./blog/ContainersAndDataPipelines.md) about why python and containers are a great way to implement the data extraction for you data pipelines!


## Walkthrough
Please complete the following in order for an end to end implementation:  
1. Create Helper Library
1. Create Data extractor
1. Create PyTests
1. Set up CI/CD Pipelines in [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/)


## Conclusion
If there are any confusing steps or errors please let me know. Any other comments or questions you can contact me at rchynoweth@10thmagnitude.com. 