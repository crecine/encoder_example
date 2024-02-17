import busio
import SerialWombat_18AB.SerialWombat_cp_i2c as SerialWombat_cp_i2c
import SerialWombat_18AB.SerialWombatQuadEnc as SerialWombatQuadEnc
import SerialWombat_18AB.SerialWombatQueue as SerialWombatQueue

def sign(x):
    return '+' if x>=0 else '-'

class wombat_chip(SerialWombat_cp_i2c.SerialWombatChip_cp_i2c):
    def __init__(self, sda_pin, scl_pin):
        i2c = busio.I2C(scl_pin, sda_pin, frequency=100000)
        super().__init__(i2c,0x6B)
        self.begin()
        self.queue = self._init_queue()

    def display_details(self):
        print(self.version)
        print(self.model)
        print(self.fwVersion)
    
    def _init_queue(self, start=0x0000, length=1000, qtype=0):
        q = SerialWombatQueue.SerialWombatQueue(self)
        q.begin(index=start,length=length,qtype=qtype)
        return q

    def read_queue(self):
        q = self.queue
        data = [0, 0, 0, 0]
        data[0] = q.read()
        if data[0] < 0:
            return
        print('reading queue')
        while data[0] >= 0:
            data[1] = q.read()
            data[2] = q.read()
            data[3] = q.read()

            if ((data[0]==14 or data[0]==16 or data[0]==18)
                and data[1]==0xCD and data[2]>=0 and data[3]>=0):
                print(f"{data[0]:X} {data[1]:X} {data[2]:X} {data[3]:X}")
                print(f"Pin {data[0]} moved to value {256*data[3]+data[2]}")
            data = [0, 0, 0, 0]
            data[0] = q.read()
    
    def flush_queue(self):
        print('Flushing Queue')
        q = self.queue
        while True:
            data = [0, 0, 0, 0]
            data[0] = q.read()
            if data[0] < 0:
                print('Queue Empty')
                return
            data[1] = q.read()
            data[2] = q.read()
            data[3] = q.read()

class encoder(SerialWombatQuadEnc.SerialWombatQuadEnc):
    def __init__(self, mp, clk:int, dt:int):
        self.mp = mp
        super().__init__(self.mp.SW)
        self.begin(clk,dt,debounce_mS=50,pullUpsEnabled=True,readState=4)
