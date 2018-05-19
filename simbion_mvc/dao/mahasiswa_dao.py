from django.db import connection
from django.core.exceptions import EmptyResultSet
from . import user_dao
from simbion_mvc.entity import Mahasiswa

def get_by_npm(npm):
    cursor = connection.cursor()
    cursor.execute('SELECT username, npm, email, nama, alamat_tinggal,\
                    alamat_domisili, nama_bank, no_rekening, nama_pemilik, no_telp\
                    FROM mahasiswa WHERE npm=\'{}\''.format(npm))
    result = cursor.fetchone()
    if result is None:
        raise EmptyResultSet('Mahasiswa with npm \'{}\' does not exists'.format(npm))
    return Mahasiswa(user_dao.get_by_username(result[0]), result[1], result[2], result[3], result[4], 
                     result[5], result[6], result[7], result[8], result[9])
