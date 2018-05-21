import logging
from simbion_mvc.dao import user_dao, mahasiswa_dao, donatur_dao, donatur_yayasan_dao, donatur_individual_dao
from django.db import DataError, IntegrityError

logger = logging.getLogger(__name__)

class InvalidRegistrationException(Exception):
    pass

def register_mahasiswa(mahasiswa):
    logger.debug('attempting to register mahasiswa:' + str(mahasiswa))
    if not mahasiswa.isValid():
        raise InvalidRegistrationException()
    register_user(mahasiswa.getUser())
    try:
        mahasiswa_dao.save(mahasiswa)
    except (DataError, IntegrityError) as e:
        logger.debug(str(e))
        logger.debug('mahasiswa registration error: username already exists')
        raise InvalidRegistrationException()
    logger.debug('mahasiswa registration successful!')

def register_donatur_individual(donatur_individual):
    logger.debug('attempting to register donatur individual:' + str(donatur_individual))
    if not donatur_individual.isValid():
        raise InvalidRegistrationException()
    register_donatur(donatur_individual.getDonatur())
    try:
        donatur_individual_dao.save(donatur_individual)
    except (DataError, IntegrityError) as e:
        logger.debug(str(e))
        logger.debug('donatur individual registration error: donatur nik already exists')
        raise InvalidRegistrationException()
    logger.debug('donatur individual registration successful!')

def register_donatur(donatur):
    logger.debug('attempting to register donatur:' + str(donatur))
    if not donatur.isValid():
        raise InvalidRegistrationException()
    register_user(donatur.getUser())
    try:
        donatur_dao.save(donatur)
    except (DataError, IntegrityError) as e:
        logger.debug(str(e))
        logger.debug('donatur registration error: donatur id already exists')
        raise InvalidRegistrationException()
    logger.debug('donatur registration successful!')

def register_user(user):
    logger.debug('attempting to register user:' + str(user))
    if not user.isValid():
        raise InvalidRegistrationException()
    try:
        user_dao.save(user)
    except (DataError, IntegrityError) as e:
        logger.debug(str(e))
        logger.debug('user registration error: username already exists')
        raise InvalidRegistrationException()
    logger.debug('user registration successful!')
    