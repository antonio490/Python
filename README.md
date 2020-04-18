
# Python help

## Import/Export requirements

1. Requirements.txt

Export pip libraries into a requirements.txt

    $ pip freeze > requirements.txt

Import and install pip libraries from requirements.txt 

    $ pip install -r requirements.txt


## Create an environment

1. Create an environment using a text file:

    
        $ conda env create --<env_name> --<file>

2. List all the environments:

    
        $ conda env list

3. Activate and log in into an environment:

    
        $ source activate <env_name>

4. Create an environment from zero:

    
        $ virtualenv <env_name>

        $ source activate <env_name>

        (env_name) antonio bin $ pip install <pkg_name>