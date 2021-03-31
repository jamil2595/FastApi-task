# FastApi-task

# Introduction:
The task is completed by the novel framework of Python - **FastAPI**. [FastAPI](https://fastapi.tiangolo.com/ ) is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It resembles the 3-tier architecture. The three tier architecture decouples presentation layer, business (application) layer and database layer. It is required to create a simple REST API for a catalog of products. The application should
contain:
* Product categories;
* Products which belong to some category (one product may belong to one category);

In my FastAPI app, main.py and schema.py represents presentation layer, crud.py represents business logic layer and model.py represents the database layer. I decided to choose many-to-many relationship between products and categories because products may belong to some other categories. Moreover, I covered many unit tests to test the roubstness of the application.This REST API contains endpoints that was asked in the requirements such as:
* Getting the list of all categories;
* Getting the list of products of the concrete category;
* Create/update/delete of category;
* Create/update/delete of product;



# Deployment

## Installation
Clone the repository to local

Enter to the directory

Following commands should be run to activate virtual environment and to get the needed packages. You may choose any virtual environment package for python. I decided to use [pipenv](https://pypi.org/project/pipenv/).

```console
pipenv shell
```
then

```console
pip3 install requirements.txt
```

## Run application
Following command runs the app: 
``` console 
uvicorn task.main:app --reload
```
## Testing

Tests are run via:
``` console 
pytest tests.py
```
If you run the tests, it will create empty test database and will pass the tests. Otherwise, it may use the existing database which may fail some tests due to the fact I manually hardwired the IDs'.

## Result

![Screenshot from 2021-03-31 19-21-35](https://user-images.githubusercontent.com/51953125/113177646-6c7e6e80-9256-11eb-91e6-918aee88eea4.png)
