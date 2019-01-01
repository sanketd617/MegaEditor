
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

    def write(self, c):
        if ord(c) == 10:
            part_one = self.lines[self.curr_y][:self.curr_x]
            part_two = self.lines[self.curr_y][self.curr_x:]
            self.lines = self.lines[:self.curr_y+1] + [part_two] + self.lines[self.curr_y+1:]
            self.lines[self.curr_y] = part_one
            self.curr_x = 0
            self.curr_y += 1
        else:
            self.lines[self.curr_y] = self.lines[self.curr_y][:self.curr_x] + c + self.lines[self.curr_y][self.curr_x:]
            self.curr_x += 1

        self.write_lines()
        self.window.refresh()

    def write_lines(self):
        ty = 0
        self.window.clear()
        for line in self.lines:
            self.window.addstr(ty, 0, line)
            ty += 1

        self.window.move(self.curr_y, self.curr_x)
        self.window.refresh()

    def backspace(self):
        if self.curr_x == 0 and self.curr_y != 0:
            part_one = self.lines[self.curr_y-1]
            part_two = self.lines[self.curr_y]
            self.lines = self.lines[:self.curr_y] + self.lines[self.curr_y+1:]
            self.lines[self.curr_y-1] = part_one + part_two
            self.curr_y -= 1
            self.curr_x = len(part_one)
        elif self.curr_x == 0 and self.curr_y == 0:
            return False
        elif self.curr_x == len(self.lines[self.curr_y]):
            self.curr_x -= 1
            self.lines[self.curr_y] = self.lines[self.curr_y][:self.curr_x]
        else:
            self.curr_x -= 1
            temp = self.lines[self.curr_y]
            part_one = temp[:self.curr_x]
            part_two = temp[self.curr_x+1:]
            self.lines[self.curr_y] = part_one + part_two

        self.write_lines()

    def delete(self):
        if self.curr_x == len(self.lines[self.curr_y]) and self.curr_y != len(self.lines)-1:
            part_one = self.lines[self.curr_y]
            part_two = self.lines[self.curr_y+1]
            self.lines = self.lines[:self.curr_y] + self.lines[self.curr_y+1:]
            self.lines[self.curr_y] = part_one + part_two
            self.curr_x = len(part_one)
        elif self.curr_x == len(self.lines[self.curr_y]) and self.curr_y == len(self.lines)-1:
            return False
        elif self.curr_x == 0:
            self.lines[self.curr_y] = self.lines[self.curr_y][:self.curr_x]
        else:
            temp = self.lines[self.curr_y]
            part_one = temp[:self.curr_x]
            part_two = temp[self.curr_x+1:]
            self.lines[self.curr_y] = part_one + part_two

        self.write_lines()

    def moveLeft(self):
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
        if self.curr_y == 0:
            return False
        self.curr_y -= 1
        if self.curr_x > len(self.lines[self.curr_y-1]):
            self.curr_x = len(self.lines[self.curr_y-1])
        self.window.move(self.curr_y, self.curr_x)
        self.window.refresh()

    def moveDown(self):
        if self.curr_y == len(self.lines)-1:
            return False
        self.curr_y += 1
        if self.curr_x > len(self.lines[self.curr_y]):
            self.curr_x = len(self.lines[self.curr_y])
        self.window.move(self.curr_y, self.curr_x)
        self.window.refresh()