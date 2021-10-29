from serial import Serial
from time import sleep
from serial.tools import list_ports
import logging

logger = logging.getLogger(__name__)

class Protocol():
    def __init__(self):
        self.connect_cmd = b"\x11\x51\x04\xB0\x05"
        self.basic_read_cmd = b"\x11\x52"
        self.pedal_read_cmd = b"\x11\x53"
        self.throttle_read_cmd = b"\x11\x54"
        self.basic_write_cmd = [0x16, 0x52] #, 0x24]

    
    def connect(self, serial_port):
        self.serial_port = Serial(serial_port, 1200, timeout=1)
        # Wait 2 seconds until Arduino is rebooted after serial connect
        # sleep(2) # not necessary if a 10µF C is connected between RESET and GND for arduino

    def disconnect(self):
        self.serial_port.close()

    def get_ports(self):
        return list_ports.comports()


    def readinfo(self):
        self.serial_port.write(self.connect_cmd)
        return self.serial_port.read(19)

    def readbasic(self):
        self.serial_port.write(self.basic_read_cmd)
        return self.serial_port.read(27)

    def writebasic(self, baf):
        basic_packet = [ baf.low_battery_protect,
                        baf.limited_current,
                        baf.limited_current_assist0,
                        baf.limited_current_assist1,
                        baf.limited_current_assist2,
                        baf.limited_current_assist3,
                        baf.limited_current_assist4,
                        baf.limited_current_assist5,
                        baf.limited_current_assist6,
                        baf.limited_current_assist7,
                        baf.limited_current_assist8,
                        baf.limited_current_assist9,
                        baf.limited_speed_assist0,
                        baf.limited_speed_assist1,
                        baf.limited_speed_assist2,
                        baf.limited_speed_assist3,
                        baf.limited_speed_assist4,
                        baf.limited_speed_assist5,
                        baf.limited_speed_assist6,
                        baf.limited_speed_assist7,
                        baf.limited_speed_assist8,
                        baf.limited_speed_assist9,
                        baf.wheel_diameter,
                        baf.speedmeter_signals,
                        baf.speedmeter_model]
        basic_packet = self.basic_write_cmd + basic_packet
        logger.debug("basic packet is:")
        logger.debug(basic_packet)
        bytes_written = self.serial_port.write(basic_packet)
        logger.debug("bytes written:")
        logger.debug(bytes_written)
        response_length = self.serial_port.in_waiting
        logger.debug("response length:")
        logger.debug(response_length)
        response = self.serial_port.read(response_length)
        logger.debug("response:")
        logger.debug(response)


        
    
    def readpedal(self):
        self.serial_port.write(self.pedal_read_cmd)
        return self.serial_port.read(14)

    def readthrottle(self):
        self.serial_port.write(self.throttle_read_cmd)
        return True


