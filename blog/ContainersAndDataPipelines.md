# Power Data Analytics with Containers

Implementing scalable and managable data solutions in the cloud can be difficult. Organizations must develop a strategy that not only succeeds technically but fits with the team's persona. There are a number of Platform as a Service (PaaS) products and Software as a Service (SaaS) products that make it easy to connect to, transform, and move data throughout your organization. However, the surplus of tools can make it difficult to figure out which ones to use and at times engineers don't want to learn or use an entirely different tool. Many of the engineers I work with love working with data using functional languages like Python, however, have a slight barrier when moving from their local desktop to the cloud. When engineers prefer more custom development I recommend implementing their data pipelines, in particular their data extractors, using Python and Docker Containers. 

## Creating Data Pipeline Containers 
Data pipelines always begin with data extraction. Then depending on the business requirements, the developer will transform and manipulate that data to solve a business need, or simply migrate that data to a raw and aggregated data store i.e data lakes. Below is a general flow diagram of data pipelines where the transformations can be as complicated as machine learning models, or as simple as normalizing the data. In this scenario each intermediate pipe could be a container, or the entire data pipeline could be a single container. This flexibility is left up to the developer.  

![](./imgs/GeneralDataPipeline.png)

Most engineers are familiar with local IDE development using notebooks (like [Jupyter notebooks](https://jupyter.org/)) or a code editor (like [VS Code](https://code.visualstudio.com/)). Therefore, when a new data source is determined, engineers should simply start developing locally and iterate over their solution in order to package it up as a container. If the engineer is using Python to extract data, they will need to track all dependencies in a `requirements.txt` file, and make note of any special installations (like sql drivers) required to extract data and write it to a raw data lake store. Once the intial development is completed the engineer will then need to get their code ready for deployment!

## Deploying Data Pipeline Containers
Before deploying a container there are a few things that the engineer will do before it is ready.  
1. Create a `requirements.txt` file in the solution's root directory
1. Create a `Dockerfile` file in the solution's root directory
1. Make sure the data extractor is in an "application" folder off the root directory
1. Write automated tests using the popular [pytest](https://pypi.org/project/pytest/) python package 
    - this is not required but I would recommend it for automated testing
1. Build an image locally
1. Build and run the container locally for testing
1. Deploy to Azure Container Instance (or Azure Kubernetes Service)  


Here is an example `requirements.txt` file:  
```
azure-mgmt-resource==1.2.2
azure-mgmt-datalake-store==0.4.0
azure-datalake-store==0.0.19
configparser==3.5.0
requests==2.20.0
pytest==3.5.1
```


Here is an example `Dockerfile` file that starts with a python3.6 image, copies are application into the working directory, and runs our data extraction. In this case we have a python script, "dataextractor.py", in a folder called "application":   
```
FROM python:3.6

RUN mkdir /src
COPY . /src/
WORKDIR /src
RUN pip install -r requirements.txt
RUN pip install .
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


Now that you have deployed the container manually to Azure Container Instance, it is important to manage this applications. Often times data extractors will be on a scheduled basis and won't be running 100% of the time. Therefore, it is usually a good idea to only have the contianer running when you need it to. Keep reading to learn how to manage containes at a high-level.  

## Managing Data Pipeline Containers

With all data solutions I recommend a centralized enterprise scheduler. One way that I implement this scheduler is using an [Azure Function](https://docs.microsoft.com/en-us/azure/azure-functions/) (or another Python Docker Container) with [Azure Table Storage](https://azure.microsoft.com/en-us/services/storage/tables/). The Azure Function reads data from table storage and triggers a container execution. The table storage tracks:  
- Job schedules (i.e. every 2 hours)  
- The last execution of the job
- The current status of the job
- Watermark (saves where we left off for incremental data pulls)

Often times companies will use a similar process to track all history the each run in order to see how the solution is operating over time. For example, tracking run duration enables an organization to view the length of each run and understand if the process needs editing based on performance.  

Often times organizations will want to have the scheduling logic in the Python code itself, however, I would caution against this as it is difficult to get a high level view and understanding of your solution when the scheduling and status of each job is separated. A centralized job scheduler allows engineers to easily monitor the solution and understand which jobs are failing and which are succeeding. 

## Conclusion
Developing data solutions using containers is an excellent way to manage, orchestrate, and develop a scalable analytics and artificial intelligence application. This [walkthrough](../walkthrough/01_WritingDataExtractors.md) walks engineers through the process of creating a weather data source extractor, wrap it up as a container, and deploy the container both locally and in the cloud. 





