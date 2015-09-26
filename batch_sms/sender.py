from abc import ABCMeta, abstractmethod

class Sender:
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self, body, to_number, from_number, media_url=None, callback=None): pass