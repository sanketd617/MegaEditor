
import curses
import curses.panel
from MegaTabBar import MegaTabBar

class MegaApp:

    def __init__(self, height, width):
        self.window = curses.newwin(height, width, 0, 0)
        tabs = ["untitled", "new tab", "another tab", "Hehheheeheheh"]
        self.tabBar = MegaTabBar(tabs, self.window.getmaxyx()[1])



