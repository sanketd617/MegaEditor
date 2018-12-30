
import curses
import curses.panel

class MegaLineNums:

    def __init__(self, maxy, n = 1):
        self.num_lines = n
        self.window = curses.newwin(maxy, 3, 3, 0)

        self.BG = 241
        self.FG = 236
        self.COLOR_PAIR = 2

        curses.use_default_colors()
        curses.init_pair(self.COLOR_PAIR, self.BG, self.FG)

        for i in range(1, self.num_lines+1):
            self.window.addstr((" "*(3-len(str(i))))+str(i), curses.color_pair(self.COLOR_PAIR))

        for i in range(self.num_lines+1, maxy):
            self.window.addstr("   ", curses.color_pair(2))

        self.window.refresh()

    def add(self):
        self.num_lines += 1
        self.window.addstr((" "*(3-len(str(self.num_lines))))+str(self.num_lines), curses.color_pair(self.COLOR_PAIR))