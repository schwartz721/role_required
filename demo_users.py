from flask_login.mixins import AnonymousUserMixin, UserMixin

class UnauthorizedUser(AnonymousUserMixin):
    # The AnonymousUserMixin is used by flask-login for unauthorized users.
    pass

class BasicUser(UserMixin):
    # BasicUser has role set to anything other than the string 'ROLE'.
    role = None

class RoleUser(UserMixin):
    # RoleUser has role set to the string 'ROLE'.
    role = 'ROLE'
