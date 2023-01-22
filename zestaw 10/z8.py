class tv():
    
    def __init__(self):
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on == True:
            print("TV is on")
        else:
            print("TV is off")
            
samsung = tv()

samsung.show_status()

samsung.turn_on()
samsung.show_status()

samsung.turn_off()
samsung.show_status()