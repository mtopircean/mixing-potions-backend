# Mixing-Potions API

The mixing-potions api is an application which was designed to support the backend of a social network platform supporting users in creating mixes of natural products, more specifically essential oils and in sharing them with other users 

Application is designed to allow users to use an existing database of products, mix them and share it as posts with various functionalities attached.

Main features:

- Authentication of users
- Creation of products and body system filters through an excel import/export admin panel functionality
- Administration of the product/profile/post database by the admin from backend of the API using the Django administration panel
- Endpoints for photos upload(for customized posts), post and product storage/processing
- Endpoints supporting user interactions on Profiles, Likes, Comments, Followers and Posts

In order to access the deployed API, please use the link bellow:

[MIXING POTIONS BACKEND](https://mixing-potions-drf-api-0a8cbdf11dd2.herokuapp.com/)

To access the final front-end project:

[Heroku App](https://mixing-potions-d88ebb719d59.herokuapp.com/)

[Github Repo](https://github.com/mtopircean/mixing-potions-frontend/)



## Table of Contents
- [Scope](#scope) 
- [Features](#features)
    - [Features Implemented](#features-implemented)
    - [Future development](#future-development)
- [Agile Methodology](#agile-methodology)
    - [Project planning](#project-planning)
    - [Milestones](#milestones)
    - [Sprints](#sprints)
    - [Epics](#epics)
    - [User stories](#user-stories)
    - [Prioritization](#prioritization)
- [Database structure](#database-structure)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
    - [Frameworks and Languages](#frameworks-and-languages)
    - [Python add-ons](#python-add-ons)
    - [Other](#other)
- [Testing](#testing)
    - [Code formating](#code-formating)
    - [Unittest](#unittest)
    - [Manual Testing](#manual-testing)
- [Bugs and issues](#bugs-and-issues)
    - [Fixed](#fixed)
    - [Open](#open)
- [Deployment](#deployment)
    - [How do Deploy](#how-to-deploy)
    - [How to Fork](#how-to-fork)
    - [How to Clone](#how-to-clone)
    - [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
    - [Sources](#sources)
    - [Aknowledgements](#acknowledgements)
- [About author](#about-author)

## Scope

Project idea came on top of the previous submitted project, especially as an extension to PP4 – Essential Oils website. It comes as an extension to a tool which allows users to search products based on specific conditions.

Extension and the scope represents a method/application in which users can share their experiences and the different variations they have used the products and their results. It offers the other users to take informed and documented decision when using the products. 

It also builds a community around the products and the administrator and offers a more targeted way of interaction. The features planned for future implementation will build further on the scope of the application.

To access the final front-end project:

[Heroku App](https://mixing-potions-d88ebb719d59.herokuapp.com/)

[Github Repo](https://github.com/mtopircean/mixing-potions-frontend/)

## Features

### Features implemented

-  Profile creation: Users can sign up and login. Sign-up process is responsible for profile creation.
-  Product and body system creation: admins and staff can create the products used for posts through an import/export excel system managed through the backend of the API app; feature and product administration is restricted to administrators

-  Post creation: users can create posts with multiple functionality options allowing them to use products/product combinations in order to create a product mix recommendation; users have also the option to upload their own image when creating a product, model for post being setup in order to allow it to take an image

-  User ranking option: User avatar/photo is set conditioned on a ranking that is allocated to the user; at the moment this is done backend manually, but front end application will build on this in order to set the ranking automatically based on number of likes a users has on a post or number of followers

-  Post liking/un-liking: Users have the ability to like each others posts or unlike them; security feature exists not allowing users to like or unlike their own posts

-  User following/unfollowing: Users have the ability to follow or un-follow each other; security feature build so they don`t have the capability to follow themselves

-  Post comments: Users have the ability to comment on another users post, with administrators having the ability to moderate it

-  Filtering and searching functionality: offers the ability to filter, search and sort the various databases for better result feedback



### Future development

-  Improved product management: allow the administrators to be able to add products and body system options outside of the standard administrator panel, by adding individual products

-  Introduction of “condition” as a further enhancement in user post creation functionality

-  User messaging system to be introduced at a later stage
-  Groups creation: in order to allow a specific user to create their groups in order to recommend mixes of products in a more targeted way




## Agile methodology

Development of the project was build around the Agile methodology and considered the applicable planes:

STRATEGY: Understanding the backend objectives and translating them into a Kanban system focused around epics, stories, milestones and allocating the effort necessary to complete them

SCOPE: Defining the objective/direction of the application through definition of user stories

STRUCTURE : which represented the data models and API endpoints design and definition


SURFACE and SKELETON are to be further defined as part of the front-end application – link to kanban here: [Front-End Kanban](https://github.com/users/mtopircean/projects/15)

### Project planning
![Current Kanban](/docs/images/kanban_current_board.png)


Prioritization was set in a very logical manner by creating key milestones connected to Sprints and to Epics. This has allowed a very targeted approach by allowing focus on specific deliverables and seeing them to completion.

User stories where created to sustain the key deliverables.

Overview of project status as of 24.02.2024:
![Current Kanban](/docs/images/kanban_current.png)


### Milestones

Total of 3 milestones created around following project delivery objectives:

- Testing and cleanup
- Extended features
- Basic functionality

### Sprints

Total of 3 Sprints created closely connected to Epics and key deliverables and Epics focus points.

### Epics

Total of 4 Epics created with very targeted action of functionality deliverable. This are further broken down into Stories breaking the deliverable into more targeted actions.

Epics focus on 4 elements:
- Setup and deployment
- Functionality: basic and extended
- Documentation

EPICS:

EPIC 1: Setup and Deployment

EPIC 2: Create basic functionality

EPIC 3: Create extended functionality

EPIC 4: Create documentation & Testing

### User stories

A total of 12 user stories created around key applications functionality.
Validation and tracking of user stories completion and status is linked to epics and milestones, but even more to a prioritization based on importance in project deliverable and to a an effort allocation system.

Each EPIC contains 3 user stories, each containing a specific level of acceptance criteria that ensures the stories are fulfilled accordingly.

USER STORIES:

Installation and deployment:

User Story 1.1: Install and Configure basic dependencies

User Story 1.2: Deploy to Heroku

User Story 1.3: Create Document Hierarchy and Structure 

Basic functionality:

User Story 2.1: Create Profiles App

User Story 2.2: Create Products App

User Story 2.3: Create Posts App


Extended functionality:

User Story 3.1: Create Likes App

User Story 3.2: Create Followers App

User Story 3.3: Create Comments App


Testing and Readme:

User Story 4.1: Create README File

User Story 4.2: Perform Unittest Testing

User Story 4.3: Create TESTING Document


### Prioritization



Prioritization was done based on 2 criteria:
- Importance allocation: Must – Should – Could: no could or Would existing at the moment in the plan

- Effort(established by using a middle point from an effort/effect impact and allocating the stories aligned to this reference point): using story points;



## Database structure:

Following diagram offers an understanding around the design direction taken when defining the models and data structure.

There is a clear level of customization done through the introduction of some customized features around the Profile model which allows user to be allocated a specific ranking.

Further customization is done also around the Post model which integrates the Products one in order to allow users to build a Post by accessing the Product model.

Profile, Post and Products are the core of the application with enhanced features and structure.


Link to diagram:
![db diagram](/docs/images/db_diagram.png)



## API Endpoints

Application provides the following API endpoints:
**Endpoint**|**HTTP Method**|**CRUD**|**View Type**|**Permissions**|**Filter/Search**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
/profiles/|GET|Read (List)|List|Public|Filters: "followers", "following"
/profiles/int:pk/|GET|Read (Detail)|Detail|Owner| 
/products/|GET, POST|Read (List), Create (List)|List|Authenticated, Admin|Filters: "name", "condition\_\_name", "body\_systems\_\_name"
/products/int:pk/|GET, PUT, DELETE|Read (Detail), Update (Detail), Delete (Detail)|Detail|Authenticated, Admin| 
/posts/|GET, POST|Read (List), Create (List)|List|Authenticated or ReadOnly|Filters: "title", "owner\_\_profile\_\_nickname", "products\_\_name"
/posts/int:pk/|GET, PUT, DELETE|Read (Detail), Update (Detail), Delete (Detail)|Detail|Owner| 
/likes/|GET, POST|Read (List), Create (List)|List|Authenticated or ReadOnly| 
/likes/int:pk/|GET, DELETE|Read (Detail), Delete (Detail)|Detail|Owner| 
/followers/|GET, POST|Read (List), Create (List)|List|Authenticated| 
/followers/int:pk/|GET, DELETE|Read (Detail), Delete (Detail)|Detail|Owner| 
/comments/|GET, POST|Read (List), Create (List)|List|Authenticated or ReadOnly| 
/comments/int:pk/|GET, PUT, DELETE|Read (Detail), Update (Detail), Delete (Detail)|Detail|Owner| 

## Technologies Used

### Frameworks and Languages

The API is built with [Django Rest Framework](https://www.django-rest-framework.org/), a [Django](https://www.djangoproject.com/) based toolkit for building APIs with Python.

### Python add-ons

asgiref==3.7.2: ASGI reference implementation for handling asynchronous requests.

cloudinary==1.38.0: Python SDK for interacting with the Cloudinary API.

diff-match-patch==20230430: Library for performing text diffs and patching.

dj-database-url==0.5.0: Utility for parsing database connection URLs in Django.

dj-rest-auth==2.1.9: Django app providing REST API endpoints for authentication.

Django==3.2.23: High-level Python web framework for rapid development.

django-allauth==0.44.0: Complete authentication system for Django projects.

django-cloudinary-storage==0.3.0: Django storage backend for Cloudinary.

django-cors-headers==4.3.1: Django app for handling Cross-Origin Resource Sharing (CORS) headers.

django-filter==23.5: Django app for dynamic queryset filtering.

django-import-export==3.3.6: Utilities for importing and exporting data in Django.

djangorestframework==3.14.0: Toolkit for building Web APIs in Django.

djangorestframework-simplejwt==5.3.1: JWT authentication for Django REST Framework.

et-xmlfile==1.1.0: Library for reading and writing Excel .xlsx files.

gunicorn==21.2.0: WSGI HTTP server for UNIX.

MarkupPy==1.14: Lightweight library for generating HTML markup.

oauthlib==3.2.2: Library for implementing OAuth 1.0 and OAuth 2.0 protocols.

odfpy==1.4.1: Library for working with OpenDocument Format (ODF) files.

openpyxl==3.1.2: Library for reading and writing Excel .xlsx files.

pillow==10.2.0: Python Imaging Library (PIL) fork for image manipulation.

psycopg2==2.9.9: PostgreSQL adapter for Python.

PyJWT==2.8.0: Library for encoding and decoding JSON Web Tokens (JWT).

python3-openid==3.2.0: Library for working with OpenID authentication.

pytz==2023.3.post1: Library for working with time zones.

requests-oauthlib==1.3.1: Library for OAuth authentication with requests.

sqlparse==0.4.4: Library for parsing SQL queries.

tablib==3.5.0: Library for handling tabular data in various formats.

xlrd==2.0.1: Library for reading data from Excel .xls files.

xlwt==1.3.0: Library for writing data to Excel .xls files.

### Other

- [GitHub](https://github.com/) used for project storage
- [Heroku](https://heroku.com/) is used to deploy the project
- [ElephantSQL](https://www.elephantsql.com/) is used for the project's PostgreSQL database.
- [Cloudinary](https://cloudinary.com/) is used to store media files and for processing uploaded audio files.
- [GitPod](https://gitpod.com/) my IDE of choice
- [DrawSQL](https://drawsql.app/) used to create my db diagram
- [CI Python Linter](https://pep8ci.herokuapp.com/) Used to validate my code for formating compliance

## Testing

Testing has been implemented through a combination of manual and automated testing.

### Code formating

Code passed through the PEP8 Code formatter and passed without any deviations from standard.
![pep8](/testing/images/pep8_noerror.png)


### Unittest

Unittest implemented for all applications basic functionality and results can be seen bellow:
-  Profiles:
![Alt](/testing/images/unitttest_profiles.png)
-  Posts:
![Alt](/testing/images/unitttest_posts.png)
-  Products:
![Alt](/testing/images/unitttest_products.png)
-  Followers:
![Alt](/testing/images/unitttest_followers.png)
-  Comments:
![Alt](/testing/images/unitttest_comments.png)
-  Likes:
![Alt](/testing/images/unitttest_likes.png)

### Manual testing

Application functionality is tested and can be found at the link bellow:
[TESTING.MD](/testing/TESTING.md)

## Bugs and issues
No major issues, just a couple of console errors.

### Open

- One error found which is visible on the deployed site in Chrome only in normal mode. This dissapears when moving to incognito mode.
Normal mode:

![Alt](/testing/images/recaptcha.png)

Incognito mode:

![Alt](/testing/images/recaptcha_incognito.png)


- Another console error due to favicon missing. I can`t add a favicon to the backend site.

![Alt](/testing/images/favicon_console.png)

- And lastly, when in DEBUG mode False, when deploying the site in gitpod, it gives me a series of errors which, are not present in the deployed sited. I understand this is related mostly to static not being able to load, and normal errors.
Discussing with the tutor I was advised that is normal to have them as the website will not load css, not even in admin mode

![Alt](/testing/images/debug_false.png)

CSS missing:
![Alt](/testing/images/css_missing.png)



## Deployment

### How to Deploy
Deployment of the website was done using HEROKU, and can be accessed here [MIXING POTIONS BACKEND](https://mixing-potions-drf-api-0a8cbdf11dd2.herokuapp.com/).

### How to Fork
To fork the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [mtopircean/mixing-potions-backend](https://github.com/mtopircean/mixing-potions-backend)
3. Click the Fork button in the top right corner.

### How to Clone
To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [mtopircean/mixing-potions-backend](https://github.com/mtopircean/mixing-potions-backend)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

### Heroku Deployment
The project was deployed to [Heroku](https://heroku.com).
Deployed site can be found [Here](https://mixing-potions-drf-api-0a8cbdf11dd2.herokuapp.com/).
To deploy, follow this steps:

1. Create an account at https://heroku.com and login. 
![Alt](/docs/images/heroku_1.png)

2. Create a new app from the [Heroku dashboard](https://dashboard.heroku.com) by clicking on `New` and then on `Create new app`.

![Alt](/docs/images/heroku_2.png)
3. Create a unique name for your app.

![Alt](/docs/images/heroku_3_4.png)
4. Choose your region (US or Europe).

![Alt](/docs/images/heroku_3_4.png)
5. Go to the **Settings** tab and click on **Reveal Config Vars** in the **Config Vars** section.

![Alt](/docs/images/heroku_5.png)
6. Now, one by one, add the following config vars:

    | Name | Value | 
    |---|---|
    | ALLOWED_HOSTS | \<your deployed heroku API app url\> * |
    | CLIENT_ORIGIN_DEV | \<your development environment url\> ** |
    | CLIENT_ORIGIN | \<your client url\> |
    | CLOUDINARY_URL | \<Your cloudinary url\> | 
    | DATABASE_URL | \<Your database url\> | 
    | DISABLE_COLLECTSTATIC | 1 |
    | SECRET_KEY | \<some random string\> |

 Paste the URL without 'https://' or a trailing slash!
 E.g. "http://localhost:3000" for building a React front end app in a local environment. 
 This may differ for your IDE.

 ![Alt](/docs/images/heroku_6.png)

7. Select the **Deploy** tab and connect the Heroku app to your GitHub repository.

![Alt](/docs/images/heroku_7.png)
8. Scroll down and choose the branch you want to deploy in the *Manual deploy* section. Click **Deploy Branch** for your first deployment.

![Alt](/docs/images/heroku_8.png)
9. Select **View** to open your deployed app.

![Alt](/docs/images/heroku_9.png)
10. If you encounter issues, use **More** and then **View logs** or check the **Activity** tab for debugging.

## Credits

### Sources

The initial setup and the general structure of the project are based on the instructions from the Code Institute *Django Rest Framework* walkthrough project ([source code](https://github.com/Code-Institute-Solutions/drf-api/)). The basic structure of the models (and their serializers), as well as the filtering functionality has been inspired from the walkthrough project. This was further enhanced through the introduction of customization in Models like Products, Profiles, Posts and more through introductions of other functionalities like Slugs to display objects instead of ids.

Took very limited inspiration on the Readme structure and Heroku deployment instructions from  [nacht-falter/sonic-explorers-api](https://github.com/nacht-falter/sonic-explorers-api/blob/main/README.md)


### Acknowledgements

- I would like to thank my Code Institute mentor Mo for his support and guidance during the development of the project
- I would like to thank the Code Institute tutors for their excellent and continuous support and patience during the development of the application

## About author
Marius Topircean is an aspiring software-developer on a journey to develop and learn his place into the developer community.

My contact details are:

Email: mtopircean@yahoo.com

Phone: +353857642212

Slack: Marius Topircean

GitHub: mtopircean

LinkedIn: [Marius Topircean](https://www.linkedin.com/in/marius-t-7b5592124)