class Television:
    """
    A class representing different functions of a television.
    It behaves like a remote that will change channel, volume, mute, and power.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Method to set default values of television object.
        :param muted: TV's mute status
        :param volume: TV's volume
        :param status: TV's power status
        :param channel: TV's channel
        """
        self.__muted: bool  = False
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn the television on and off.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Method to mute and unmute the television.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True
    
    def channel_up(self) -> None:
        """
        Method to change the channel up by one.
        Will update to minimum channel if at the max.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to change the channel down by one.
        Will update to maximum channel if at the min.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to change the volume up by one.
        Automatically unmutes the TV.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to change the volume down by one.
        Automatically unmutes the TV.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        """
        if self.__muted:
            volume = Television.MIN_VOLUME
        else:
            volume = self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
    
