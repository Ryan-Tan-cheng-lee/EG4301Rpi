import smbus2
import time

I2C_BUS = 1  
PN532_I2C_ADDRESS = 0x48  
MULTIPLEXER_I2C_ADDRESS = 0x70

def select_channel(channel):
    bus = smbus2.SMBus(I2C_BUS)
    bus.write_byte(MULTIPLEXER_I2C_ADDRESS, 1 << channel)

def read_rfid():
    bus = smbus2.SMBus(I2C_BUS)

    while True:
        try:
            
            select_channel(0)  # channel number
            data = bus.read_byte(PN532_I2C_ADDRESS)
            
            if data == 0x01:  
                print("Card read")
            
            time.sleep(0.5)  
        except IOError:
            pass  





if __name__=='__main__':
    rfidmodule()
