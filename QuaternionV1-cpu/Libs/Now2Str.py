from datetime import datetime
def Now2Str():
    # current date and time
    now = datetime.now()
    #Date
    year = str(now.year)
    month = ("00"+str(now.month))[-2:]
    day = ("00"+str(now.day))[-2:]
    #time
    hour = ("00"+str(now.hour))[-2:]
    minute = ("00"+str(now.minute))[-2:]
    second = ("00"+str(now.second))[-2:]
    microsecond= ("0000000"+str(now.microsecond))[-7:]
    return year+"-"+month+"-"+day+"_"+hour+"-"+minute+"-"+second+"."+microsecond