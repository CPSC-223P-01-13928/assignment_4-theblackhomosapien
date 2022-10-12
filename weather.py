from dataclasses import dataclass
import json
import calendar


def read_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


def max_temperature(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if date[key]["t"] > x:
                x = data[key]["t"]
    return x


def min_temperature(data, date):
    x = 99999
    for key in data:
        if date == key[0:8]:
            if date[key]["t"] < x:
                x = data[key]["t"]
    return x

def max_humidity(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if date[key]["h"] > x:
                x = data[key]["h"]
    return x

def min_humidity(data, date):
    x = 99999
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] < x:
                x = data [key]['h']
    return x

def tot_rain(data , date):
    x = 0.0
    for key in data:
        if date == key[0:8]:
            x = x + data[key]['r']

def report_daily(data, date):
    display = "========================= DAILY REPORT ========================\n"
    display = display + "Date                      Time  Temperature  Humidity  Rainfall\n"

    display = display + "====================  ========  ===========  ========  ========\n"
    for key in data:
        if date == key[0:8]:
            m = calendar.month_name(int(date[4:6])) + (date[6:8]), "," + str(int(date[0:4]))
            tm = key[8:10] + ":" + key [10:12] + ":" + key[12:14]
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']

            display += f"{m:22}" + f"{tm:10}" + f"{t:11}" + f"{h:10}" + f"{r:10.2f}" + "\n"
        return display

def report_historical(data):
    display = "============================== HISTORICAL REPORT ===========================\n"
    display = display + "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    display = display + "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    display = display + "====================  ===========  ===========  ========  ========  ========\n"
    d = ''

    for key in data:
        if d == key[0:8]:
            continue
        else:
            d == key[0:8]
            m = calendar.month_name[int(d[4:6])] + " " + str(int(d[6:8]))+ ", " + str(int(d[0:4]))
            min_temperature = min_temperature(data = data, date = d)
            max_temperature = max_temperature(data = data, date = d)
            min_humidity = min_humidity(data = data, date = d)
            max_humidity = max_humidity(data = data, date = d)
            rain = tot_rain(data = data, date = d)

    display += f'{m:20}{min_temperature:13}{max_temperature:13}{min_humidity:10}{max_humidity:10}{rain:10:2f}' + '\n'

    return display

