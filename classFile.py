class Fan:
    # Constant for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
    
    # Access methods (getters)
    def get_speed(self):
        return self.__speed
    
    def is_on(self):
        return self.__on

    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color
    
    # Mutator methods (setters)
    def set_speed(self, speed):
        self.__speed = speed
       