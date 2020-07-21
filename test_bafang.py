from serial import Serial
from protocol import Protocol
import unittest
from bafang import Bafang


class BafangTest(unittest.TestCase):

    # def test_get_info(self):
    #     protocol = Protocol()
    #     protocol.connect('COM3')
    #     info = protocol.get_info()
    #     self.assertEqual(info, b'\x51\x10HZXTSZZ6222011\x01\x14\x1b')
    #     basic = protocol.get_basic()
    #     self.assertEqual(basic, b'R\x18\x1f\x0f\x00\x1c%.7@IR[ddddddddddd4\x01\xdf')
    #     pedal = protocol.get_pedal()
    #     self.assertEqual(pedal, b"S\x0b\x03\xff\xffd\x06\x14\n\x19\x08\x14\x14'")

    def test_bafang_initiation(self):
        baf = Bafang()
        baf.set_info(b'\x51\x10HZXTSZZ6222011\x02\x14\x1b')
        self.assertEqual(baf.manufacturer, 'HZXT')
        self.assertEqual(baf.model, 'SZZ6')
        self.assertEqual(baf.hw_version, 'V2.2')
        self.assertEqual(baf.fw_version, 'V2.0.1.1') # 'V2.0.1.1')
        self.assertEqual(baf.voltagebytes, 2)
        self.assertEqual(baf.voltagestring, "48V")
        self.assertEqual(baf.max_current, 20)
        #self.assertEqual(baf.checksum, 27)

    def test_bafang_set_basic(self):
        baf = Bafang()
        baf.set_basic(b'R\x18\x1f\x0f\x00\x1c%.7@IR[ddddddddddd\x34\x01\xdf')
        self.assertEqual(baf.wheel_diameter, '26"')



if __name__ == '__main__':
    unittest.main()