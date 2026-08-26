from machine import Pin, PWM

freq_num = 10000

redLED = PWM(Pin(0))
greenLED = PWM(Pin(1))
blueLED = PWM(Pin(2))
redLED.freq(freq_num)
greenLED.freq(freq_num)
blueLED.freq(freq_num)

def setColor(r, g, b):
    redLED.duty_u16(r)
    greenLED.duty_u16(g)
    blueLED.duty_u16(b)
    
red   = 0   #Choose number between 0 and 65535
green = 255 #Choose number between 0 and 65535
blue  = 255 #Choose number between 0 and 65535
#Because it's a little unclear how this works, use this website to pick colours: https://www.w3schools.com/colors/colors_picker.asp, it worked for me when I did it at home
#Oh, and the number 65535 comes from being FFFF in base sixteen, which is why we say duty_u16(), just so you know
setColor(red, green, blue)
