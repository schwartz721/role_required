from flask import Flask
from flask_login import LoginManager, login_required
from role_required import ROLE_required, not_ROLE

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
# LoginManager needs the `not_ROLE` method to redirect users without ROLE privileges.
LoginManager.not_ROLE = not_ROLE
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.not_ROLE_view = 'not_ROLE'


# You can demo the @ROLE_required functionality by running this flask app with
# different demo users. Uncomment a user and try to access the views below.
from demo_users import UnauthorizedUser, BasicUser, RoleUser
# user = UnauthorizedUser()
# user = BasicUser()
user = RoleUser()


@app.route('/')
def index():
    return 'Anyone can visit this page.'

@app.route('/user-page/')
@login_required
def user_page():
    return 'Any logged-in users can visit this page.'

@app.route('/ROLE-page/')
@ROLE_required
def ROLE_page():
    return 'Only logged-in ROLE users can visit this page.'

@app.route('/login/')
def login():
    return 'Login page. Unauthorized users requesting @login_required or\
            @ROLE_required pages are redirected here.'

@app.route('/not-ROLE/')
@login_required
def not_ROLE():
    return "Authorized users without ROLE privileges are redirected here.<br>\
            Notice that this view can be @login_required, because only users\
            who are authorized but who don't have ROLE privileges will be\
            redirected here.<br>\
            Unauthorized users accessing an @ROLE_required view are redirected\
            to the login_view, so a @login_required decorator is not\
            additionally needed on a @ROLE_required view."


# DO NOT INCLUDE THIS IN YOUR FLASK APP
# This overrides the LoginManager's functionality and is only for demo purposes.
import flask_login.utils as utils
def force_user():
    return user
utils._get_user = force_user
