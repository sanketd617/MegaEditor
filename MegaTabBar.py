
import curses
import curses.panel
from MegaTab import MegaTab


class MegaTabBar:

    def __init__(self, tab_titles, maxy, maxx):
        self.tabs = []
        self.tab_titles = [] + tab_titles
        self.window = curses.newwin(3, maxx)
        self.window.box()
        self.panel = curses.panel.new_panel(self.window)
        curses.panel.top_panel()
        self.index = 0
        self.pos_x = 1
        self.maxx = maxx
        self.maxy = maxy
        self.active_tab = 0

        self.setupTabs()

    def setupTabs(self):
        self.tabs = []
        self.pos_x = 1
        self.index = 0
        self.active_tab = 0
        for title in self.tab_titles:
            self.addTab(title, False, False)

    def draw(self):
        self.window.addstr(1, 0, " "*self.window.getmaxyx()[1])
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

        # work around for cases where tab isn't switched
        self.switchTo(next_index)

    def prevTab(self):
        prev_index = (self.active_tab + len(self.tabs) - 1) % len(self.tabs)
        self.switchTo(prev_index)

        # work around for cases where tab isn't switched
        self.switchTo(prev_index)

    def addTab(self, title = "untitled", concat_tab_titles = True, switch_to_new = True):
        if self.pos_x + len(title) + 3 > self.window.getmaxyx()[1]:
            return False
        if concat_tab_titles:
            self.tab_titles += [title]
        self.tabs += [MegaTab(self.maxy, self.maxx, self.window, self.index, title, self.pos_x)]
        self.pos_x = self.pos_x + len(title) + 3
        self.index += 1
        if switch_to_new:
            self.switchTo(self.index-1)
        else:
            self.switchTo(self.active_tab)

    def closeTab(self):
        if len(self.tab_titles) == 1:
            self.addTab("untitled", True, False)
            self.closeTab()
        else:

            del self.tab_titles[self.active_tab:self.active_tab+1]
            self.setupTabs()

            self.tabs[self.active_tab].activate()
            self.draw()

    def getActiveEditor(self):
        return self.tabs[self.active_tab].editor
