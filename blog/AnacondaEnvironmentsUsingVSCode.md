# Using Anaconda Environments with Visual Studio Code

My Python distribution of choice is [Anaconda]() and I love working in different conda environments to avoid dependency conflicts and start fresh with new predictive solutions. Over the last year and a half I have slowly made a transition from R to Python as my preferred data science language, and when I first started out in Python I used [Jupyter Notebooks](). While I am still a huge fan of the notebook development style, I now primarily use a scripting IDE like [Visual Studio Code]() (VS Code) for all my Python development. One thing that I initially found difficult with VS Code is the ability to create a conda environment and use it as my python interpreter. 

The ability to do this is somewhat well documented and easy to do, however, I had to piece together a few different sources to find out. As a reference I am using a Windows 10 Microsoft Surface Laptop for my local development. 


1. To set up your development environment please make sure that you have both Anaconda and Visual Studio Code installed on your machine. 

1. Once installed, please open an anaconda command prompt. The following command creates a new conda environment with python 3.6. 
    ```
    conda create -n myenv python=3.6
    ```

1. To activate that new environment run: 
    ```
    conda activate myenv
    ```

    If I want to pip install or conda install any libraries in my new environment I will typically use the anaconda command prompt to do so. 

1. Next we would like to use this new conda environment as our python interpreter in VS Code. 


