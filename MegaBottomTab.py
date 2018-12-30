
import curses


class MegaBottomTab:

    def __init__(self, window, id, title, pos_x, is_active = False):
        self.id = id
        self.title = title
        self.pos_x = pos_x
        self.window = window
        self.is_active = is_active

    def draw(self):
        if self.is_active:
            self.window.addstr(1, self.pos_x, " "+self.title[0][0:self.title[1]]+self.title[0]+" ", curses.A_REVERSE)
        else:
            self.window.addstr(1, self.pos_x, " "+self.title[0][0:self.title[1]], curses.A_NORMAL)
            self.window.addstr(self.title[0][self.title[1]], curses.A_UNDERLINE)
            self.window.addstr(self.title[0][self.title[1]+1:]+" ", curses.A_NORMAL)

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False