# Deploy Data Extractor to Azure Container Instance
In Azure I recommend deploying to either Azure Kubernetes Service (AKS) or Azure Container Instance (ACI). These are the two container orchestration services in Azure and allow develoeprs to easily deploy to an environment without having to worry about maintaining infrastructure. 

Please download and install the [Azure Command Line Interface](https://docs.microsoft.com/cli/azure/install-azure-cli). We will be using the Azure CLI Tool to deploy our local image to Azure. Typically, this would be done with Azure DevOps Builds and Releases but we will do it manually to understand the tasks required for deployment. 

## Create a Dockerfile and Requirements File
1. In your application's root directory create a file named "Dockerfile". Please note that there is no file extension.  

1. Paste the following into your docker file. 
    ```
    FROM python:3.6


    RUN mkdir /src
    COPY . /src/
    WORKDIR /src
    RUN pip install -r requirements.txt
    RUN pip install .
    CMD [ "python", "./application/extract_data.py" ]
    ```

1. Next we want to create a "requirements.txt" file in the application root directory. This file is used to pip install all dependent python libraries. Paste the following:
    ```
    azure-mgmt-resource==1.2.2
    azure-mgmt-datalake-store==0.4.0
    azure-datalake-store==0.0.19
    configparser==3.5.0
    requests==2.20.0
    pytest==3.5.1
    ```


## Build Image and Run Container Locally
1. Open up a command prompt and navigate to the root of your extractor application. In my case, my applicaton root is in the [code](/code) folder.  

1.  Log in interactively to the Azure CLI by running the following:
    ```
    az login
    ```

1. Next we must build a container image. Run the following command:
    ```
    docker build ./Dockerfile -t demo-data-extractor
    ```

1. Use the following command to view the built image. 
    ```
    docker images
    ```

1. Next we will want to build and run the container locally.
    ```
    docker run -d -p 8080:80 demo-data-extractor
    ```

## Deploy Container to ACI

##### https://docs.microsoft.com/en-us/azure/container-instances/container-instances-tutorial-prepare-app#get-application-code

