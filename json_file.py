import json

def write_json(baf, filename = "backup.json"):
    """
    function to save settings to a json file
    """
    basic_dict = {      
                    'info' : {
                        "manufacturer": baf.manufacturer,
                        "model": baf.model,
                        "hw_version": baf.hw_version,
                        "fw_version": baf.fw_version,
                        "voltagebytes": baf.voltagebytes,
                        "voltagestring": baf.voltagestring,
                        "max_current": baf.max_current
                    },
                    'basic': {
                        "low_battery_protect": baf.low_battery_protect,
                        "limited_current": baf.limited_current,
                        "limited_current_assist0": baf.limited_current_assist0,
                        "limited_current_assist1": baf.limited_current_assist1,
                        "limited_current_assist2": baf.limited_current_assist2,
                        "limited_current_assist3": baf.limited_current_assist3,
                        "limited_current_assist4": baf.limited_current_assist4,
                        "limited_current_assist5":  baf.limited_current_assist5,
                        "limited_current_assist6": baf.limited_current_assist6,
                        "limited_current_assist7": baf.limited_current_assist7,
                        "limited_current_assist8": baf.limited_current_assist8,
                        "limited_current_assist9": baf.limited_current_assist9,
                        "limited_speed_assist0": baf.limited_speed_assist0,
                        "limited_speed_assist1": baf.limited_speed_assist1,
                        "limited_speed_assist2": baf.limited_speed_assist2,
                        "limited_speed_assist3": baf.limited_speed_assist3,
                        "limited_speed_assist4": baf.limited_speed_assist4,
                        "limited_speed_assist5": baf.limited_speed_assist5,
                        "limited_speed_assist6": baf.limited_speed_assist6,
                        "limited_speed_assist7": baf.limited_speed_assist7,
                        "limited_speed_assist8": baf.limited_speed_assist8,
                        "limited_speed_assist9": baf.limited_speed_assist9,
                        "wheel_diameter": baf.wheel_diameter,
                        "speedmeter_signals": baf.speedmeter_signals,
                        "speedmeter_model": baf.speedmeter_model
                    }
                }

    with open(filename, 'w') as outfile:
        json.dump(basic_dict, outfile, indent=4)
        outfile.close()

def read_json(backup_file = 'backup.json'):
    """function to read bafang settings from json file"""
    with open(backup_file) as json_file:
        data = json.load(json_file)
        info = data['info']
        basic = data['basic']
        return info, basic