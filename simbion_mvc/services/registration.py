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
    
