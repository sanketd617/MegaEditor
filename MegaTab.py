
import curses

from MegaEditor import MegaEditor


class MegaTab:

    def __init__(self, maxy, maxx, window, id, title, pos_x, is_active = False):
        self.id = id
        index = title.rfind("/")
        if index == -1:
            self.title = title
        else:
            self.title = title[index+1:]
        self.pos_x = pos_x
        self.maxy = maxy
        self.maxx = maxx
        self.window = window
        self.is_active = is_active
        self.editor = MegaEditor(id, self.maxy-6, self.maxx-2, title)
        self.editor_panel = curses.panel.new_panel(self.editor.window)
        self.is_dirty = False

    def draw(self):
        if self.is_active:
            if self.is_dirty:
                self.window.addstr(1, self.pos_x, ""+self.title+"* ", curses.A_REVERSE)
            else:
                self.window.addstr(1, self.pos_x, " "+self.title+" ", curses.A_REVERSE)
        else:
            if self.is_dirty:
                self.window.addstr(1, self.pos_x, ""+self.title+"* ", curses.A_NORMAL)
            else:
                self.window.addstr(1, self.pos_x, " "+self.title+" ", curses.A_NORMAL)

    def activate(self):
        self.is_active = True
        self.editor_panel.top()

    def deactivate(self):
        self.is_active = False
