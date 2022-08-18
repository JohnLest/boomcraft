import pickle
import logging

logger = logging.getLogger(__name__)


def serialize(obj) -> bytes:
    try:
        return pickle.dumps(obj)
    except Exception as ex:
        logger.error(f"Exception in serialize() : {ex.args[0]}")
        logger.error(f"Exception with message {obj}")
        return b''


def deserialize(msg: bytes):
    try:
        return pickle.loads(msg)
    except Exception as ex:
        logger.error(f"Exception in deserialize() : {ex.args[0]}")
        logger.error(f"Exception with message {msg}")
        return None


def first_or_default(_iter):
    return next(iter(_iter), None)


def get_key(_dict: dict, _value):
    for key, value in _dict.items():
        if value == _value:
            return key
    return None
