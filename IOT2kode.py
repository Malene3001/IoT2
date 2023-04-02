import time
from rotary_irq_esp import RotaryIRQ
import machine
from machine import SoftI2C, Pin
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

button = Pin(32, Pin.IN)

I2C_ADDR = 0x27
totalRows = 4
totalColumns = 20

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)    

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
cel = bytearray([0x0E, 0x0A, 0x0E, 0x00, 0x00, 0x00, 0x00, 0x00])
oe = bytearray([0x00, 0x00, 0x1F, 0x13, 0x15, 0x19, 0x1F, 0x00])
aa = bytearray([0x04, 0x00, 0x0E, 0x01, 0x0F, 0x11, 0x0F, 0x00])

lcd.custom_char(0, cel)
lcd.custom_char(1, oe)
lcd.custom_char(2, aa)

r = RotaryIRQ(pin_num_clk=34, 
              pin_num_dt=35, 
              min_val=0, 
              max_val=5, 
              reverse=False, 
              range_mode=RotaryIRQ.RANGE_WRAP)


def homescreen1():
    lcd.putstr("                 4"+chr(0)+"c") 
    lcd.putstr("        Menu        ") 
    lcd.putstr("                    ")
    lcd.putstr("Tilfoej  |  Oversigt")
              

def homescreen():
    lcd.putstr("                 4"+chr(0)+"c") 
    lcd.putstr("    Mit k"+chr(1)+"leskab    ") 
    lcd.putstr("                    ")
    lcd.putstr("   Tryk p"+chr(2)+" knappen  ")
    while True:
        if button.value() == 0:
            tilføj()
            break
        else:
            sleep(0.2)
    

def tilføj():
    lcd.putstr("        MENU        ") 
    lcd.putstr("--->  Tilf"+chr(1)+"j        ") 
    lcd.putstr("      Oversigt      ")
    lcd.putstr("      Tilbage       ")
    
def oversigt():
    lcd.putstr("        MENU        ") 
    lcd.putstr("      Tilf"+chr(1)+"j        ") 
    lcd.putstr("--->  Oversigt      ")
    lcd.putstr("      Tilbage       ")
    
    
def tilbage():
    lcd.putstr("        MENU        ") 
    lcd.putstr("      Tilf"+chr(1)+"j        ") 
    lcd.putstr("      Oversigt      ")
    lcd.putstr("--->  Tilbage       ")
    
def oversigt1():
    if mælk == 0:
        lcd.putstr("      Oversigt      ") 
        lcd.putstr("F"+chr(1)+"devare | Udl"+chr(1)+"bsdag ") 
        lcd.putstr("                    ")
        lcd.putstr("                    ")
        while True:
            if button.value() == 0:
                break
            else:
                sleep(0.2)
    if mælk >= 1:
        lcd.putstr("      Oversigt      ") 
        lcd.putstr("F"+chr(1)+"devare | Udl"+chr(1)+"bsdag ") 
        lcd.putstr("Maelk   |"+val_new_d1+" /"+val_new_m1+"-23 ")
        lcd.putstr("                    ")
        while True:
            if button.value() == 0:
                break
            else:
                sleep(0.2)
                
def oversigt2():
        lcd.putstr("                    ") 
        lcd.putstr("--> Fjern f"+chr(1)+"devare  ") 
        lcd.putstr("    Tilbage         ")
        lcd.putstr("                    ")

def oversigt3():
        lcd.putstr("                    ") 
        lcd.putstr("    Fjern f"+chr(1)+"devare  ") 
        lcd.putstr("--> Tilbage         ")
        lcd.putstr("                    ")
    
            
def tilføj0():
    lcd.putstr("  Tilf"+chr(1)+"j f"+chr(1)+"devare   ") 
    lcd.putstr("-->   Maelk         ") 
    lcd.putstr("      Tofu          ")
    lcd.putstr("      Tilbage       ")
    

def tilføj1():
    lcd.putstr("  Tilf"+chr(1)+"j f"+chr(1)+"devare   ") 
    lcd.putstr("      Maelk         ") 
    lcd.putstr("-->   Tofu          ")
    lcd.putstr("      Tilbage       ")
    
def tilføj2():
    lcd.putstr("  Tilf"+chr(1)+"j f"+chr(1)+"devare   ") 
    lcd.putstr("      Maelk         ") 
    lcd.putstr("      Tofu          ")
    lcd.putstr("-->   Tilbage       ")

    
    
def tilføj3():
    lcd.clear
    lcd.putstr("                    ") 
    lcd.putstr("      Tilf"+chr(1)+"jet      ") 
    lcd.putstr("                    ")
    lcd.putstr("                    ")
    
    
    
    
def tilføj3dato():
    lcd.clear()
    lcd.putstr("                    ") 
    lcd.putstr("       Dato         ") 
    lcd.putstr("                    ")
    lcd.putstr("                    ")
    
def lcdtilbage():
    lcd.putstr("                    ") 
    lcd.putstr("       Tilbage      ") 
    lcd.putstr("                    ")
    lcd.putstr("                    ")
    
def fjern0():
    lcd.putstr("                    ") 
    lcd.putstr("       Fjern        ") 
    lcd.putstr("                    ")
    lcd.putstr("                    ")

    
    
val_old = r.value()
val_old1 = r.value()
val_old2 = r.value()
val_pkt = 0
val_pkt = 2
mælk = 0
tofu = 0
homescreen()
valgt = False
    

while True:
    val_new = r.value()
    sleep(0.1)

#menu start
    if val_old != val_new:
        val_old = val_new
        print('result =', val_new)
        
        if val_new == 0 or val_new == 3:
            
            tilføj()
            print("1")
            val_pkt = 0
        elif val_new == 5 or val_new == 2:
            
            oversigt()
            print("2")
            val_pkt = 1
        elif val_new == 4 or val_new == 1:
            
            tilbage()
            print("3")
            val_pkt = 2
            
#start tilføj
            
    if button.value() == 0 and val_pkt == 0:
        tilføj0()
        
        while True:
            if valgt == True:
                valgt = False
                homescreen()
                break
            val_new1 = r.value()
            sleep(0.1)
            if val_old1 != val_new1:
                val_old1 = val_new1
                print('result =', val_new1)
    
                if val_new1 == 0 or val_new1 == 3:
                    tilføj0() #mælk
            
                if val_new1 == 5 or val_new1 == 2:
                    tilføj1() #tofu
        
                if val_new1 == 4 or val_new1 == 1:
                    tilføj2() #tilbage
                    
            if button.value() == 0 and val_new1 == 0 or button.value()== 0 and val_new1 == 3:
                sleep(0.2)
                #rod her
    
                r1 = RotaryIRQ(pin_num_clk=34, 
                pin_num_dt=35, 
                min_val=1, 
                max_val=31, 
                reverse=False, 
                range_mode=RotaryIRQ.RANGE_WRAP)
                lcd.putstr(" Indtast udl"+chr(1)+"bsdato ") 
                lcd.putstr("--> Dag  1          ") 
                lcd.putstr("                    ")
                lcd.putstr("                    ")
    
                val_new_d1 = " 1"
                val_old_d = r1.value()
                while True:
                    if valgt == True:
                        break
                    val_new_d = r1.value()
                    if val_old_d != val_new_d:
                        val_old_d = val_new_d
                        if val_new_d == 31:
                            val_new_d1 = "31"
                        elif val_new_d == 30:
                            val_new_d1 = "30"
                        elif val_new_d == 29:
                            val_new_d1 = "29"
                        elif val_new_d == 28:
                            val_new_d1 = "28"
                        elif val_new_d == 27:
                            val_new_d1 = "27"
                        elif val_new_d == 26:
                            val_new_d1 = "26"
                        elif val_new_d == 25:
                            val_new_d1 = "25"
                        elif val_new_d == 24:
                            val_new_d1 = "24"
                        elif val_new_d == 23:
                            val_new_d1 = "23"
                        elif val_new_d == 22:
                            val_new_d1 = "22"
                        elif val_new_d == 21:
                            val_new_d1 = "21"
                        elif val_new_d == 20:
                            val_new_d1 = "20"
                        elif val_new_d == 19:
                            val_new_d1 = "19"
                        elif val_new_d == 18:
                            val_new_d1 = "18"
                        elif val_new_d == 17:
                            val_new_d1 = "17"
                        elif val_new_d == 16:
                            val_new_d1 = "16"
                        elif val_new_d == 15:
                            val_new_d1 = "15"
                        elif val_new_d == 14:
                            val_new_d1 = "14"
                        elif val_new_d == 13:
                            val_new_d1 = "13"
                        elif val_new_d == 12:
                            val_new_d1 = "12"
                        elif val_new_d == 11:
                            val_new_d1 = "11"
                        elif val_new_d == 10:
                            val_new_d1 = "10"
                        elif val_new_d == 9:
                            val_new_d1 = " 9"
                        elif val_new_d == 8:
                            val_new_d1 = " 8"
                        elif val_new_d == 7:
                            val_new_d1 = " 7"
                        elif val_new_d == 6:
                            val_new_d1 = " 6"
                        elif val_new_d == 5:
                            val_new_d1 = " 5"
                        elif val_new_d == 4:
                            val_new_d1 = " 4"
                        elif val_new_d == 3:
                            val_new_d1 = " 3"
                        elif val_new_d == 2:
                            val_new_d1 = " 2"
                        elif val_new_d == 1:
                            val_new_d1 = " 1"
           
            
                        print('result =', val_new_d)
                        lcd.putstr(" Indtast udl"+chr(1)+"bsdato ") 
                        lcd.putstr("--> Dag "+val_new_d1+"          ") 
                        lcd.putstr("                    ")
                        lcd.putstr("                    ")
                        
                    
                    if button.value() == 0:
                        
        #rod stop
                        sleep(0.5)
                        
                #måned
                
                        r2 = RotaryIRQ(pin_num_clk=34, 
                        pin_num_dt=35, 
                        min_val=1, 
                        max_val=12, 
                        reverse=False, 
                        range_mode=RotaryIRQ.RANGE_WRAP)
                        lcd.putstr(" Indtast udl"+chr(1)+"bsdato ") 
                        lcd.putstr("    Dag "+val_new_d1+"          ") 
                        lcd.putstr("--> M"+chr(2)+"ned  1        ")
                        lcd.putstr("                    ")
                
                        mælk= mælk + 1
                        print(mælk)
                        val_new_m1 = " 1"
                        val_old_m = r2.value()
                        while True:
                            val_new_m = r2.value()
                            if val_old_m != val_new_m:
                                val_old_m = val_new_m
                                if val_new_m == 12:
                                    val_new_m1 = "12"
                                elif val_new_m == 11:
                                    val_new_m1 = "11"
                                elif val_new_m == 10:
                                    val_new_m1 = "10"
                                elif val_new_m == 9:
                                    val_new_m1 = " 9"
                                elif val_new_m == 8:
                                     val_new_m1 = " 8"
                                elif val_new_m == 7:
                                    val_new_m1 = " 7"
                                elif val_new_m == 6:
                                    val_new_m1 = " 6"
                                elif val_new_m == 5:
                                    val_new_m1 = " 5"
                                elif val_new_m == 4:
                                    val_new_m1 = " 4"
                                elif val_new_m == 3:
                                     val_new_m1 = " 3"
                                elif val_new_m == 2:
                                    val_new_m1 = " 2"
                                elif val_new_m == 1:
                                    val_new_m1 = " 1"

                                print('result =', val_new_m)
                                lcd.putstr(" Indtast udl"+chr(1)+"bsdato ") 
                                lcd.putstr("    Dag "+val_new_d1+"          ") 
                                lcd.putstr("--> M"+chr(2)+"ned "+val_new_m1+"        ")
                                lcd.putstr("                    ")
        
                            if button.value() == 0:
                                print("Her")
                                valgt = True #bryder ud af loop
                                r = RotaryIRQ(pin_num_clk=34, 
                                pin_num_dt=35, 
                                min_val=0, 
                                max_val=5, 
                                reverse=False, 
                                range_mode=RotaryIRQ.RANGE_WRAP)
                                break
                        
        
        #måned
                    
            if button.value() == 0 and val_new1 == 5 or button.value()== 0 and val_new1 == 2:
                sleep(0.2)
                while True:
                    if button.value() == 0:
                        sleep(0.2)
                        tofu= tofu + 1
                        print(tofu)
                        dato()
                        break
                    else:
                        sleep(0.5)
            if button.value() == 0 and val_new1 == 4 or button.value()== 0 and val_new1 == 1:
                lcd.clear()
                homescreen()
                break
        
#slut med tilføj
#start oversigt
        
    if button.value() == 0 and val_pkt == 1:
        val_pkt = 0
        
        print("hej1")
        lcd.clear()
        oversigt1()
        if button.value() == 0:
            oversigt2()
            print("hej2")
            val_new2 = 0
            val_pkt_2 = 0
            while True:
                val_new2 = r.value()
                sleep(0.2)
                if val_old2 != val_new2:
                    val_old2 = val_new2
                    print('result =', val_new2)
        
                    if val_new2 == 0 or val_new2 == 2 or val_new2 == 4:
                        print("Hej3")
                        oversigt2()
                        sleep(0.2)
                        val_pkt_2 = 1
                    if val_new2 == 1 or val_new2 == 3 or val_new2 == 5:
                        oversigt3()
                        sleep(0.2)
                        val_pkt_2 = 2
                if button.value() == 0 and val_pkt_2 == 1:
                    val_pkt_2 = 0
                    print("slettet")
                    mælk = 0
                    lcd.clear()
                    oversigt1()
                if button.value() == 0 and val_pkt_2 == 2:
                    val_pkt_2 = 0
                    lcd.clear()
                    homescreen()
                    break
                     
                
                
        
        
#slut oversigt
            
#tilbageknap
            
    if button.value() == 0 and val_pkt == 2: # or button.value() == 0 and val_pkt == 1:
        print("jep2")
        val_pkt = 0
        lcd.clear()
        homescreen()
            

