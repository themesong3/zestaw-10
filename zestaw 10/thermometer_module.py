import random
class thermometer():
    def __init__(self):
        self.temp = 0.0
        is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
        
    def measure_temp(self):
        if self.is_on:
            self.temp = round(random.uniform(34.0, 42.1), 1)
            if self.temp >= 37.0 and self.temp < 41.0:
                print(f"Your temperature is: {self.temp} (fever)")
            elif self.temp >= 41.0:
                print(f"Your temperature is: {self.temp} (CRITICAL TEMPERATURE)")
            else:
                print(f"Your temperature is: {self.temp}")
        else:
            print("Thermometer is off")