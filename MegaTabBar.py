
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
        index = 0
        pos_x = 1

        for title in tab_titles:
            if title == "":
                title = "untitled"
            if pos_x + len(title) + 3 > maxx:
                break
            self.tabs.append(MegaTab(self.window, index, title, pos_x))
            pos_x = pos_x + len(title) + 3
            index += 1

        self.active_tab = 0
        self.switchTo(0)

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

