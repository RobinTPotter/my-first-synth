import ws

ws.clear(0)

import utime

for i in range(240):
    ws.lcd.line(i,0,0,i,ws.colour(243,234,0))
    ws.lcd.show()
#    utime.sleep(0.02)

for i in range(240):
    ws.lcd.line(i,240,240,i,ws.colour(243,234,0))
    ws.lcd.show()
#    utime.sleep(0.02)

