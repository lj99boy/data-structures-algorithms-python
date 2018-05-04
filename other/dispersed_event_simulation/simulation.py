from random import randint
from tree.scenes.PrioQueue import PrioQueue
from stack_and_queue.queue.queue_by_list import SQueue

class Simulation:

    def __init__(self,duration):
        self._eventq = PrioQueue()
        self._time = 0
        self._duration = duration

    def run(self):
        while not self._eventq.is_empty():
            event = self._eventq.dequeue()
            self._time = event.time()
            if self._time>self._duration:
                break
            event.run()

    def add_event(self,event):
        self._eventq.enqueue(event)

    @property
    def cur_time(self):
        return self._time