import ws
import utime

sy = 10
bg = ws.colour(0,0,50)
hl = ws.colour(255,255,100)
fg = ws.colour(150,150,250)

class Menu():
    def __init__(self, options):
        self.options = options
        self.selected = 0

    def show(self):
        ws.clear(bg)
        for o,i in enumerate(options):
            y = sy*i + ofs
            if i==selected:
                ws.lcd.text("*", 5, y, hl)

            ws.lcd.text(o, 20, y, fg)

    def up(self):
        self.selected -=1
        if self.selected < 0: self.selected = len(self.options) - 1

    def down(self):
        self.selected +=1
        if self.selected > len(self.options)-1: self.selected = 0

    def go(self):
        return self.selected





