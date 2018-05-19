from django.db import connection
from django.core.exceptions import EmptyResultSet
from simbion_mvc.entity import User

def get_by_username(username):
    cursor = connection.cursor()
    cursor.execute('SELECT username, password, role FROM pengguna WHERE username = \'{}\''.format(username))
    result = cursor.fetchone()
    if result is None:
        raise EmptyResultSet('User with username \'{}\' does not exists'.format(username))
    return User(result[0], result[1], result[2])
