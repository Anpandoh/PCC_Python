#Chapter 6 Assignment part 1#

class Time:
    """Blueprint for a Time object"""
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    def set_time(self, hour, minute, second):
        if hour < 24 and hour >=0 and minute < 60 and minute >=0 and second < 60 and second >=0:
            self.__hour = hour
            self.__minute = minute
            self.__second = second
        else:
            print("Not valid time")
        
    def print_time(self):
        print (self.__hour, ":", self.__minute, ":", self.__second)
###################################################

    def set_second(self, second):
        if second < 60 and second >=0:
            self.__second = second
        else:
            print("Not valid time")
    def get_second(self):
        return self.__second
    
###################################################

    def set_minute(self, minute):
        if minute < 60 and minute >=0:
            self.__minute = minute
        else:
            print("Not valid time")
    def get_minute(self):
        return self.__minute
    
###################################################
    
    def set_hour(self, hour):
        if hour < 24 and hour >=0:
            self.__hour = hour
        else:
            print("Not valid time")
    def get_hour(self):
        return self.__hour
    
###################################################

