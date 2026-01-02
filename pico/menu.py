import ws
import utime

ofs = 10
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
        for i,o in enumerate(self.options):
            y = sy*i + ofs
            if i==self.selected:
                ws.lcd.text("*", 5, y, hl)

            ws.lcd.text(o, 20, y, fg)

        ws.lcd.show()

    def up(self):
        self.selected -=1
        if self.selected < 0: self.selected = len(self.options) - 1
        self.show()

    def down(self):
        self.selected +=1
        if self.selected > len(self.options)-1: self.selected = 0
        self.show()

    def go(self):
        return self.selected


menu = Menu(["test", "hello", "gogo"])
menu.show()
choice = None

while True:
    utime.sleep(0.1)
    if ws.up.value()==0:
        menu.up()
    elif ws.down.value()==0:
        menu.down()
    elif ws.ctrl.value()==0:
        choice = menu.go()
        break


print("you chose " + str(choice))

import sys
sys.exit()
