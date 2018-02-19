# PCT Treehouse

Hi. This a project dedicates to create a family tree application for frat "family" tree management. 


# Scope

Features to implement:
1. User login
2. Upload excel to generate family tree data structures
3. Data visualization on user board
4. DFS to print out all paths so it will be easier for assignment


Django Notes

Tutorial 1 Quick Set Up

Views are written in views.py

New url needs to be added to root conf and directory conf so that root conf can figure out where to go and what to load

include() cuts off the search
path() is used in directory conf

Tutorial 2 Database and Admin

database

Models are added in models.py
All models inherit from model.models
All fields inherit from field class
Name of data attribute is column
Models need to be activated and then migrated
settings.py are the settings for django root
news apps for django need to be added to setting installed_apps
add str method to have cleared visuals in database

admin

admin is already made
create an admin
allow you app to be modified in admin you need to add the models in admin.py in directory
