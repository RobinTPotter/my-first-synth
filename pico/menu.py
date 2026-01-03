
import ws
import utime
from ws import lcd, colour
import FONTS as f

menu = None
last = None

db = 0.3
ofs = 10
sy = 20
sz = 3
bg = ws.colour(0,0,50)
hl = ws.colour(255,255,100)
fg = ws.colour(150,150,250)

class Menu():
    def __init__(self, options, callback=None):
        self.options = options
        self.selected = 0
        self.callback = callback

    def show(self):
        ws.clear(bg)
        for i,o in enumerate(self.options):
            y = sy*i + ofs
            if i==self.selected:
                #ws.lcd.text("*", 5, y, hl)
                f.prnt_st("*", 5, y, sz, 200, 200, 0) #asci,xx,yy,sz,r,g,b)
            # ws.lcd.text(o, 20, y, fg)
            f.prnt_st(o, 20, y, sz, 200,200,250)

        ws.lcd.show()

    def up(self):
        self.selected -=1
        if self.selected < 0: self.selected = len(self.options) - 1
        self.show()
        utime.sleep(db)

    def left(self):
        if self.callback: self.callback((None,None))
        utime.sleep(db)

    def down(self):
        self.selected +=1
        if self.selected > len(self.options)-1: self.selected = 0
        self.show()
        utime.sleep(db)

    def go(self):
        if self.callback: self.callback((self.selected, self.options[self.selected]))
        utime.sleep(db)
        return self.selected

def hello(data):
    i, o = data
    print(data)
    if o==None:
        global menu, last
        menu = last
        menu.show()
    elif o=="test":
        ws.clear(ws.colour(250,250,80))
        ws.lcd.show()
        utime.sleep(1)
    elif o=="hello":
        global menu, last
        last = menu
        menu = kill_sauce_menu
        menu.show()
    return

kill_sauce_menu = Menu(["kill", "sauce"], callback=hello)
main_menu = Menu(["test", "hello", "gogo"], callback=hello)
menu = main_menu
menu.show()
choice = None

from machine import Pin

ws.up.irq(lambda p: menu.up(), trigger=Pin.IRQ_FALLING)
ws.down.irq(lambda p: menu.down(), trigger=Pin.IRQ_FALLING)
ws.left.irq(lambda p: menu.left(), trigger=Pin.IRQ_FALLING)
ws.ctrl.irq(lambda p: menu.go(), trigger=Pin.IRQ_FALLING)

while True:
    utime.sleep(1)
    print("tick")


