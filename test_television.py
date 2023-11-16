import pytest 
from television import Television
class Test:
    def setup_method(self):
        self.tv0 = Television()
        self.tv1 = Television()

    def test_construction(self):
        assert self.tv0.__str__() == 'Power = False, Channel = 0, Volume = 0'
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'
    def test

