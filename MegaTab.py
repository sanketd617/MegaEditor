
import curses


class MegaTab:

    def __init__(self, window, id, filename, pos_x, is_active = False):
        self.id = id
        self.title = filename
        self.pos_x = pos_x
        self.window = window
        self.is_active = is_active

    def draw(self):
        if self.is_active:
            self.window.addstr(1, self.pos_x, " "+self.title+" ", curses.A_REVERSE)
        else:
            self.window.addstr(1, self.pos_x, " "+self.title+" ", curses.A_NORMAL)
