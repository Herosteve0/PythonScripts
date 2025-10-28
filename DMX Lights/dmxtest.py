import DMXI
from KingPar3 import KingPar3
from LEDBar import LEDBar13
import time

ms = 1/1000

def main():
    if not DMXI.CheckDevices(): return
    interface = DMXI.DMXInterface(0)

    light = LEDBar13(interface, 50)

    interface.start()

    light.setPosY(128)
    light.setDimmer(255)
    light.setStrobo(0)

    time.sleep(5)

    interface.stop()

if __name__ == '__main__':
    main()