
import curses
import curses.panel

class MegaEditor:

    def __init__(self, id, maxy, maxx, file):
        self.id = id
        self.curr_y = 0
        self.curr_x = 0
        self.maxx = maxx
        self.maxy = maxy
        self.window = curses.newwin(maxy, maxx, 3, 4)
        self.window.refresh()
        self.lines = [""]

    def setCursorPos(self):
        self.curr_y, self.curr_x = self.window.getyx()

    def write(self, c):
        self.setCursorPos()

        if ord(c) == 10:
            part_one = self.lines[self.curr_y][:self.curr_x]
            part_two = self.lines[self.curr_y][self.curr_x:]
            self.lines = self.lines[:self.curr_y+1] + [part_two] + self.lines[self.curr_y+1:]
            self.lines[self.curr_y] = part_one
            self.window.addstr(self.curr_y, 0, part_one + (" "*len(part_two)))
            self.window.move(self.curr_y+1, 0)
            self.window.insertln()
            self.window.addstr(part_two)
            self.curr_y += 1
            self.curr_x = 0
        else:
            self.window.addstr(c)
            self.curr_x += 1
            self.lines[self.curr_y] += c
        self.window.move(self.curr_y, self.curr_x)

        self.window.refresh()

    def backspace(self):
        self.setCursorPos()

        if self.curr_x == 0 and self.curr_y != 0:
            part_one = self.lines[self.curr_y-1]
            part_two = self.lines[self.curr_y]
            self.lines = self.lines[:self.curr_y] + self.lines[self.curr_y+1:]
            self.lines[self.curr_y-1] = part_one + part_two
            self.window.addstr(self.curr_y-1, 0, part_one + part_two)
            self.window.move(self.curr_y, 0)
            self.window.deleteln()
            self.curr_y -= 1
            self.curr_x = len(part_one)
        elif self.curr_y != 0:
            self.curr_x -= 1
            self.window.delch(self.curr_y, self.curr_x)
            self.lines[self.curr_y] += self.lines[self.curr_y][:self.curr_x]+self.lines[self.curr_y][self.curr_x+1:]
        self.window.move(self.curr_y, self.curr_x)

        self.window.refresh()

    def delete(self):

        self.window.refresh()

    def moveLeft(self):
        self.setCursorPos()

        if self.curr_x == 0:
            if self.curr_y == 0:
                return False
            else:
                self.curr_y -= 1
                self.curr_x = len(self.lines[self.curr_y])
        else:
            self.curr_x -= 1
        self.window.move(self.curr_y, self.curr_x)
        self.window.refresh()

    def moveRight(self):
        self.setCursorPos()

        if self.curr_x == len(self.lines[self.curr_y]):
            if self.curr_y == len(self.lines)-1:
                return False
            else:
                self.curr_y += 1
                self.curr_x = 0
        else:
            self.curr_x += 1
        self.window.move(self.curr_y, self.curr_x)
        self.window.refresh()

    def moveUp(self):
        self.setCursorPos()

        if self.curr_y == 0:
            return False
        self.curr_y -= 1
        if self.curr_x > len(self.lines[self.curr_y-1]):
            self.curr_x = len(self.lines[self.curr_y-1])
        self.window.move(self.curr_y, self.curr_x)
        self.window.refresh()

    def moveDown(self):
        self.setCursorPos()

        if self.curr_y == len(self.lines)-1:
            return False
        self.curr_y += 1
        if self.curr_x > len(self.lines[self.curr_y]):
            self.curr_x = len(self.lines[self.curr_y])
        self.window.move(self.curr_y, self.curr_x)
        self.window.refresh()