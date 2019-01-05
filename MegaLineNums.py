
import curses
import curses.panel

class MegaLineNums:

    def __init__(self, maxy, start = 1, end = 1):
        self.num_lines = start-1
        self.window = curses.newwin(maxy, 3, 3, 0)

        self.BG = 241
        self.FG = 236
        self.COLOR_PAIR = 2

        curses.use_default_colors()
        curses.init_pair(self.COLOR_PAIR, self.BG, self.FG)

        t = min(start + end, maxy)

        for i in range(start, t):
            self.num_lines += 1
            self.window.addstr((i-start), 0, (" "*(3-len(str(self.num_lines))))+str(self.num_lines), curses.color_pair(self.COLOR_PAIR))

        for i in range(self.num_lines+1, maxy):
            self.window.addstr("   ", curses.color_pair(2))

        self.window.refresh()

    def resize(self, y):
        self.window.resize(y, 3)

    def add(self):
        self.num_lines += 1
        self.window.addstr((" "*(3-len(str(self.num_lines))))+str(self.num_lines), curses.color_pair(self.COLOR_PAIR))