import pygame as pg
import button


class App:

    def __init__(self):

        pg.init()

        # Settings window.
        self._width = 800
        self._height = 600
        self.window = pg.display.set_mode((self._width, self._height))
        self._caption = 'Ловкая кнопка' 
        pg.display.set_caption(self._caption)
        self._color_fon = (20, 20, 20)

        # Settings framerate.
        self._fps = 90
        self._clock = pg.time.Clock()

        # Create exemple button.
        self._button_1 = button.Button(self.window, (90, 30), (250, 20, 20))


    def _close(self):
        """Ends the program."""

        quit()

    
    def _check_events(self):
        """Check all events in the program."""

        # Closing by clicking on the cross.
        [self._close() for event in pg.event.get() if event.type == pg.QUIT]

        # Get all events keyboard.
        keys = pg.key.get_pressed()

        # Closing by key down ESCAPE.
        if keys[pg.K_ESCAPE]:
            self._close()

        # Check collision cursor with button.
        self._button_1.check_collision_cursor()

        
    def _draw(self):
        """Drawing all objects."""

        self.window.fill(self._color_fon)
        self._button_1.draw()
        pg.display.update()

    
    def main_loop(self):
        """Main loop App."""

        while True:
            self._check_events()
            self._draw()
            self._clock.tick(self._fps)