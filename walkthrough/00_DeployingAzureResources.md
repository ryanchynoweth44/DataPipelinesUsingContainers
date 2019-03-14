# Deploy Azure Resources
In this section of the walkthrough we will deploy and configure the Azure resources required to deploy a python container for data extraction and landing in an Azure Data Lake Store. 

## Azure Data Lake Store
A Data Lake Store is an ideal storage for big data and predictive analytics. Past data warehousing strategies Extract Transform Load (ETL) workflow, however, as we move towards a big data strategy the ability to keep untouched raw data is curcial to avoid data loss or decrease in speed. Therefore, in data lakes we preach an Extract Land Transform (ELT) workflow. In this walkthrough we use an Azure Data Lake Store to land data as quickly as possible from the source system (weather api) to the data lake. 

1. [Create an Azure Data Lake Store.](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-get-started-portal#create-a-data-lake-storage-gen1-account)  

1. Once your data lake is create you will need to [create a service principle.](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) A service principle is esstentially a secure way to handle service accounts in Azure, and can be treated similarly to a regular user.   

1. Now that you have created a service principle you will need to give it access to your Azure Data Lake Store by following these [instructions.](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-secure-data#filepermissions) 
    - Check out access control rules [here.](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-access-control)  

## Azure Container Registry
Azure Container Registry allows you to store images for all types of containers. Containers make it easy for anyone to manage the configuration of apps isolated from the configuration of the hosting environment. We will use a container registry to store the images of our Docker containers. 

1. In the same resource group as your Azure Data Lake Store, [Create an Azure Container Registry.](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal)


Continue to the next portion of the walk through to [create a data extractor](./01_WritingDataExtractors.md) in a Docker Container.

