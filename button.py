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
        self._set_position()

        # Create surface button.
        self._object = pg.Surface((self._width, self._height))
        self._object.fill(self._color)


    def draw(self):
        """Drawing button in coordinates self._pos_x, self._pos_y."""

        self._window.blit(self._object, (self._pos_x, self._pos_y))
        
    
    def check_collision_cursor(self):
        """Check collision cursor with button."""

        mouse_x, mouse_y = pg.mouse.get_pos()
        if mouse_x >= self._pos_x and mouse_x <= self._pos_x + self._width:
            if mouse_y >= self._pos_y and mouse_y <= self._pos_y + self._height:
                self._set_position()

    
    def _set_position(self):
        """Change self._pos_x and self._pos_y."""

        self._pos_x = random.randrange(0, pg.display.get_window_size()[0] - self._width)
        self._pos_y = random.randrange(0, pg.display.get_window_size()[1] - self._height)
