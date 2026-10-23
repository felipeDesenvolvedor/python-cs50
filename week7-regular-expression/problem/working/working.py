import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
   try:
       if mathces:= re.search(r"^(\d{1,2}?)(:\d{1,2}?)? (AM|PM) to (\d{1,2}?)(:\d{1,2}?)? (PM|AM)$", s):
           print(extractTime(mathces)) 
           return "Valid"
       else:
           raise ValueError("Invalid")  
   except ValueError as e:
       return e

def extractTime(ranges):
    times = {}
    times["startHour"] = {}
    times["startHour"]["hour"] = f'{ranges.group(1):01}'

    if ranges.group(2):
        times["startHour"]["minutes"] = f'{ranges.group(2).replace(":", ""):01}'

    times["endHour"] = {}
    times["endHour"]["hour"] = f'{ranges.group(4):01}'

    if ranges.group(5):
        times["endHour"]["minutes"] = f'{ranges.group(5).replace(":", ""):01}'

    if "minutes" in times["startHour"]:
        if int(times["startHour"]["minutes"]) > 59:
            raise ValueError("Invalid")
    
    if "minutes" in times["endHour"]:
        if int(times["endHour"]["minutes"]) > 59:
            raise ValueError("Invalid")
        
    return times

if __name__ == "__main__":
    main()