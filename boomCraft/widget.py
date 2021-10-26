import pygame
class Widget:
    @staticmethod
    def button(screen, text, position=(0, 0), rect: pygame.Rect = None):
        font = pygame.font.SysFont("Arial", 25)
        text_render = font.render(text, 1, (255, 0, 0))
        rectText = text_render.get_rect()
        if (rect is not None):
            x, y, w, h = btn = rect
            rectText.center = rect.center
        else :
            x, y, w, h = btn = rectText
            rectText.x, rectText.y = x, y = position

        pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
        pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
        pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
        screen.blit(text_render, (rectText.x, rectText.y))
        return btn
