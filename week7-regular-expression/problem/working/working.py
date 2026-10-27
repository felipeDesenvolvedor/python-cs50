import re
import sys

def main():
    convert(input("Hours: "))


def convert(s):
   try:
       if mathces:= re.search(r"^(?P<startHour>\d\d?):?(?P<startMinutes>\d\d?)? (?P<periodStart>AM|PM) to (?P<endHour>\d\d?):?(?P<endMinutes>\d\d?)? (?P<periodEnd>PM|AM)$", s):
           fomat24Hour(extractTime(mathces)) 
           return "Valid"
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
    format24 = ""
    horarios = [
        {"12:00AM": "00:00"},
        {"1:00AM": "01:00"},
        {"2:00AM": "02:00"},
        {"3:00AM": "03:00"},
        {"4:00AM": "04:00"},
        {"5:00AM": "05:00"},
        {"6:00AM": "06:00"},
        {"7:00AM": "07:00"},
        {"8:00AM": "08:00"},
        {"9:00AM": "09:00"},
        {"10:00AM": "10:00"},
        {"11:00AM": "11:00"},
        {"12:00PM": "12:00"},
        {"1:00PM": "13:00"},
        {"2:00PM": "14:00"},
        {"3:00PM": "15:00"},
        {"4:00PM": "16:00"},
        {"5:00PM": "17:00"},
        {"6:00PM": "18:00"},
        {"7:00PM": "19:00"},
        {"8:00PM": "20:00"},
        {"9:00PM": "21:00"},
        {"10:00PM": "22:00"},
        {"11:00PM": "23:00"},
        {"12:00AM": "00:00"},
    ]
    
    # start = times["startHour"]["hour"]+":"+times["startHour"]["minutes"]+times["startHour"]["period"]
    # end = times["endHour"]["hour"]+":"+times["endHour"]["minutes"]+times["endHour"]["period"]

    # for horario in horarios:
    #     if end in horario:
    #         format24 = f'{start} to {horario[end]}'


    print("times", times)

if __name__ == "__main__":
    main()