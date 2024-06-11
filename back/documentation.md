Tue 4 Jun 2024
I realize that the Described in the Trello board was wrong redacted. So, I inquire to see if ChatGPT can fixed for me: it was the best solution.


Fri 7 Jun 2018
The configuration of Djoser as a medium to Authentications and Json Web Token as as the authorization agent, was a sui generis endeavor.
To understand the configuration process, let me put a sequence of steps, but before to starts it's necessary see the landscape complete.

Djoser:
REST implementation of Django authentication system. djoser library provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation. It works with custom user model( https://djoser.readthedocs.io/en/latest/introduction.html)

Djoser is a Django app specifically designed to handle user management tasks. It provides a set of RESTful endpoints to handle tasks like user registration, login, logout, password reset, account activation, and more.
It aims to simplify the process of adding user authentication and management to your Django REST Framework project.
Djoser can be configured to work with rest_framework_simplejwt to handle token-based authentication, but it also works with other authentication systems.
( https://chatgpt.com/c/a7fc1e0f-4bc2-4b76-a1b2-4e0f841e4a3d)

# Mon 10 Jun 2024
- Yesterday, was a tipping point in the Continues Integrations. The requirements of the Doc360 changed in it's core functionality.
Let's look at the issue, el register functionality wasn't works as the initial planning, so I took the threads to refactor the functionality.
Well, the trouble consited in change the extended native Django User into a Overriding it. But when the Django Project goes ahead in production the changes impacts almost architecture as we'll see in the following areas:
--------------------------------
- Database initialization
- Migrations must bereseted
- Initial configuration settings changes taking care of some configuration, particularly the Djoser library
- Into all scripts files where the new model class "Doc360User" is imported.
- This functionality into the api app, that is where the overriding functionality where implemented were created a new file called "managers.py".



