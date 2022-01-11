import pickle


def serialize(obj) -> bytes:
    return pickle.dumps(obj)


def deserialize(msg: bytes):
    return pickle.loads(msg)


def first_or_default(_iter):
    return next(iter(_iter), None)
