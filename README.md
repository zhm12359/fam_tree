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
  path takes arguments path(route, view, [], [])

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

Tutorial 3 templating and urls

In Django, web pages and other content are delivered by views.Each view is represented by a simple Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name).

To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns to views.

Views are basically subpages of the main page, so their path should be added in main page url alongside the index

Using angle brackets “captures” part of the URL and sends it as a keyword argument to the view function. The :question_id> part of the string defines the name that will be used to identify the matched pattern, and the <int: part is a converter that determines what patterns should match this part of the URL path.

Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. The rest is up to you.
All Django wants is that HttpResponse. Or an exception.

Templates

Views take templates, Django looks into the templates folder within the app
within the templates folder you should define the another folder with the same app name and inside this folder put html (templates)

Your project’s TEMPLATES setting describes how Django will load and render templates. The default settings file configures a DjangoTemplates backend whose APP_DIRS option is set to True. By convention DjangoTemplates looks for a “templates” subdirectory in each of the INSTALLED_APPS.

In other words, your template should be at polls/templates/polls/index.html. Because of how the app_directories template loader works as described above, you can refer to this template within Django simply as polls/index.html.

You need loader to load templates and httprequest as a return
With render() you don't need those, it will take render(request, path, context) and returns an httprequest object

get_object_or_404 is a shortcut for checking if an object exists
The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist.

The template system uses dot-lookup syntax to access variable attributes

Can have dynamic url based on name option in urlconf in href pass 'url' and name

Use namespaces to differentiate between templates... add app_name in app urlconf
and then change the href to use 'app_name:name' instead of name

Tutorial 4 forms

request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.

 HttpResponseRedirect takes a single argument: the URL to which the user will be redirected (see the following point for how we construct the URL in this case).
 
 Should redirect after post
 
 Django Generic Views
 
 views.GenericView.as_view()
 in views.py Generic view needs to know what model it is acting upon so you give it model to know
 also need to tell it what template to use with template_name (default template name is <app>/<app>_template.html
 
 context_object_name overrides the name used for data back from the model
 
 Tutorial 5 Testing
 
 Tutorial 6 StyleSheet and Images
 
 Django looks for css/js in static files located in the with the html
 put the files inside a file with same app name within the static folder
 *i think we do this so its easier to reference the files due to (fileFinders) in settings
  
  Static file namespacing

Just like templates, we might be able to get away with putting our static files directly in polls/static (rather than creating another polls subdirectory), but it would actually be a bad idea. Django will choose the first static file it finds whose name matches, and if you had a static file with the same name in a different application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the easiest way to ensure this is by namespacing them. That is, by putting those static files inside another directory named for the application itself.

The {% static %} template tag generates the absolute URL of static files.

Background image


 

