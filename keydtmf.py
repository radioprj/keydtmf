#!/usr/bin/env python3

import smbus
import sys
import time
import os
import configparser


""" this is an example on how to create a keypad using the pcf8475
    https://forums.raspberrypi.com/viewtopic.php?t=100140

    Adopted by SP2ONG 2024 to DTMF keypad 4x4 for SVXLink

    

            Pin4(P4)  Pin6(P5)   Pin7(P6)   Pin8(P7)
               |         |          |
  Pin5(P0) --- 1 ------- 2 -------- 3---------A
               |         |          |
  Pin7(P1) --- 4 ------- 5 -------- 6---------B
               |         |          |
  Pin2(P2) --- 7 ------- 8 -------- 9---------C
               |         |          |
  Pin3(P3) --- * ------- 0 -------- #---------D
   
  
          

"""

config = configparser.ConfigParser()
config.read('keydtmf.ini')

# Define path/file to DTMF SVXLink control
fpath = config.get("keypad","dtmf_ctrl_file")

# Define Power OFF Button
poweroff_btn = config.get("keypad","poweroff_btn")

class MyKeyboard:


  KeyPadTable= [['1','2','3','A'] , ['4','5','6','B'], ['7','8','9','C'], ['*','0','#','D']]
  RowID=[0,0,0,0, 0,0,0,4, 0,0,0,3, 0,2,1,0]

  CurrentKey=None

  def __init__(self,I2CBus=int(config.get("keypad","i2c_port")), I2CAddress=int(config.get("keypad","i2c_address"),16)):
    self.I2CAddress = I2CAddress
    self.I2CBus = I2CBus
    #open smbus pcf8574
    self.bus = smbus.SMBus(self.I2CBus)
    time.sleep(1)
    #set pcf to input
    self.bus.write_byte(self.I2CAddress,0xff)

    #ReadRawKey
    #this function will scan and return a key press
    #with no debouncing.
    # it will return None if no or more than a key is pressed on the same row
    
  def ReadRawKey(self):
    #set P4 Low First
    OutPin= 0x10
    for Column in range(4):
      #scan first row to see if we have something
      self.bus.write_byte(self.I2CAddress,~OutPin)
      #read the key now 
      key = self.RowID[self.bus.read_byte(self.I2CAddress) & 0x0f]
      if key >0 :
        return self.KeyPadTable[key-1][Column]
      OutPin = OutPin * 2
    return None


  #ReadKey return current key once and debounce it
  def ReadKey(self):
   LastKey= self.CurrentKey;
   while True:
    NewKey= self.ReadRawKey()
    if  NewKey != LastKey:
      time.sleep(0.01)
      LastKey= NewKey
    else:
      break
   #if LastValue is the same than CurrentValue
   #just return None
   if LastKey==self.CurrentKey:
     return None
   #ok put Lastvalue to be CurrentValue
   self.CurrentKey=LastKey
   return self.CurrentKey

if __name__ == "__main__":

    test = MyKeyboard()

    while True:
      V = test.ReadKey()
      if V != None:
         if V == poweroff_btn.upper():
            os.system('sudo /usr/sbin/shutdown -h now')
         if os.path.islink(fpath):
            os.system('echo "'+V+'">'+fpath)
         else:
           sys.stdout.write(V)
           sys.stdout.flush()
      else:
        time.sleep(0.1)
