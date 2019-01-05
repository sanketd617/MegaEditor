
import curses
import curses.panel
from MegaTabBar import MegaTabBar
from MegaLineNums import MegaLineNums
from MegaBottomPanel import MegaBottomPanel


class MegaApp:

    def __init__(self, height, width, argv):
        self.window = curses.newwin(height, width, 0, 0)
        self.filenames = []
        if len(argv) > 1:
            self.filenames = argv[1:]
        else:
            self.filenames = ["untitled"]

        options = [["new", 0], ["open", 0], ["write", 0], ["exit", 0]]

        self.tabBar = MegaTabBar(self.filenames, self.window.getmaxyx()[0], self.window.getmaxyx()[1])
        self.lineNums = MegaLineNums(height-4, 1, 1)
        self.bottomPanel = MegaBottomPanel(options, height, width)

    def addLine(self):
        self.lineNums.add()

    def resize(self, y, x):
        self.window = curses.newwin(y, x, 0, 0)

        options = [["new", 0], ["open", 0], ["write", 0], ["exit", 0]]

        all_lines = []

        for tab in self.tabBar.tabs:
            all_lines.append(tab.editor.lines)

        tab_titles = self.tabBar.tab_titles
        active_tab = self.tabBar.active_tab

        self.tabBar = MegaTabBar(tab_titles, self.window.getmaxyx()[0], self.window.getmaxyx()[1])
        self.lineNums = MegaLineNums(y-4, 1)
        self.bottomPanel = MegaBottomPanel(options, y, x)

        j = 0
        for tab in self.tabBar.tabs:
            tab.editor.lines = all_lines[j]
            j += 1
            tab.editor.write_lines()

        self.tabBar.switchTo(active_tab)
        self.tabBar.tabs[self.tabBar.active_tab].editor_panel.top()

        self.tabBar.draw()