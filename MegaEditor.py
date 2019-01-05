
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
        self.file = file
        self.start_y = 0
        self.line_index = 0

    def resize(self, y, x):
        self.window.resize(y, x)

    def write(self, c):
        self.line_index = self.start_y + self.curr_y
        if ord(c) == 10:
            part_one = self.lines[self.line_index][:self.curr_x]
            part_two = self.lines[self.line_index][self.curr_x:]
            self.lines = self.lines[:self.line_index+1] + [part_two] + self.lines[self.line_index+1:]
            self.lines[self.line_index] = part_one
            self.curr_x = 0
            if self.curr_y < self.maxy-1:
                self.curr_y += 1
            else:
                self.start_y += 1
        else:
            if ord(c) == 9:
                self.lines[self.line_index] = self.lines[self.line_index][:self.curr_x] + "    " + self.lines[self.line_index][self.curr_x:]
                self.curr_x += 4
            else:
                self.lines[self.line_index] = self.lines[self.line_index][:self.curr_x] + c + self.lines[self.line_index][self.curr_x:]
                self.curr_x += 1

        self.write_lines()
        self.window.refresh()

    def write_lines(self):
        ty = 0
        self.window.clear()
        end_y = self.start_y + self.maxy
        if end_y > len(self.lines):
            end_y = len(self.lines)
        lines = self.lines[self.start_y:end_y]
        for line in lines:
            self.window.addstr(ty, 0, line)
            ty += 1

        self.window.move(self.curr_y, self.curr_x)
        self.window.refresh()

    def backspace(self):
        self.line_index = self.start_y + self.curr_y
        if self.curr_x == 0 and self.line_index != 0:
            part_one = self.lines[self.line_index-1]
            part_two = self.lines[self.line_index]
            self.lines = self.lines[:self.line_index] + self.lines[self.line_index+1:]
            self.lines[self.line_index-1] = part_one + part_two
            if self.curr_y > 0:
                self.curr_y -= 1
            else:
                self.start_y -= 1
            self.curr_x = len(part_one)
        elif self.curr_x == 0 and self.line_index == 0:
            return False
        elif self.curr_x == len(self.lines[self.line_index]):
            self.curr_x -= 1
            self.lines[self.line_index] = self.lines[self.line_index][:self.curr_x]
        else:
            self.curr_x -= 1
            temp = self.lines[self.line_index]
            part_one = temp[:self.curr_x]
            part_two = temp[self.curr_x+1:]
            self.lines[self.line_index] = part_one + part_two

        self.write_lines()

    def delete(self):
        self.line_index = self.start_y + self.curr_y
        if self.line_index == len(self.lines[self.line_index]) and self.line_index != len(self.lines)-1:
            part_one = self.lines[self.line_index]
            part_two = self.lines[self.line_index+1]
            self.lines = self.lines[:self.line_index] + self.lines[self.line_index+1:]
            self.lines[self.line_index] = part_one + part_two
            self.curr_x = len(part_one)
        elif self.curr_x == len(self.lines[self.line_index]) and self.line_index == len(self.lines)-1:
            return False
        # elif self.curr_x == 0:
        #     self.lines[self.curr_y] = self.lines[self.curr_y][:self.curr_x]
        else:
            temp = self.lines[self.line_index]
            part_one = temp[:self.curr_x]
            part_two = temp[self.curr_x+1:]
            self.lines[self.line_index] = part_one + part_two

        self.write_lines()

    def moveLeft(self):
        self.line_index = self.start_y + self.curr_y
        if self.curr_x == 0:
            if self.line_index == 0:
                return False
            else:
                if self.curr_y > 0:
                    self.curr_y -= 1
                else:
                    self.start_y -= 1
                self.line_index = self.start_y + self.curr_y
                self.curr_x = len(self.lines[self.line_index])
        else:
            self.curr_x -= 1

        self.write_lines()

    def moveRight(self):
        self.line_index = self.start_y + self.curr_y
        if self.curr_x == len(self.lines[self.line_index]):
            if self.line_index == len(self.lines)-1:
                return False
            else:
                if self.curr_y < self.maxy - 1:
                    self.curr_y += 1
                else:
                    self.start_y += 1
                self.curr_x = 0
        else:
            self.curr_x += 1

        self.write_lines()

    def moveUp(self):
        self.line_index = self.start_y + self.curr_y
        if self.line_index <= 0:
            return False

        if self.curr_y > 0:
            self.curr_y -= 1
        else:
            self.start_y -= 1

        if self.curr_x > len(self.lines[self.line_index-1]):
            self.curr_x = len(self.lines[self.line_index-1])

        self.write_lines()

    def moveDown(self):
        self.line_index = self.start_y + self.curr_y
        if self.line_index == len(self.lines)-1:
            return False
        if self.curr_y < self.maxy-1:
            self.curr_y += 1
        else:
            self.start_y += 1
        if self.curr_x > len(self.lines[self.line_index]):
            self.curr_x = len(self.lines[self.line_index])
        self.write_lines()

    def save(self):
        file = open(self.file, "w+")
        for line in self.lines:
            file.write(line+"\r\n")

        file.close()
