
import curses
import curses.panel

class MegaLineNums:

    def __init__(self, maxy, start = 1, n = 1):
        self.curr_line = 0
        self.maxx = 4
        self.window = curses.newwin(maxy, self.maxx, 3, 0)

        self.BG = 241
        self.FG = 236
        self.COLOR_PAIR = 2

        curses.use_default_colors()
        curses.init_pair(self.COLOR_PAIR, self.BG, self.FG)

        end = start + n - 1

        line_num = start

        while line_num <= end:
            self.window.addstr(self.curr_line, 0, (" "*(self.maxx - len(str(line_num)) - 1)) + str(line_num), curses.color_pair(self.COLOR_PAIR))
            line_num += 1
            self.curr_line += 1

        while line_num <= maxy:
            self.window.addstr(self.curr_line, 0, " "*(self.maxx-1), curses.color_pair(self.COLOR_PAIR))
            line_num += 1
            self.curr_line += 1

        self.window.refresh()

    def resize(self, y):
        self.window.resize(y, self.maxx)