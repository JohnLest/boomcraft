import logging

# import pygame
from importWindow import ImportWindow

from farmvillageApi import FarmVillageApi

def main() :

    potions = farmvillage_api()

    # pygame.init()

    importWin = ImportWindow(potions)

    # pygame.quit()
    
def farmvillage_api():
    print("Hello Farm Village")
    fv_api = FarmVillageApi()
    potions = fv_api.get_potions()
    print("--------------- Farm Village------------------------")
    print(potions)
    return potions
    print("---------------END Farm Village----------------------")


if __name__ == "__main__":

    main()
