class Event:
    def __init__(self,event_time,host):
        self._ctime = event_time
        self._host = host

    def __lt__(self,other_event):
        return self._ctime < other_event._ctime

    def __le__(self,other_event):
        return self._ctime < other_event._ctime

    def host(self):
        return self._host

    def time(self):
        return self._ctime

    def run(self):
        pass