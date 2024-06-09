import csv
import typing as t

from flights_exploration.data.readers import AbstractFlightsReader


class KaggleFlightsReader(AbstractFlightsReader):
    def __init__(self):
        self.data = []
        self.file_headers = [
            "id",
            "year",
            "month",
            "day",
            "dep_time",
            "sched_dep_time",
            "dep_delay",
            "arr_time",
            "sched_arr_time",
            "arr_delay",
            "carrier",
            "flight",
            "tailnum",
            "origin",
            "dest",
            "air_time",
            "distance",
            "hour",
            "minute",
            "time_hour",
            "name",
        ]

    def read_file(self, file: t.IO) -> t.Iterator[t.Dict]:
        """
        read flights from a file
        """
        reader = csv.DictReader(file)
        return (line for line in reader)

    def get_flights(self, file: t.IO, cache=False) -> t.List[t.Dict]:
        """
        return a list of all flights. optionally caches the data.
        """
        data = [line for line in self.read_file(file)]
        if cache == True:
            self.data = data
        return data

    def iter_flights(self, file: t.IO) -> t.Iterator[t.Dict]:
        """
        return an iterator of single flights
        """
        return self.read_file(file)
