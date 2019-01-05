# -*- coding: utf-8 -*-

import curses
import curses.panel
from MegaBottomTab import MegaBottomTab

class MegaBottomPanel:

    def __init__(self, options, maxy, maxx):
        self.maxx = maxx
        self.window = curses.newwin(3, maxx, maxy - 3, 0)
        self.window.box()
        self.options = options
        self.tabs = []
        self.setupTabs()
        self.window.refresh()

    def resize(self, x):
        self.window.resize(3, x)

    def printLineNo(self, y, x):
        self.window.addstr(1, self.maxx - len(str(x)+str(y)) - 3, str(y)+","+str(x))
        self.window.refresh()

    def setupTabs(self):
        pos_x = 1
        index = 0
        for option in self.options:
            if index != 0:
                pos_x += 3
            self.tabs += [MegaBottomTab(self.window, index, option, pos_x)]
            self.tabs[index].draw()
            pos_x = pos_x + len(option) + 1
            index += 1