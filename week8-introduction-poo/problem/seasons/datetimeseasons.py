import re
import sys
import datetime

class DateTimeSeasons:
    def __init__(self, dataBirth):
            self.data_birth = dataBirth
            self.date_now = datetime.date.today()
            self.date_birth_in_minutes = 0

    @property
    def data_birth(self):
        return self._data_birth

    @data_birth.setter
    def data_birth(self, dataBirth):
        if re.search(r"^\d{4}-\d{2}-\d{2}$", dataBirth):
            self._data_birth = dataBirth
        else:
            sys.exit("Invalid date format. Please use YYYY-MM-DD.")

    @property
    def date_now(self):
        return self._date_now

    @date_now.setter
    def date_now(self, dateNow):
        self._date_now = dateNow

    @property
    def date_birth_in_minutes(self):
        return self._date_birth_in_minutes

    @date_birth_in_minutes.setter
    def date_birth_in_minutes(self, date_birth_in_minutes):
        self._date_birth_in_minutes = date_birth_in_minutes

    def get_date_born(self):
               dateDiff = self._date_now - datetime.date(int(self._data_birth.split("-")[0]), int(self._data_birth.split("-")[1]), int(self._data_birth.split("-")[2]))
               self._date_birth_in_minutes = dateDiff.days * 24 * 60
               print("date_birth_in_minutes:", self._date_birth_in_minutes)