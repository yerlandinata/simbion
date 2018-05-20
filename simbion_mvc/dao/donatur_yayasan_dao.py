import logging
from django.db import connection
from django.core.exceptions import EmptyResultSet
from simbion_mvc.entity import DonaturYayasan
from . import donatur_dao

LOGGER = logging.getLogger(__name__)

def get_by_no_sk(no_sk):
    cursor = connection.cursor()
    cursor.execute('SELECT nomor_identitas_donatur, no_sk, email, nama, no_telp_cp\
                    FROM yayasan WHERE no_sk = \'{}\''
                    .format(no_sk))
    result = cursor.fetchone()
    if result is None:
        raise EmptyResultSet('Yayasan donatur with sk \'{}\' does not exists'.format(no_sk))
    return DonaturYayasan(donatur_dao.get_by_id(result[0]), result[1], result[2], result[3], result[4])

def save(donatur_yayasan):
    insert_query = '''
    INSERT INTO yayasan (nomor_identitas_donatur, no_sk_yayasan, email, nama, no_telp_cp)
    VALUES ('{}', '{}', '{}', '{}', '{}')
    '''.format(
            donatur_yayasan.getDonatur().getId(),
            donatur_yayasan.getNoSk(),
            donatur_yayasan.getEmail(),
            donatur_yayasan.getNama(),
            donatur_yayasan.getNoTelp()
        )
    cursor = connection.cursor()
    LOGGER.debug('inserting {} into database...'.format(donatur_yayasan))
    cursor.execute(insert_query)
    LOGGER.debug('inserted {} into database!'.format(donatur_yayasan))
