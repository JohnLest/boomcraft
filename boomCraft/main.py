import pygame
from mainWindow import MainWindow

def main():
    pygame.init()
    mainWin = MainWindow()
    btn = mainWin.button(mainWin.mainWindow, "API", rect=mainWin.gbMenuButton)

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn.collidepoint(pygame.mouse.get_pos()):
                    print("API")
        pygame.display.update()
    pygame.quit()
    return

if __name__ == "__main__":
    main()
