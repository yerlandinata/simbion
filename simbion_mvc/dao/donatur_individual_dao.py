import logging
from django.db import connection
from django.core.exceptions import EmptyResultSet
from simbion_mvc.entity import DonaturIndividual
from . import donatur_dao

LOGGER = logging.getLogger(__name__)

def get_by_nik(nik):
    cursor = connection.cursor()
    cursor.execute('SELECT nomor_identitas_donatur, nik\
                    FROM individual_donor WHERE nik = \'{}\''
                    .format(nik))
    result = cursor.fetchone()
    if result is None:
        raise EmptyResultSet('Individual donatur with nik \'{}\' does not exists'.format(nik))
    return DonaturIndividual(donatur_dao.get_by_id(result[0]), result[1])

def save(donatur_individual):
    insert_query = '''
    INSERT INTO individual_donor (nik, nomor_identitas_donatur)
    VALUES ('{}', '{}')
    '''.format(donatur_individual.getNik(), donatur_individual.getDonatur().getId())
    cursor = connection.cursor()
    LOGGER.debug('inserting {} into database...'.format(donatur_individual))
    cursor.execute(insert_query)
    LOGGER.debug('inserted {} into database!'.format(donatur_individual))
