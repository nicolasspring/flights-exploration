import typing as t


class AbstractFlightsReader:
    def read_file(self, file: t.IO):
        """
        read flights from a file
        """
        raise NotImplementedError

    def get_flights(self, file: t.IO, cache=False) -> t.List[t.Dict]:
        """
        return a list of all flights. optionally caches the data.
        """
        raise NotImplementedError

    def iter_flights(self, file: t.IO) -> t.Iterator[t.Dict]:
        """
        return an iterator of single flights
        """
        raise NotImplementedError
