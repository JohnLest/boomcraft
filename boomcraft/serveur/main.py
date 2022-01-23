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
from otherApi import OtherApi

def test_api():
    print(f"Hello API")
    uri = "http://dataservice.accuweather.com/currentconditions/v1/"
    weather_api = OtherApi(uri)
    weather = weather_api.get_request("27581?apikey=NM6IwoED21vbDTI6Fc7gosRt9A5rqNTu")
    print(weather)
    uri2 = "https://nominis.cef.fr/json"
    saint_api = OtherApi(uri2)
    saint = saint_api.get_request("saintdujour.php")
    print(saint)



from veggiecrushApi import VeggieCrushApi

def veggiecrush_api():
    print("Hello Veggie Crush")
    vc_api = VeggieCrushApi()
    potions = vc_api.get_potions()
    print("--------------- Veggie Crush------------------------")
    print(potions)
    print("---------------END Veggie Crush----------------------")

from farmvillageApi import FarmVillageApi

def farmvillage_api():
    print("Hello Farm Village")
    fv_api = FarmVillageApi()
    potions = fv_api.get_potions()
    print("--------------- Farm Village------------------------")
    print(potions)
    print("---------------END Farm Village----------------------")
# endregion

if __name__ == "__main__":
    # test_api()
    # veggiecrush_api()
    # farmvillage_api()
    main()
