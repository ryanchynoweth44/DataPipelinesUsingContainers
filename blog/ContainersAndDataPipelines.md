# Data Analytics, Data Engineering, and Containers

Implementing scalable and managable data solutions in the cloud can be difficult. Organizations need to develop a strategy that not only succeeds technically but fits with their team's persona. There are a number of Platform as a Service (PaaS) products and Software as a Service (SaaS) products that make it easy to connect to, transform, and move data in your network. However, the surplus of tools can make it difficult to figure out which ones to use, and often they tools can only do a fraction of what an engineer can do with scripting language. Many of the engineers I work with love functionaly languages when working with data. My preffered data language is Python, however, there can be a barrier when moving from a local desktop to the cloud. When developing data pipelines using a language like Python I recommend using Docker Containers.  

Historically, it is not a simple task to deploy code to different environments and have it run reliably. This issue arises most when a data scientist or data engineer is moving code from local development to a test or production environment. Containers consist of their own runtime environment and contain all the required dependencies, therefore, it eliminates variable environments at deployment. Containers make it easy to develop in the same environment as production and eliminate a lot of risk when deploying.  

## Creating Data Pipeline Containers 
My preferred Python distribution is [Anaconda](https://www.anaconda.com/) because of how easy it is to create an use different virtual environments, allowing me to insure that there are no python or dependency conflicts when working on different solutions. Virtual environments are extremely popular with python developers, therefore, the transition deploying using containers should be familiar. If you are unfamiliar with anaconda virtual environments check out this separate [blog post](https://ryansdataspot.com/2019/02/14/anaconda-environments-in-visual-studio-code/) where I talk about best practices and how to use these environments when working with Visual Studio Code.  

Data pipelines always start with data extractions. Best practices the engineer should land their raw data into a data store as quickly as possible. The raw data gives organizations a source of data that is untouched, allowing a developer to reprocess data as needed to solve different business problems. Once in the raw data store the developer will transform and manipulate data as needed. In Azure, my favorite data store to handle raw, transformed, and business data is the Azure Data Lake Store. Below is a general flow diagram of data pipelines where the transformations can be as complicated as machine learning models, or as simple as normalizing the data. In this scenario each intermediate pipe could be a container, or the entire data pipeline could be a single container. At each pipeline the data may be read a data source source or chained from a previous tranform. This flexibility is left up to the developer. Containers make versioning and deploying data applications easy because they allow an engineer to develop how they prefer, and quickly deploy with a few configuration steps and commands. 

![](./imgs/GeneralDataPipeline.png)

Most engineers prefer to develop locally on their laptops using notebooks (like [Jupyter notebooks](https://jupyter.org/)) or a code editor (like [Visual Studio Code](https://code.visualstudio.com/)). Therefore, when a new data source is determined, engineers should simply start developing locally using an Anaconda environment and iterate over their solution in order to package it up as a container. If the engineer is using Python to extract data, they will need to track all dependencies in a `requirements.txt` file, and make note of any special installations (like sql drivers) required to extract data and write it to a raw data lake store. Once the intial development is completed the engineer will then need to get their code ready for deployment! This workflow is ideal for small to medium size data sources because the velocity of true big data can often be an issue for batch data extraction, and a streaming data solution is preferred (i.e. Apache Spark). 

## Deploying Data Pipeline Containers
To set the stage, you are a developer and you have written a python data extraction application using a virtual environment on your machine. Since you started with a fresh python interpretter and added requirements you have compiled a list of the installed libraries, drivers, and other dependencies as need to solve their problem. How does a developer get from running the extraction on a local machine to the cloud? 

First we will create and run a docker container locally for testing purposes. Then we will deploy the container to Azure Container Instance, the fastest and simplest way to run a container in Azure. Data extractors that are deployed as containers are usually batch jobs that the developers wants to run on a specific cadence. There are two ways to acheive this CRON scheduling: have the application "sleep" after each data extraction, or have a centralized enterprise scheduler that kicks off the process as needed. I recommend the latter because it allows for a central location to monitor all data pipeline jobs, and avoids having to redeploy or make code changes if the developers wishes to change the schedule.  

Before deploying a Docker container there are a few things that the engineer will do before it is ready.  
1. Create a `requirements.txt` file in the solution's root directory
1. Create a `Dockerfile` file in the solution's root directory
1. Make sure the data extractor is in an "application" folder off the root directory
1. Write automated tests using the popular [pytest](https://pypi.org/project/pytest/) python package 
    - this is not required but I would recommend it for automated testing. I do not include this in my walk through that is provided. 
1. Build an image locally
1. Build and run the container locally for testing
1. Deploy to Azure Container Instance (or Azure Kubernetes Service)  


Here is an example `requirements.txt` file for the sample application available [here](/code/requirements.txt):  
```
azure-mgmt-resource==1.2.2
azure-mgmt-datalake-store==0.4.0
azure-datalake-store==0.0.19
configparser==3.5.0
requests==2.20.0
pytest==3.5.1
```


Here is an example `Dockerfile` file that starts with a python 3.6 image, copies are application into the working directory, and runs our data extraction. In this case we have a python script, "dataextractor.py", in a folder called "application":   
```
FROM python:3.6

RUN mkdir /src
COPY . /src/
WORKDIR /src
RUN pip install -r requirements.txt
CMD [ "python", "./application/dataextractor.py" ]
```

To build an image locally you will need Docker installed. If you do not have it installed please download it [here](https://www.docker.com/get-started), otherwise, make sure that docker is currently running on your machine. Open up a command prompt, navigate to your projects root directory, and run the following commands:  
```python
## Build an image from the current directory
docker build -t my-image-name .

## Run the container using the newly created image
docker run my-image-name

```

To deploy the container to Azure Container Instance, you first must create an Azure Container Registry and [push your container to the registry](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-acr). Next you will need to deploy that image to [Azure Container Instance using the Azure CLI](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-deploy-app). Note that the Azure CLI tool can be used to automate these deployments in the future, or an engineer can take advantage of Azure DevOps Build and Release tasks. 

Now that you have deployed the container manually to Azure Container Instance, it is important to manage these applications. Often times data extractors will be on a scheduled basis, therfore, will likely require external triggers to extract and monitor data pipelines. Stay tuned for a future blog on how to managed your data containers!

## Conclusion
Developing data solutions using containers is an excellent way to manage, orchestrate, and develop a scalable analytics and artificial intelligence application. This [walkthrough](https://github.com/ryanchynoweth44/DataPipelinesUsingContainers/blob/master/walkthrough/00_DeployingAzureResources.md) walks engineers through the process of creating a weather data source extractor, wrap it up as a container, and deploy the container both locally and in the cloud. 





