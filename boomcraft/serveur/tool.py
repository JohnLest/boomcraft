import pickle


def serialize(obj) -> bytes:
    return pickle.dumps(obj)


def deserialize(msg: bytes):
    return pickle.loads(msg)


def first_or_default(_iter):
    return next(iter(_iter), None)


def get_key(_dict: dict, _value):
    for key, value in _dict.items():
        if value == _value:
            return key
    return None
