import logging

logger = logging.getLogger(__name__)

class Bafang:
    """
    class to store all information from bafang controller
    """

    def __init__(self):
        # info
        self.manufacturer = "N/A"
        self.model = "N/A"
        self.hw_version = "N/A"
        self.fw_version = "N/A"
        self.voltagebytes = 0
        self.voltagestring = "N/A"
        self.max_current = "N/A"


        #basic
        self.low_battery_protect = 30
        self.limited_current = 15
        self.limited_current_assist0 = 10
        self.limited_current_assist1 = 20
        self.limited_current_assist2 = 30
        self.limited_current_assist3 = 40
        self.limited_current_assist4 = 50
        self.limited_current_assist5 = 60
        self.limited_current_assist6 = 70
        self.limited_current_assist7 = 80
        self.limited_current_assist8 = 90
        self.limited_current_assist9 = 100
        self.limited_speed_assist0 = 10
        self.limited_speed_assist1 = 20
        self.limited_speed_assist2 = 30
        self.limited_speed_assist3 = 40
        self.limited_speed_assist4 = 50
        self.limited_speed_assist5 = 60
        self.limited_speed_assist6 = 70
        self.limited_speed_assist7 = 80
        self.limited_speed_assist8 = 90
        self.limited_speed_assist9 = 100
        self.wheel_diameter = 1
        self.speedmeter_signals = 1
        self.speedmeter_model = 1

        #pedal
        self.pedal_type = 0
        self.assist_level = 0
        self.speed_limit = 0
        self.start_current = 0
        self.slow_start_mode = 0
        self.startup_degree = 0
        self.work_mode = 0
        self.stop_delay = 0
        self.current_decay = 0
        self.stop_decay = 0
        self.keep_current = 0


    def set_info(self, info_bytes: bytes):
        """set the info paramaters of bafang"""
        self.manufacturer = info_bytes[2:6].decode("utf-8")
        self.model = info_bytes[6:10].decode("utf-8")
        self.hw_version = "V" + '.'.join(str(int(info_bytes[10:12])))
        self.fw_version = "V" + '.'.join(str(int(info_bytes[12:16])))
        self.voltagebytes = info_bytes[16]
        self.voltagestring = voltages[self.voltagebytes]
        self.max_current = info_bytes[17]

    def set_basic(self, basic_bytes: bytes):
        """set the basic parameters of bafang"""
        self.low_battery_protect = basic_bytes[2]
        self.limited_current = basic_bytes[3]
        self.limited_current_assist0 = basic_bytes[4]
        self.limited_current_assist1 = basic_bytes[5]
        self.limited_current_assist2 = basic_bytes[6]
        self.limited_current_assist3 = basic_bytes[7]
        self.limited_current_assist4 = basic_bytes[8]
        self.limited_current_assist5 = basic_bytes[9]
        self.limited_current_assist6 = basic_bytes[10]
        self.limited_current_assist7 = basic_bytes[11]
        self.limited_current_assist8 = basic_bytes[12]
        self.limited_current_assist9 = basic_bytes[13]
        self.limited_speed_assist0 = basic_bytes[14]
        self.limited_speed_assist1 = basic_bytes[15]
        self.limited_speed_assist2 = basic_bytes[16]
        self.limited_speed_assist3 = basic_bytes[17]
        self.limited_speed_assist4 = basic_bytes[18]
        self.limited_speed_assist5 = basic_bytes[19]
        self.limited_speed_assist6 = basic_bytes[20]
        self.limited_speed_assist7 = basic_bytes[21]
        self.limited_speed_assist8 = basic_bytes[22]
        self.limited_speed_assist9 = basic_bytes[23]
        self.wheel_diameter = wheel_sizes[basic_bytes[24]]
        self.speedmeter_signals = basic_bytes[25]
        self.speedmeter_model = basic_bytes[25]

    def set_basic_with_dict(self, basic_dict: dict):
        """set the basic parameters of bafang from a dict """
        for attr, value in basic_dict.items():
            setattr(self, attr, value)

        ### Response (description):
        """ 00: 0x53 
        * 01: 0x0B (Length?)
        * 02: Pedal Type (0x03)
            * 0x00: None
            * 0x01: DH-Sensor-12
            * 0x02: BB-Sensor-32
            * 0x03: DoubleSignal-24
        * 03: Designated Assist (FF)
            * 0x00-0x09: Assist Mode No.
            * 0xFF: By Display's Command
        * 04: Speed Limit (FF)
            * 0x0F-0x28: Speed Limit in km/h
            * 0xFF: By Display's Command
        * 05: Start current in % (0x64 -> 100)
            * 0x00-0x64
        * 06: Slow-Start Mode (06 -> 6)
            * 0x01-0x08: Mode Number
        * 07: Startup Degree (Signal No.) (0x14 -> 20)
            * Integer: Number of Signal before start
        * 08: Work Mode (0x0A -> 10)
            * 0x0A-0x50: Angular Speed of pedal/wheel*10
            * 0xFF: Undetermined
        * 09: Time of Stop (0x19 -> 25)
            * Integer: *10ms
        * 10: Current Decay (0x08 -> 8)
            * 0x01-0x08: Current Decay 
        * 11: Stop Decay (0x14 -> 20)
            * Integer: *10ms
        * 12: Keep Current in % (0x14 -> 20)
        * 13: Checksum ? (0x27)*/ """

    def set_pedal(self, pedal_data: bytes):
        """set the pedal parameters of bafang"""
        logger.debug("pedal data is:")
        logger.debug(pedal_data)
        self.pedal_type = pedal_data[2]
        self.assist_level = pedal_data[3]
        self.speed_limit = pedal_data[4]
        self.start_current = pedal_data[5]
        self.slow_start_mode = pedal_data[6]
        self.startup_degree = pedal_data[7]
        self.work_mode = pedal_data[8]
        self.stop_delay = pedal_data[9]
        self.current_decay = pedal_data[10]
        self.stop_decay = pedal_data[11]
        self.keep_current = pedal_data[12]



    def get_key(self, val): 
        for key, value in voltages.items(): 
            if val == value: 
                return key
        return "key doesn't exist"

voltages = {
    0x00: '24V',
    0x01: '36V',
    0x02: '48V',
    0x03: '60V',
    0x04: 'Other'
    }


wheel_sizes = {
    0x1F: 0,
    0x20: 0,
    0x21: 1,
    0x22: 1,
    0x23: 2,
    0x24: 2,
    0x25: 3,
    0x26: 3,
    0x27: 4,
    0x28: 4,
    0x29: '21"',
    0x2A: '21"',
    0x2B: '22"',
    0x2C: '22"',
    0x2D: '23"',
    0x2E: '23"',
    0x2F: '24"',
    0x30: '24"',
    0x31: '25"',
    0x32: '25"',
    0x33: 10,
    0x34: 10,
    0x35: '27"',
    0x36: '27"',
    0x37: '700C',
    0x38: '28"',
    0x39: '29"',
    0x3A: '29"',
    0x3B: '30"',
    0x3C: '30"',
}

# wheel_sizes = {
#     0x1F: '16"',
#     0x20: '16"',
#     0x21: '17"',
#     0x22: '17"',
#     0x23: '18"',
#     0x24: '18"',
#     0x25: '19"',
#     0x26: '19"',
#     0x27: '20"',
#     0x28: '20"',
#     0x29: '21"',
#     0x2A: '21"',
#     0x2B: '22"',
#     0x2C: '22"',
#     0x2D: '23"',
#     0x2E: '23"',
#     0x2F: '24"',
#     0x30: '24"',
#     0x31: '25"',
#     0x32: '25"',
#     0x33: '26"',
#     0x34: '26"',
#     0x35: '27"',
#     0x36: '27"',
#     0x37: '700C',
#     0x38: '28"',
#     0x39: '29"',
#     0x3A: '29"',
#     0x3B: '30"',
#     0x3C: '30"',
# }