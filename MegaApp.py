
import curses
import curses.panel
from MegaTabBar import MegaTabBar


class MegaApp:

    def __init__(self, height, width, argv):
        self.window = curses.newwin(height, width, 0, 0)
        filenames = []
        if len(argv) > 1:
            filenames = argv[1:]
        else:
            filenames = [""]

        self.tabBar = MegaTabBar(filenames, self.window.getmaxyx()[1])



