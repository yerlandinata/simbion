import logging
from django.db import connection
from django.core.exceptions import EmptyResultSet
from simbion_mvc.entity.syarat_beasiswa import SyaratBeasiswa 
from . import skema_beasiswa_dao

LOGGER = logging.getLogger(__name__)

def get_by_kode(kode_beasiswa):
    cursor = connection.cursor()
    cursor.execute('SELECT kode_beasiswa,syarat\
                    FROM SYARAT_BEASISWA SB, SKEMA_BEASISWA SSB\
                    WHERE SB.kode_beasiswa=SSB.kode AND SB.kode_beasiswa={}'.format(kode_beasiswa))
    result = cursor.fetchone()
    if result is None:
        raise EmptyResultSet('Beasiswa with kode \'{}\' does not exists'.format(kode_beasiswa))
    return SyaratBeasiswa(skema_beasiswa_dao.get_by_kode(result[0]), result[1])

def save(syarat_beasiswa):
    insert_query = '''
    INSERT INTO syarat_beasiswa (
        kode_beasiswa, syarat) VALUES (
        '{}', '{}'
    )
    '''.format(
        syarat_beasiswa.getSkemaBeasiswa().getKode(),
        syarat_beasiswa.getSyarat()
        )
    cursor = connection.cursor()
    LOGGER.debug('inserting {} into database...'.format(syarat_beasiswa))
    cursor.execute(insert_query)
    LOGGER.debug('inserted {} into database!'.format(syarat_beasiswa))
