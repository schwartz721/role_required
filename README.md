# role_required
A super light-weight alternative to flask-user or flask-security that adds
role requirements for views to flask-login.

role_required is a template for a view decorator that can be customized to
restrict access to flask views to users who have been given a specific role.
The app will now have "privileged" users, in addition to the authorized and
unauthorized users that flask-login provides. The template defines the
decorator as ROLE_required with the expectation that ROLE will be replaced by
the developer to fit the context of their app. For example, ROLE could be
changed to admin, giving the developer an @admin_required decorator.. 

***The developer should change all instances of ROLE (in all-caps) for proper
functionality***

User models will need a role attribute which can be set to match the value of
ROLE chosen by the developer. If the role attribute equals anything other than
the chosen string, the user will not be able to access the @ROLE_required
decorated views.

The @ROLE_required decorator includes the same functionality as flask-login's
@login-required. It will redirect unauthorized users to the same view as
@login_required. The developer specifies a 'not_ROLE' view that users who are
authorized aren't privileged are redirected to.

Set Up (see app.py for an example of proper set up):
-Add role_required.py to the flask app's directory where it can be accessed by
the same file that instantiates flask_login.LoginManager.
-From role_required import not_ROLE, and add a not_ROLE method to LoginManager.
-Give LoginManager a not_ROLE_view attribute that is a string that indicates
which view function to redirect authorized but unprivileged users to.
-From role_required import ROLE_required wherever routes are defined, and
decorate privileged routes.

Demo:
To demo the functionality, clone the whole repo. Run the flask app in a
virtualenv with flask-login installed. In app.py, take turns uncommenting the
three different demo users to see which pages they can and can't access, and
which redirect views they are sent to.
