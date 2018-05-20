import logging
from django.db import connection
from django.core.exceptions import EmptyResultSet
from simbion_mvc.entity.skema_beasiswa_aktif import SkemaBeasiswaAktif
from . import skema_beasiswa_aktif_dao

LOGGER = logging.getLogger(__name__)

def get_by_kode_and_noUrut(kode_skema_beasiswa,no_urut):
    cursor = connection.cursor()
    cursor.execute('SELECT kode_skema_beasiswa,no_urut,tgl_mulai_pendaftaran,\
                    tgl_tutup_pendaftaran,periode_penerimaan,status\
                    FROM SKEMA_BEASISWA_AKTIF\
                    WHERE kode_skema_beasiswa={} AND no_urut={}'.format(kode_skema_beasiswa, no_urut))
    result = cursor.fetchone()
    return result
    if result is None:
        raise EmptyResultSet('Beasiswa Aktif with kode \'{}\' and nomor urut \'{}\'does not exists'.format(kode_skema_beasiswa,no_urut))
    return SkemaBeasiwaAktif(skema_beasiswa_dao.getKode(result[0]), result[1], result[2], result[3], result[4],result[5])

def save(skema_beasiswa_aktif):
    insert_query = '''
    INSERT INTO skema_beasiswa_aktif (
        kode_skema_beasiswa,no_urut,tgl_mulai_pendaftaran,tgl_tutup_pendaftaran,periode_penerimaan,status) VALUES (
        '{}', '{}', '{}', '{}', '{}','{}'
    )
    '''.format(
        skema_beasiswa_aktif.getKodeSkemaBeasiswa(),
        skema_beasiswa_aktif.getNoUrut(),
        skema_beasiswa_aktif.getTglMulaiPendaftaran(),
        skema_beasiswa_aktif.getTglTutupPendaftaran(),
        skema_beasiswa_aktif.getPeriodePenerimaan(),
        skema_beasiswa_aktif.getStatus()
    )
    cursor = connection.cursor()
    LOGGER.debug('inserting {} into database...'.format(skema_beasiswa_aktif))
    cursor.execute(insert_query)
    LOGGER.debug('inserted {} into database!'.format(skema_beasiswa_aktif))
