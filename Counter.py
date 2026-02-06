class Counter: #this is the is used to handle the counting logic for seconds, minutes, and hours in the Clock class
    def __init__(self):
        self.__count = 0
    
    def get_count(self):
        return self.__count
    
    def increment(self):
        self.__count += 1
    
    def reset(self):
        self.__count = 0