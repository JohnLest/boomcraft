import pickle


def serialize(obj) -> bytes:
    return pickle.dumps(obj)


def deserialize(msg: bytes):
    return pickle.loads(msg)

