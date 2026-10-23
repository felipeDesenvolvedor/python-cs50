import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
   try:
       if mathces:= re.search(r"^(\d{1,2}?)(:?\d{1,2}?)? (AM|PM) to (\d{1,2}?)(:?\d{1,2}?)? (PM|AM)$", s):
           fomat24Hour(extractTime(mathces)) 
           return "Valid"
       else:
           raise ValueError("Invalid")  
   except ValueError as e:
       return e

def extractTime(ranges):
    times = {}

    print("groups", ranges.groups())

    times["startHour"] = {}
    times["startHour"]["hour"] = f'{ranges.group(1):01}'
    times["startHour"]["minutes"] = re.search(r"^(:)?(\d+)?$", ranges.group(2) or '00').group(2)
    
    times["endHour"] = {}
    times["endHour"]["hour"] = f'{ranges.group(4):01}'
    times["endHour"]["minutes"] = re.search(r"^(:)?(\d+)?$", ranges.group(5) or '00').group(2)

    if "minutes" in times["startHour"]:
        if int(times["startHour"]["minutes"]) > 59:
            raise ValueError("Invalid")
    
    if "minutes" in times["endHour"]:
        if int(times["endHour"]["minutes"]) > 59:
            raise ValueError("Invalid")

    if ranges.group(3) == "AM":
        times["startHour"]["period"] = ranges.group(3)
    else:
        times["endHour"]["period"] = ranges.group(6)

    
    if ranges.group(3) == "PM":
        times["startHour"]["period"] = ranges.group(3)
    else:
        times["endHour"]["period"] = ranges.group(6)
        
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
    
    start = times["startHour"]["hour"]+":"+times["startHour"]["minutes"]+times["startHour"]["period"]
    end = times["endHour"]["hour"]+":"+times["endHour"]["minutes"]+times["endHour"]["period"]

    # for horario in horarios:
    #     if end in horario:
    #         format24 = f'{start} to {horario[end]}'


    # print("times", times)

if __name__ == "__main__":
    main()