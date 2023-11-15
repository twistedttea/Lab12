#jalen been here ong
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False 
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        if self.__muted and self.__status:
            self.__muted = False
        elif not(self.__muted) and self.__status:
            self.__muted = True
        else:
            #turn that hoe on
            pass      

    def channel_up(self):
        pass

    def channel_down(self):
        pass

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.MAX_VOLUME == self.__volume:
                pass #cant change vol
            else: 
                self.__volume += 1
        else:
            pass #tv off

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.MIN_VOLUME == self.__volume:
                pass #cant change vol
            else: 
                self.__volume -= 1
        else:
            pass #tv off

    def __str__(self):
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
