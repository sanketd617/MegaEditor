
import curses
import curses.panel
from MegaTab import MegaTab


class MegaTabBar:

    def __init__(self, tabs, maxx):
        self.tabs = []
        self.window = curses.newwin(3, maxx)
        self.window.box()

        self.panel = curses.panel.new_panel(self.window)
        curses.panel.top_panel()
        index = 0
        pos_x = 1
        is_first = True
        for text in tabs:
            self.tabs.append(MegaTab(self.window, index, text, pos_x, is_first))
            pos_x = pos_x + len(text) + 3
            index += 1
            is_first = False

        self.draw()

        curses.panel.update_panels()

    def draw(self):
        is_first = True
        pos_x = 1
        index = 0
        for tab in self.tabs:
            if not is_first:
                self.window.vline("|", 1)
            pos_x = pos_x + len(tab.title) + 2 + index
            is_first = False
            tab.draw()
            index += 1
        self.window.refresh()


