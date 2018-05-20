import logging
from django.core.exceptions import EmptyResultSet
from django.shortcuts import redirect, reverse
from simbion_mvc.dao import user_dao, mahasiswa_dao, donatur_dao

logger = logging.getLogger(__name__)

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def isValid(self):
        return len(self.username) > 0 and len(self.password) >= 8
    
    def __repr__(self):
        return 'Login: username={}, password={}'.format(self.username, self.password)

class LoginFailedException(Exception):
    pass

# will return User
def attempt_login(login):
    if not login.isValid():
        raise LoginFailedException()
    try:
        logger.debug('attempt to login with {}'.format(login))
        user = user_dao.get_by_username(login.username)
    except EmptyResultSet:
        logger.debug('username does not exist')
        raise LoginFailedException()
    if user.getPassword() != login.password:
        logger.debug('wrong password')
        raise LoginFailedException()
    logger.info('Login suceess - {}'.format(user))
    return user

def require_role(mahasiswa=False, donatur=False, admin=False):
    def require_login(function):
        def wrapper(request, *args, **kwargs):
            user = request.session.get('simbion_user', False)
            if user:
                if (user['role'] == 'mahasiswa' and mahasiswa) or (user['role'] == 'donatur' and donatur) or (user['role']   == 'admin' and admin):
                    return function(request, *args, **kwargs)
            return redirect(reverse('login'))
        return wrapper
    return require_login

def require_guest(function):
    def wrapper(request, *args, **kwargs):
        if request.session.get('simbion_user', False):
            return redirect(reverse('home'))
        else:
            return function(request, *args, **kwargs)
    return wrapper
