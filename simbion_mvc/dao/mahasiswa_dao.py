import logging
from django.db import connection
from django.core.exceptions import EmptyResultSet
from simbion_mvc.entity import Mahasiswa
from . import user_dao

LOGGER = logging.getLogger(__name__)

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

def save(mahasiswa):
    insert_query = '''
    INSERT INTO mahasiswa (
        username, npm, email, nama, alamat_tinggal, 
        alamat_domisili, nama_bank, no_rekening, nama_pemilik, no_telp
    ) VALUES (
        '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'
    )
    '''.format(
        mahasiswa.getUser().getUsername(),
        mahasiswa.getNpm(),
        mahasiswa.getEmail(),
        mahasiswa.getNama(),
        mahasiswa.getAlamatTinggal(),
        mahasiswa.getAlamatDomisili(),
        mahasiswa.getNamaBank(),
        mahasiswa.getNoRekening(),
        mahasiswa.getNamaPemilikRekening(),
        mahasiswa.getNoTelp()
    )
    cursor = connection.cursor()
    LOGGER.debug('inserting {} into database...'.format(mahasiswa))
    cursor.execute(insert_query)
    LOGGER.debug('inserted {} into database!'.format(mahasiswa))
