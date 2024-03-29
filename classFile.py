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

    def set_on(self, on):
        self.__on = on

    def set__radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

class TestFan:
    def main(self):
        # Create two Fan object
        fan1 = Fan(Fan.FAST, 10, 'yellow', True)
        fan2 = Fan(Fan.MEDIUM, 5, 'blue', False)
        
        # Display fan1 properties
        print("Fan 1 Properties:")
        print("Speed:", fan1.get_speed())
        print("Radius:", fan1.get_radius())
        print("Color:", fan1.get_color())
        print("Is On:", fan1.is_on())

        # Display fan2 properties
        print("\nFan 2 Properties:")
        print("Speed:", fan2.get_speed())
        print("Radius:", fan2.get_radius())
        print("Color:", fan2.get_color())
        print("Is On:", fan2.is_on())

# Create a TestFan object and run the test program
if __name__ == "__main__":
    test_fan = TestFan()
    test_fan.main()
       