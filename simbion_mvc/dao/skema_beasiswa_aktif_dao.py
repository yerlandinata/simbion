import logging
from django.db import connection
from django.core.exceptions import EmptyResultSet
from simbion_mvc.entity import SkemaBeasiswaAktif
from . import skema_beasiswa_dao

LOGGER = logging.getLogger(__name__)

def get_by_skema_beasiswa_and_no_urut(skema_beasiswa,no_urut):
    cursor = connection.cursor()
    cursor.execute('SELECT kode_skema_beasiswa,no_urut,tgl_mulai_pendaftaran,\
                    tgl_tutup_pendaftaran,periode_penerimaan,status,jumlah_pendaftar\
                    FROM skema_beasiswa_aktif\
                    WHERE kode_skema_beasiswa={} AND no_urut={}'.format(skema_beasiswa.getKode(), no_urut))
    result = cursor.fetchone()
    if result is None:
        raise EmptyResultSet('Skema Beasiswa Aktif with skema \'{}\' and nomor urut \'{}\'does not exists'.format(skema_beasiswa,no_urut))
    return SkemaBeasiswaAktif(skema_beasiswa_dao.get_by_kode(result[0]), result[1], result[2], result[3], result[4], result[5], result[6])

def save(skema_beasiswa_aktif):
    insert_query = '''
    INSERT INTO skema_beasiswa_aktif (
        kode_skema_beasiswa,no_urut,tgl_mulai_pendaftaran,tgl_tutup_pendaftaran,periode_penerimaan,status,jumlah_pendaftar) VALUES (
        '{}', '{}', '{}', '{}', '{}','{}','{}'
    )
    '''.format(
        skema_beasiswa_aktif.getSkemaBeasiswa().getKode(),
        skema_beasiswa_aktif.getNoUrut(),
        skema_beasiswa_aktif.getTglMulaiPendaftaran(),
        skema_beasiswa_aktif.getTglTutupPendaftaran(),
        skema_beasiswa_aktif.getPeriodePenerimaan(),
        skema_beasiswa_aktif.getStatus(),
        skema_beasiswa_aktif.getJumlahPendaftar()
    )
    cursor = connection.cursor()
    LOGGER.debug('inserting {} into database...'.format(skema_beasiswa_aktif))
    cursor.execute(insert_query)
    LOGGER.debug('inserted {} into database!'.format(skema_beasiswa_aktif))
