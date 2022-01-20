from server import Server


def main():
    print(f"Hello server")
    serv = Server(host="192.168.0.100")
    serv.connect()
    print("coucou")

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

# endregion





if __name__ == "__main__":
    test_api()
    main()
