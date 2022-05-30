<h1 align="center">Meg's Italian Kitchen</h1>

<h3>Milestone Three Project - Python and Data Centric Development</h3>
<br>

**Please note: To open any links in this document in a new browser tab, press 'CTRL + Click'.**

<a id=#table-of-contents></a>
# Table of Contents
<details open>
<summary><b>(click to expand or hide)</b></summary>
<!-- Markdown TOC -->

1. [Description](#description)
2. [User Experience (UX)](#user-experience-(ux))
   * [User Stories](#user-stories)
   * [5 Planes](#5-planes)
     1. [Strategy](#strategy)
     2. [Scope](#scope)
     3. [Structure](#structure)
     4. [Skeleton](#skeleton)
     5. [Surface](#surface)
3. [Features](#features)
   * [Current Features](#current-features)
   * [Future Features](#future-features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Lessons Learned](#lessons-learned)
7. [Deployment](#deployment)
8. [Credits](#credits)

<!-- /Markdown TOC -->
</details>

<a id="description"></a>
# Description  

I am currently studying the Full Stack Development Course through Code Institute. Part of the course I am required 
to complete 4 milestone projects. Meg's Italian Kitchen is my 3rd milestone project which is part of the Python and Data Centric Development.  

Meg's Italian Kitchen has been created for all lovers of Italian food.  
The purpose of this website is to have a variety of Italian recipes display so people can create mouth watering meals. 
The website will also accommodate for users that would like to add new recipes and amend and delete their own recipes when needed.

[Back to Table of Contents](#table-of-contents)

<a id="user-experience-(ux)"></a>
# User Experience (UX)

<a id="user-stories"></a>
## User Stories  

First Time Visitor Goals

* As a first time visitor to the website, I would like to:  
  * search for Italian recipes
  * view various Italian recipes
  * have the meals in categories so they are easier to find
  * add a recipe to my favourites
  * be able to have the opportunity to register so I can add new recipes to the database
  * be able to contact the site owner to ask questions if required

Returning Visitor Goals

* As a returning user to the website, I would like to:
  * have the ability to log in so I can view my recipes
  * have the ability to search for recipes whilst logged in
  * have the ability to add a recipe
  * have the ability to amend the recipe as required
  * have the ability to delete my own recipes
  * add a recipe to my favourites
  * delete a recipe from my favourites
  * be able to contact the site owner to ask questions if required

[Back to Table of Contents](#table-of-contents)

<a id="5-planes"></a>
## 5 Planes

<a id="strategy"></a>
### 1. Strategy

The purpose of this project is to create an online Italian cookbook where users can search and/or log in and add, amend and delete their own recipes.

<a id="scope"></a>
### 2. Scope

The features of this project will include:

* The ability to:
  * search for Italian recipes
  * view all Italian recipes
  * have the meals in categories so they are easier to locate
  * register to add new recipes to the database
  * once registered to have a log in/out screen that the user can return to
  * view the users recipes that have been added by that user
  * add my own recipe
  * amend my recipe
  * delete my recipe
  * add a recipe to my favourites
  * delete a recipe from my favourites
  * contact the site owner to ask questions if required

<a id="structure"></a>
### 3. Structure

The information is grouped logically for all users. The Interaction Design (IXD) will be 
consistent between pages where the navigation bar is fixed and tailored to have the priority 
items displayed first at the top of the screen. The footer will scroll with the page. A user 
can either search and view all recipes and/or log in to add, amend, delete their own recipes 
and add them to favourites. Once the 'Contact Us' content has been submitted, the user will have 
clear feedback that the information has been submitted. The site will be consistent with what 
users expect from an online cookbook.

<a id="skeleton"></a>
### 4. Skeleton

The [wireframes](./static/documents/wireframes/megs-italian-kitchen.pdf) have been created using [Balsamiq](https://balsamiq.com/) and were created 
for Desktop, Tablet and Phone.

Here are the individual wireframes:

* [Home Page Wireframe](static/images/readme-images/wireframes/homepage.png)
* [Entree Wireframe](static/images/readme-images/wireframes/entree.png)
* [Mains Wireframe](static/images/readme-images/wireframes/main.png)
* [Dessert Wireframe](static/images/readme-images/wireframes/dessert.png)
* [Register Wireframe](static/images/readme-images/wireframes/register.png)
* [Log In Wireframe](static/images/readme-images/wireframes/login.png)
* [Add Recipe Wireframe](static/images/readme-images/wireframes/add-recipe.png)
* [My Recipes Wireframe](static/images/readme-images/wireframes/my-recipes.png)
* [Edit Recipe Wireframe](static/images/readme-images/wireframes/edit-recipe.png)
* [Favourites Wireframe](static/images/readme-images/wireframes/favourites.png)
* [Contact Us Wireframe](static/images/readme-images/wireframes/contact-us.png)
* [404 Error Wireframe](static/images/readme-images/wireframes/404-error.png)

<a id="surface"></a>
### 5. Surface 

Colour Scheme


Typography

* The fonts were sourced from [Google Fonts](https://fonts.google.com/).
* Simonetta is used for all the headings with sans-serif as the fallback font. This font was 
chosen from an [Italian Fonts Google search](https://www.1001fonts.com/regular+italian+google-web-fonts.html).
* Open Sans is the main font used through the website with sans-serif as the fallback font. This font 
was chosen as Simonetta is a serif font and Open Sans is a sans serif font and these both compliment each other.

Imagery


[Back to Table of Contents](#table-of-contents)

<a id="features"></a>
# Features

<a id="current-features"></a>
**Current Features**


<a id="future-features"></a>
**Future Features to implement**


[Back to Table of Contents](#table-of-contents)

<a id="technologies-used"></a>
# Technologies Used

**Languages**

1. [HTML5](https://en.wikipedia.org/wiki/HTML5)
2. [CSS3](https://en.wikipedia.org/wiki/CSS)
3. [Python 3](https://www.python.org/)

**Databases**

1. [MongoDB Atlas](https://www.mongodb.com/)

**Frameworks and Libraries**

1. [DNSPython](https://www.dnspython.org/) - is a toolkit for Python
1. [Flask](https://palletsprojects.com/p/flask/) - is a lightweight WSGI web application framework
1. [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) - bridges Flask and PyMongo and provides some convenience helpers
1. [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - is a templating engine for Python
1. [jQuery](https://developer.mozilla.org/en-US/docs/Glossary/jQuery) - used to initialise the Materialize CSS components
1. [Materialize](https://materializecss.com/getting-started.html) - to make the website responsive and use custom components
1. [PyMongo](https://pymongo.readthedocs.io/en/stable/) - is a Python distribution containing tools for working with MongoDB
1. [Werkzeug](https://werkzeug.palletsprojects.com/en/2.1.x/) - is a comprehensive WSGI web application library and was used for security features

**Programs and Resources**

1. [Balsamiq](https://balsamiq.com/) - wireframes
1. [Code Institute Course Content](https://learn.codeinstitute.net/login?next=/) - main source of fundamental knowledge
1. [Coolors](https://coolors.co/) - to display colour palette
1. [Font Awesome](https://fontawesome.com/v5/search) - for their icons
1. [Git](https://git-scm.com/) - version control
1. [GitHub](https://github.com/) - used to store the project files
1. [Gitpod](https://www.gitpod.io/) - IDE
1. [Google Fonts](https://fonts.google.com/) - typography
1. [Heroku](https://id.heroku.com/login) - a container-based cloud Platform as a Service (PaaS) used to deploy the project 
1. [Snagit](https://www.techsmith.com/screen-capture.html) - screen capture and resizing images
1. [TinyPNG](https://tinypng.com/) - efficient compression of images for the site
1. [WebAIM](https://webaim.org/resources/contrastchecker/) - web accessibility contrast checker

[Back to Table of Contents](#table-of-contents)

<a id="testing"></a>
# Testing

[See Testing.md for testing information](TESTING.md)

[Back to Table of Contents](#table-of-contents)

<a id="lessons-learned"></a>
# Lessons Learned


[Back to Table of Contents](#table-of-contents)

<a id="deployment"></a>
# Deployment


**Run this site locally**


[Back to Table of Contents](#table-of-contents)

<a id="credits"></a>
# Credits

Code


Content  


Media  


Acknowledgements


[Back to Table of Contents](#table-of-contents)