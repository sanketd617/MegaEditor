
import curses
import curses.panel
from MegaTabBar import MegaTabBar
from MegaLineNums import MegaLineNums
from MegaBottomPanel import MegaBottomPanel


class MegaApp:

    def __init__(self, height, width, argv):
        self.window = curses.newwin(height, width, 0, 0)
        filenames = []
        if len(argv) > 1:
            filenames = argv[1:]
        else:
            filenames = ["untitled"]

        options = [["new", 0], ["open", 0], ["write", 0], ["exit", 0]]

        self.tabBar = MegaTabBar(filenames, self.window.getmaxyx()[0], self.window.getmaxyx()[1])
        self.lineNums = MegaLineNums(height-4, 1)
        self.bottomPanel = MegaBottomPanel(options, height, width)

    def addLine(self):
        self.lineNums.add()


