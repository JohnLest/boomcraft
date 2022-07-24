import logging
from server import Server


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - class : %(name)s - %(message)s")
    logger = logging.getLogger(__name__)
    logger.debug(f"Start Boomcraft server")
    # serv = Server(host="192.168.1.55")
    serv = Server()
    serv.connect()

# region Test

# endregion

if __name__ == "__main__":
    main()
