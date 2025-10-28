import ctypes
import time
import threading

ftd2xx = ctypes.windll.LoadLibrary("ftd2xx.dll")

def CheckDevices() -> bool:
    dev_count = ctypes.c_ulong()
    ftd2xx.FT_CreateDeviceInfoList(ctypes.byref(dev_count))
    if dev_count.value == 0:
        print("No Devices found.")
        return False
    print("Devices found:", dev_count.value)
    return True

FPS = 30
FT_OK = 0

class DMXInterface:
    def __init__(self, device_index = 0):
        self.handle = ctypes.c_void_p()
        status = ftd2xx.FT_Open(device_index, ctypes.byref(self.handle))
        if status != FT_OK:
            raise RuntimeError(f"FT_Open failed: {status}")
        print(f"Opened FTDI device index {device_index}, handle = {self.handle.value}")

        status = ftd2xx.FT_SetBaudRate(self.handle, 250000)
        if status != FT_OK:
            raise RuntimeError(f"FT_SetBaudRate failed: {status}")

        status = ftd2xx.FT_SetDataCharacteristics(
            self.handle,
            8, 2, 0
        )
        if status != FT_OK:
            raise RuntimeError(f"FT_SetDataCharacteristics failed: {status}")

        ftd2xx.FT_SetLatencyTimer(self.handle, 2)
        ftd2xx.FT_SetUSBParameters(self.handle, 512, 512)
        ftd2xx.FT_Purge(self.handle, 1 | 2)

        self.dmx_data = bytearray(512)
        self.running = False
        self.thread = None

        print("DMX Interface initialized and ready.")

    def set_channel(self, ch, val):
        if 1 <= ch <= 512:
            self.dmx_data[ch-1] = val & 0xFF

    def _frame_loop(self):
        while self.running:
            ftd2xx.FT_SetBreakOn(self.handle)
            time.sleep(0.0001)
            ftd2xx.FT_SetBreakOff(self.handle)
            time.sleep(0.000012)

            written = ctypes.c_ulong()
            packet = b"\x00" + bytes(self.dmx_data)
            buffer = ctypes.create_string_buffer(packet)
            status = ftd2xx.FT_Write(self.handle, buffer, len(packet), ctypes.byref(written))
            if status != FT_OK:
                raise RuntimeError(f"FT_Write failed: {status}")

            time.sleep(1/FPS)

    def start(self):
        if self.running:
            print("Start called when Interface was already running.")
            return
        self.running = True

        self.thread = threading.Thread(target=self._frame_loop, daemon=True)
        self.thread.start()
        print(f"DMX Interfaced output thread started ({FPS} FPS)")

    def stop(self):
        for i in range(len(self.dmx_data)):
            self.set_channel(i, 0)

        time.sleep(0.1)

        self.running = False
        if self.thread:
            self.thread.join()
        ftd2xx.FT_Close(self.handle)
        print("DMX Interface closed.")