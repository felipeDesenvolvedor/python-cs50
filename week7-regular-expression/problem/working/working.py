import re
from datetime import datetime

def main():
    print(convert(input("Hours: ")))


def convert(s):
   try:
       if mathces:= re.search(r"^(?P<startHour>\d\d?):?(?P<startMinutes>\d\d?)? (?P<periodStart>AM|PM) to (?P<endHour>\d\d?):?(?P<endMinutes>\d\d?)? (?P<periodEnd>PM|AM)$", s):
           return fomat24Hour(extractTime(mathces)) 
       else:
           raise ValueError("Invalid")  
   except ValueError as e:
       return e

def extractTime(ranges):
    times = {}

    times["startHour"] = {}
    times["startHour"]["hour"] = f'{ranges.group("startHour")}'
    times["startHour"]["minutes"] = f'{ranges.group("startMinutes") or '00'}'
    
    times["endHour"] = {}
    times["endHour"]["hour"] = f'{ranges.group("endHour")}'
    times["endHour"]["minutes"] = f'{ranges.group("endMinutes") or '00'}'

    if "minutes" in times["startHour"]:
        if int(times["startHour"]["minutes"]) > 59:
            raise ValueError("Invalid")
    
    if "minutes" in times["endHour"]:
        if int(times["endHour"]["minutes"]) > 59:
            raise ValueError("Invalid")
    
    if ranges.group("periodStart") == "AM":
        times["startHour"]["period"] = ranges.group("periodStart")
    else:
        times["endHour"]["period"] = ranges.group("periodEnd")

    if ranges.group("periodStart") == "PM":
        times["startHour"]["period"] = ranges.group("periodStart")
    else:
        times["endHour"]["period"] = ranges.group("periodEnd")
        
    return times

def fomat24Hour(times):
    t1 = datetime.strptime(f'{times["startHour"]["hour"]}:{times["startHour"]["minutes"]} {times["startHour"]["period"]}', '%I:%M %p')
    t2 = datetime.strptime(f'{times["endHour"]["hour"]}:{times["endHour"]["minutes"]} {times["endHour"]["period"]}', '%I:%M %p')
    return f'{t1.strftime("%H:%M")} to {t2.strftime("%H:%M")}'

if __name__ == "__main__":
    main()