import logging
from django.db import connection
from django.core.exceptions import EmptyResultSet
from simbion_mvc.entity import SkemaBeasiswa
from . import donatur_dao

LOGGER = logging.getLogger(__name__)

def get_by_kode(kode_beasiswa):
    cursor = connection.cursor()
    cursor.execute('SELECT nomor_identitas_donatur,kode,nama,jenis,deskripsi\
                    FROM SKEMA_BEASISWA\
                    WHERE kode={}'.format(kode_beasiswa))
    result = cursor.fetchone()
    if result is None:
        raise EmptyResultSet('Beasiswa with kode \'{}\' does not exists'.format(kode_beasiswa))
    return SkemaBeasiswa(donatur_dao.get_by_id(result[0]), result[1], result[2], result[3], result[4])

def save(skema_beasiswa):
    insert_query = '''
    INSERT INTO skema_beasiswa (
        kode, nama, jenis, deskripsi, nomor_identitas_donatur) VALUES (
        '{}', '{}', '{}', '{}', '{}'
    )
    '''.format(
        skema_beasiswa.getKode(),
        skema_beasiswa.getNama(),
        skema_beasiswa.getJenis(),
        skema_beasiswa.getDeskripsi(),
        skema_beasiswa.getDonatur().getId()
    )
    cursor = connection.cursor()
    LOGGER.debug('inserting {} into database...'.format(skema_beasiswa))
    cursor.execute(insert_query)
    LOGGER.debug('inserted {} into database!'.format(skema_beasiswa))
