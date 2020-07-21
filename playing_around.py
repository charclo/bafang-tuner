class Voltage(str):
    twentyfour = 0x00
    thirtysix = 0x01
    fortyeight = 0x02
    sixty = 0x03
    other = 0x04


    def voltagetostring(value):
        switcher = {
            1: "24V",
            2: "36V"
        }
        return switcher[value]

    def stringtovoltage(voltage):
        switcher = {
            "24V" : 1,
            "36V" : 2
        }
        return switcher[voltage]

voltage = Voltage.voltagetostring(0x01)
print(voltage)
print(Voltage.stringtovoltage(voltage))

voltages = {
            "24V" : 0x01,
            "36V" : 0x02
        }

voltages2 =  {
            0x01: "24V",
            0x02: "36V"
        }

voltage = voltages2[0x01]
print(voltage)

print(voltage)