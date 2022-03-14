# SIMPLE CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.8.12
- Django 4.0.3
- Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `recipes`, so we will use the following URLS - `/recipes/` and `/recipes/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`recipes` | GET | READ | Get all recipes
`recipes/:id` | GET | READ | Get a single recipe
`recipes`| POST | CREATE | Create a new recipe
`recipes/:id` | PUT | UPDATE | Update a recipe
`recipes/:id` | DELETE | DELETE | Delete a recipe

## Use
We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation), or we can use [Postman](https://www.postman.com/)

Httpie is a user-friendly http client that's written in Python. Let's try and install that.

You can install httpie using pip:
```
pip install httpie
```

First, we have to start up Django's development server.
```
python manage.py runserver
```
Only authenticated users can use the API services, for that reason if we try this:
```
http  http://127.0.0.1:8000/api/recipes/
```
we get:
```
{
    "detail": "Authentication credentials were not provided."
}
```
Instead, if we try to access with credentials:
```
http http://127.0.0.1:8000/api/recipes/5 
```
we get the recipe with id = 5
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "recipe_id": 5,
    "recipe_name": "Apple Pie",
    "ingredients": "1 recipe pastry for a 9 inch double crust pie\r\n½ cup unsalted butter\r\n3 tablespoons all-purpose flour\r\n¼ cup water\r\n½ cup white sugar\r\n½ cup packed brown sugar",
    "instructions": "Step 1\r\nPreheat oven to 425 degrees F (220 degrees C). Melt the butter in a saucepan. Stir in flour to form a paste. Add water, white sugar and brown sugar, and bring to a boil. Reduce temperature and let simmer.\r\n\r\nStep 2\r\nPlace the bottom crust in your pan. Fill with apples, mounded slightly. Cover with a lattice work crust. Gently pour the sugar and butter liquid over the crust. Pour slowly so that it does not run off.\r\n\r\nStep 3\r\nBake 15 minutes in the preheated oven. Reduce the temperature to 350 degrees F (175 degrees C). Continue baking for 35 to 45 minutes, until apples are soft.",
    "serving_size": 4,
    "category": "Lunch",
    "notes": "512 calories; protein 3.6g; carbohydrates 67.8g; fat 26.7g; cholesterol 30.5mg; sodium 240.8mg",
    "date_added": "2022-03-14T22:44:47.896949Z",
    "date_modified": null
}
```

## Create users and Tokens

First we need to create a user, 
First we’ll need to create a user who can login to the admin site. Run the following command:

$ python manage.py createsuperuser
Enter your desired username and press enter.

Username: admin
You will then be prompted for your desired email address:

Email address: admin@example.com
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

Password: **********
Password (again): *********
Superuser created successfully.

 we can log in
```
http POST http://127.0.0.1:8000/api-auth/login
```
## Examples/Screenshots

![image](https://user-images.githubusercontent.com/47580465/158274869-54eebb46-17e6-45ed-93e4-400dcf0c099d.png)
![image](https://user-images.githubusercontent.com/47580465/158274955-f5aa6112-8e40-4c2b-a9cb-9df2085aa4f7.png)



