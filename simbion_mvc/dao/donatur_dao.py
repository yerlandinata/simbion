import logging
from django.db import connection
from django.core.exceptions import EmptyResultSet
from simbion_mvc.entity import Donatur
from . import user_dao

LOGGER = logging.getLogger(__name__)

def get_by_id(id_num):
    cursor = connection.cursor()
    cursor.execute('SELECT username, nomor_identitas, email, \
                    nama, npwp, alamat, no_telp\
                    FROM donatur WHERE nomor_identitas=\'{}\''.format(id_num))
    result = cursor.fetchone()
    if result is None:
        raise EmptyResultSet('Donatur with id \'{}\' does not exists'.format(id_num))
    return Donatur(user_dao.get_by_username(result[0]), result[1], result[2], 
                result[3], result[4], result[5], result[6])

def save(donatur):
    insert_query = '''
    INSERT INTO donatur (username, nomor_identitas, email, nama, npwp, alamat, no_telp) 
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')
    '''.format(
            donatur.getUser().getUsername(),
            donatur.getId(),
            donatur.getEmail(),
            donatur.getNama(),
            donatur.getNpwp(),
            donatur.getAlamat(),
            donatur.getNoTelp()
        )
    cursor = connection.cursor()
    LOGGER.debug('inserting {} into database...'.format(donatur))
    cursor.execute(insert_query)
    LOGGER.debug('inserted {} into database!'.format(donatur))
