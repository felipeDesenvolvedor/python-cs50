import re
import sys
import datetime
import inflect

class DateTimeSeasons:
    pInflect = inflect.engine()

    def __init__(self, dataBirth):
            self.data_birth = dataBirth
            # self.date_now = datetime.datetime.now().replace(
            #      hour=0, minute=0, second=0, microsecond=0
            # )
            self.date_now = datetime.datetime(2000, 1, 1, 0, 0, 0) 
            self.date_birth_in_minutes = 0
            self.date_diff = 0

    @property
    def data_birth(self):
        return datetime.datetime(
             int(self._data_birth.split("-")[0]), 
             int(self._data_birth.split("-")[1]), 
             int(self._data_birth.split("-")[2]),
             0,
             0,
             0
             )

    @data_birth.setter
    def data_birth(self, dataBirth):
        if re.search(r"^\d{4}-\d{2}-\d{2}$", dataBirth):
            self._data_birth = dataBirth
        else:
            sys.exit("Invalid date")

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
    
    @property
    def date_diff(self):
        return self._date_diff

    @date_diff.setter
    def date_diff(self, dateDiff):
        self._date_diff = dateDiff

    def get_date_born_minutes(self):
               self.date_diff = self.date_now - self.data_birth
               self.date_birth_in_minutes = self.date_diff.days * 24 * 60
               return self.date_birth_in_minutes

    def get_date_born_minutes_in_words(self):
         return self.pInflect.number_to_words(self.get_date_born_minutes(), andword="")