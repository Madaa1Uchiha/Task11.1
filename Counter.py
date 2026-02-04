class Counter:
    def __init__(self):
        self.__count = 0
    
    def get_count(self):
        return self.__count
    
    def increment(self):
        self.__count += 1
    
    def reset(self):
        self.__count = 0