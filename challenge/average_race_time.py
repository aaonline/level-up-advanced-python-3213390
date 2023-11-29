# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    rhine_times = []
    def get_time(line):
        return re.findall(r'\d{2}:\S+', line)[0]
    lines = races.splitlines()
    for line in lines:
        if "Jennifer Rhines" in line:
            race_time = get_time(line)
            rhine_times.append(race_time)
    print(rhine_times)
    return rhine_times

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    #print('33:04'.split('.'))
    #print('32:32.006'.split('.'))
    sum = 0
    for rt in racetimes:
        millis = 0
        if len(rt.split('.')) > 1:
            millis = int(float(rt.split('.')[1]))
            #print(millis)
            mm = int((rt.split('.')[0]).split(':')[0])
            ss = int((rt.split('.')[0]).split(':')[1])
            print (mm,ss, millis)
        else:
            mm = int(rt.split(':')[0])
            ss = int(rt.split(':')[1])
            print(mm,ss)
        sum = sum + (mm*60*1000 + ss*1000 + millis)
        print (sum)
    print(sum)
    avg = sum / len(racetimes)
    print(avg)
    from datetime import timedelta
    delta = timedelta(milliseconds=avg)
    return (str(delta)[2:-5])
   