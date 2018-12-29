
import curses
import curses.panel
from MegaTab import MegaTab


class MegaTabBar:

    def __init__(self, tab_titles, maxx):
        self.tabs = []
        self.window = curses.newwin(3, maxx)
        self.window.box()

        self.panel = curses.panel.new_panel(self.window)
        curses.panel.top_panel()
        self.index = 0
        self.pos_x = 1

        self.active_tab = 0

        for title in tab_titles:
            self.addTab(title)

        self.draw()

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
        curses.panel.update_panels()

    def switchTo(self, tab_index):
        self.tabs[self.active_tab].deactivate()
        self.active_tab = tab_index
        self.tabs[self.active_tab].activate()
        self.draw()

    def nextTab(self):
        next_index = (self.active_tab + 1) % len(self.tabs)
        self.switchTo(next_index)

    def prevTab(self):
        prev_index = (self.active_tab + len(self.tabs) - 1) % len(self.tabs)
        self.switchTo(prev_index)

    def addTab(self, title = "untitled"):

        if self.pos_x + len(title) + 3 > self.window.getmaxyx()[1]:
            return False
        self.tabs.append(MegaTab(self.window, self.index, title, self.pos_x))
        self.pos_x = self.pos_x + len(title) + 3
        self.index += 1
        self.switchTo(self.index-1)