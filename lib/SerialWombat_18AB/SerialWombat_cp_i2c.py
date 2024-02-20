import .SerialWombat as SerialWombat
import time
import busio
from adafruit_bus_device.i2c_device import I2CDevice



class SerialWombatChip_cp_i2c(SerialWombat.SerialWombatChip):
    i2c  = 0
    def __init__(self,i2c_port:busio.I2C,address:int):
        super().__init__()
        self.device = I2CDevice(i2c_port, address)


    def sendReceivePacketHardware (self,tx):
        device = self.device
        rx = bytearray([0]*8)
        try:
            if (isinstance(tx,list)):
                tx = bytearray(tx);
            with device:
                device.write(tx)
            with device:
                device.readinto(rx)
            if (len(rx) < 8 ):
                return (-len(rx))
            return 8,rx  
        except OSError:
            return -48,bytes("E00048UU",'utf-8')

    def sendPacketToHardware (self,tx):
        device = self.device
        try:
            if (isinstance(tx,list)):
                tx = bytearray(tx);
            with device:
                device.write(tx)
            return 8,bytes("E00048UU",'utf-8')  
        except OSError:
            return -48,bytes("E00048UU",'utf-8')
