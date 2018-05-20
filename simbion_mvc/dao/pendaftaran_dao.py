import logging
from  django.db import connection
from django.core.exceptions import EmptyResultSet
from simbion_mvc.entity import Pendaftaran
from . import skema_beasiswa_aktif_dao
from . import mahasiswa_dao
from . import skema_beasiswa_dao

LOGGER = logging.getLogger(__name__)

def get_by_skema_beasiswa_and_no_urut(skema_beasiswa_aktif):
    cursor = connection.cursor()
    cursor.execute('SELECT no_urut,kode_skema_beasiswa,npm,waktu_daftar,status_daftar,status_terima\
                   FROM PENDAFTARAN\
                   WHERE no_urut = {} AND kode_skema_beasiswa = {}'.format(skema_beasiswa_aktif.getNoUrut(),skema_beasiswa_aktif.getSkemaBeasiswa().getKode()))
    result = cursor.fetchone()
    if result is None:
        raise EmptyResultSet('Pendaftaran with no urut \'{}\' and kode \'{}\' and  does not exists'.format(skema_beasiswa_aktif.getNoUrut(),
                                                                                                           skema_beasiswa_aktif.getSkemaBeasiswa().getkode()))
    return Pendaftaran(skema_beasiswa_aktif_dao.get_by_skema_beasiswa_and_no_urut(skema_beasiswa_dao.get_by_kode(result[1]),result[0]),mahasiswa_dao.get_by_npm(result[2]),result[3],
                       result[4],result[5])
def get_by_npm(mahasiswa):
    cursor = connection.cursor()
    cursor.execute('SELECT no_urut,kode_skema_beasiswa,npm,waktu_daftar,status_daftar,status_terima\
                       FROM PENDAFTARAN\
                       WHERE npm = \'{}\''.format(mahasiswa.getNpm()))
    result = cursor.fetchone()
    if result is None:
        raise EmptyResultSet('Pendaftaran with npm \'{}\' does not exists'.format(mahasiswa.getNpm()))
    return Pendaftaran(skema_beasiswa_aktif_dao.get_by_skema_beasiswa_and_no_urut(skema_beasiswa_dao.get_by_kode(result[1]), result[0]),
                       mahasiswa_dao.get_by_npm(result[2]), result[3],
                       result[4], result[5])

def save(pendaftaran):
    insert_query = '''
    INSERT INTO PENDAFTARAN(no_urut,kode_skema_beasiswa,npm,waktu_daftar,status_daftar,status_terima) VALUES (
    '{}','{}','{}','{}','{}','{}'
    )
    '''.format(pendaftaran.getNoUrut(),pendaftaran.getKodeSkemaBeasiswa(),pendaftaran.getNPM(),
               pendaftaran.getWaktuDaftar(),pendaftaran.getStatusDaftar(),pendaftaran.getStatusTerima())
    cursor = connection.cursor()
    LOGGER.debug('inserting {} into database...'.format(pendaftaran))
    cursor.execute(insert_query)
    LOGGER.debug('inserted {} into database!'.format(pendaftaran))