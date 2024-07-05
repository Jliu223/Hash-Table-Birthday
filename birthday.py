#John Liu, jl4582
#Justyn Ngo, jmn365
#Karan Rai, kr3287

class Birthday:
    def __init__(self, month, day, year):
        '''
        Purpose: initialize attributes month, day, year
        Parameters: self, month, day, year
        Return: none
        '''
        self.__month = month
        self.__day = day
        self.__year = year
    
    def getMonth(self):
        '''
        Purpose: get the month
        Parameters: self
        Return: self.__month
        '''
        return self.__month
    
    def getDay(self):
         '''
        Purpose: get the day
        Parameters: self
        Return: self.__day
        '''
        return self.__day
    
    def getYear(self):
        '''
        Purpose: get the year
        Parameters: self
        Return: self.__year
        '''
        return self.__year
    
    def __str__(self):
        '''
        Purpose: print the date in month/day/year format 
        Parameters: self
        Return: f"{self.__month}/{self.__day}/{self.__year}"
        '''
        return f"{self.__month}/{self.__day}/{self.__year}"
    
    def __hash__(self):
        '''
        Purpose: return the hash  
        Parameters: self
        Return: (self.__month + self.__day + self.__year) % 12
        '''
        return (self.__month + self.__day + self.__year) % 12
    
    def __eq__(self, other):
        '''
        Purpose: determine if the dates are equal 
        Parameters: self, other 
        Return: return self._day == other._day and self._month == other._month and self._year == other._year
        '''
        if isinstance(other, Birthday):
            return self._day == other._day and self._month == other._month and self._year == other._year
        return False