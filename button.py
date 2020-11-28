import random
import pygame as pg


class Button:

    def __init__(self, window: object, size: tuple, color: tuple):
        """Initializes all settings button.

        Args:
            window (object): Surfaсe for button placement.
            size (tuple): Size button. (width, height)
            color (tuple): Color button. (R, G, B)
        """
        
        # Settings button.
        self._window = window
        self._width, self._height = size
        self._color = color
        self._pos_x = random.randrange(0, pg.display.get_window_size()[0] - self._width)
        self._pos_y = random.randrange(0, pg.display.get_window_size()[1] - self._height)

        # Create surface button.
        self._object = pg.Surface((self._width, self._height))
        self._object.fill(self._color)
        self._object_rect = self._object.get_rect(topleft=(self._pos_x, self._pos_y))

        # Create text.
        self.font = pg.font.SysFont(None, 24, True)
        self.text = self.font.render('Click me!', True, pg.Color('white'))
        self.text_rect = self.text.get_rect(center=(self._width//2, self._height//2))
        self._object.blit(self.text, self.text_rect)


    def draw(self):
        """Drawing button in coordinates self._pos_x, self._pos_y."""
        
        self._window.blit(self._object, self._object_rect)
       
    
    def check_collision_cursor(self):
        """Check collision cursor with button."""
        
        if self._object_rect.collidepoint(pg.mouse.get_pos()):
            self._set_position()

    
    def _set_position(self):
        """Change self._pos_x and self._pos_y."""

        self._object_rect.x = random.randrange(0, pg.display.get_window_size()[0] - self._width)
        self._object_rect.y = random.randrange(0, pg.display.get_window_size()[1] - self._height)
