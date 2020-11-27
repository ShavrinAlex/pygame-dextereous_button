import pygame as pg


class App:

    def __init__(self):
        # Settings window.
        self.width = 800
        self.height = 600
        self.window = pg.display.set_mode((self.width, self.height))
        self.caption = 'Ловкая кнопка' 
        pg.display.set_caption(self.caption)
        self.color_fon = (20, 20, 20)

        # Settings framerate.
        self.fps = 60
        self.clock = pg.time.Clock()


    def close(self):
        """Ends the program."""

        quit()

    
    def check_events(self):
        """Check all events in the program."""

        # Closing by clicking on the cross.
        [self.close() for event in pg.event.get() if event.type == pg.QUIT]

        # Get all events keyboard.
        keys = pg.key.get_pressed()

        # Closing by key down ESCAPE.
        if keys[pg.K_ESCAPE]:
            self.close()

        
    def draw(self):
        """Drawing all objects."""

        self.window.fill(self.color_fon)


    def update_positions(self):
        """Update positions objects."""

        pass

    
    def main_loop(self):
        """Main loop App."""

        while True:
            self.check_events()
            self.update_positions()
            self.draw()
            self.clock.tick(self.fps)