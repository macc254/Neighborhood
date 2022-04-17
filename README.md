# HoodYangu - A Neighbourhood Web App built with Django
>[Repo link: ](https://github.com/macc254/Neighborhood.git)
## Author 

>[Mercy Bore](https://github.com/macc254)  
##  Live Link  
You can view the project [here](https://mercy-neighbourhood.herokuapp.com/)
  
  
# Description  

This is a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.
## User Story  
A user can :

- Sign in with the application to start using.
- Set up a profile  and a general location and neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities   near my neighborhood.
- Create Posts that will be visible to everyone in the neighborhood.
- Change the neighborhood when the user  decides to move out.
- Only view details of a single neighborhood. 


## Screenshots 
## Home page
In the homepage, a user is able to login or sign up to be able to to view each neighburhood and its details.
 ![home](https://user-images.githubusercontent.com/61621637/163714631-a0d81b04-c5a6-4b2e-809d-a6ca09a92c60.png)
## Login
An existing user enters their details here to login. There is an option for signing up for new users.
![login](https://user-images.githubusercontent.com/61621637/163714625-383e6c0e-fab7-4075-bc1c-a86194a9412c.png)

## Sign up page
This is a page where a new user will register.
 ![register](https://user-images.githubusercontent.com/61621637/163714621-3d347431-54e6-4af7-b746-b2e6938e5671.png)
## Join a neighborhood
![join-hood](https://user-images.githubusercontent.com/61621637/163714597-15d4e74a-631e-4913-a32e-91252fbe79c9.png)
## View details of your current neighborhood
![cureent-neigh](https://user-images.githubusercontent.com/61621637/163714555-ac592968-b9ed-4e11-9505-3d1911278184.png)
## Leave a neighborhood
![leave-hood](https://user-images.githubusercontent.com/61621637/163714611-e12ba7c9-5e0f-472f-8ce9-0d1070b35780.png)


## Add a business and post
![biz](https://user-images.githubusercontent.com/61621637/163714574-18243d5a-4ca0-4f56-870c-eaa92fc51c8c.png)

## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/macc254/Neighborhood.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd neighborhood pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
 python3 -m venv venv - source bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  

 
## Technology used  
  
* [Python3.8.10](https://www.python.org/)  
* [Django 4.0.4](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)    
## Contact Information   
If you have any question or contributions, please email me at [mercycherotich757@gmail.com](mailto:mercycherotich757@gmail.com)
  
## License 
[License](https://github.com/macc254/Neighborhood/blob/master/License)  
* Copyright (c) 2022 **Mercy Bore**
