class tv():
    
    def __init__(self):
        self.is_on = False
        self.channel = 1
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on:
            print(f"TV is on. Channel nr. {self.channel}")
        else:
            print("TV is off")
            
    def set_channel(self, new_channel_no):
        if self.is_on:
            self.channel = new_channel_no
        else:
            print("Turn on TV to set channel")
            
samsung = tv()

samsung.show_status()

samsung.turn_on()
samsung.show_status()

samsung.set_channel(5)
samsung.show_status()

samsung.turn_off()
samsung.show_status()