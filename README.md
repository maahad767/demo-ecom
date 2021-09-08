# Welcome to Simple E-Commerce System
## Requirements
Python: >=3.5(recommended: 3.8)

Django: 3.2

## Installation

### Clone the repository
`git-clone https://github.com/maahad767/demo-ecom.git`

### Create & Activate Virtual Environment
Create virtual environment for the project. You can follow bellow instructions to install, create and activate virtual environment.

For Linux: <br>
<code>
pip install virtualenv <br>
  
virtualenv .env <br>
  
source .env/bin/activate
</code>

For Windows(powershell): <br>
<code>
pip install virtualenv <br>
  
virtualenv .env <br>

source .env/Scripts/Activate.ps1
</code>


For Windows(Command Prompt, run as Administrator): <br>
<code>
pip install virtualenv <br>
  
virtualenv .env <br>
  
source .env/Scripts/activate
</code>

### Install dependencies
`pip install -r requirements.txt`

### Run Project
If you get errors related to python versions, please consider using python3 instead of python.

<code>
python manage.py migrate <br>
  
python manage.py runserver
</code>

It will run the server in localhost:8000 / 127.0.0.1:8000. If you want to change the localhost ip or port use the runserver command in the following format: 

`python manage.py runserver ip port`

## Documentation
For detailed documentation of the API please visit 
[Simple E-commerce Documentation hosted by Postman](https://documenter.getpostman.com/view/14449101/U16hsmTs)
