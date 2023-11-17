
class Television:
    """
    This class is represents a TV remote
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self) -> None:
        """
        Initializes 4 attributes
        :param status: power False
        :param muted: mute False
        :param volume: volume 0
        :param channel: channel 0
        """
        self.__status: bool = False
        self.__muted: bool = False 
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL
    
    def power(self) -> None:
        """
        flips status state
        None
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        flips mute state if status True
        None
        """
        if self.__status:
            if self.__muted: 
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Increases channel value by +1
        if channel is at max value -> min value
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases channel value by -1
        if channel is at min value -> max value
        """

        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
    
    def volume_up(self) -> None:
        """
        Increases volume value by +1
        if volume is at max -> no change
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.MAX_VOLUME == self.__volume:
                pass
            else:
                self.__volume += 1

            

    def volume_down(self) -> None:
        """
        Decreases volume by -1
        if volume is at min -> no change
        """

        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.MIN_VOLUME == self.__volume:
                pass
            else:
                self.__volume -= 1         
    
    def __str__(self) -> str:
        """
        Returns the current values of the attributes
        if muted == true -> display volume as zero
        """

        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
