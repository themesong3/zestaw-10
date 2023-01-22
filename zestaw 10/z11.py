class tv():
    
    def __init__(self):
        self.is_on = False
        self.channel_num = 1
        self.channel_list = []
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on:
            print(f"TV is on. Channel nr. {self.channel_num}")
        else:
            print("TV is off")
            
    def set_channel_num(self, new_channel_no):
        if self.is_on:
            self.channel_num = new_channel_no
        else:
            print("Turn on TV to set channel")
            
    def set_channels(self, channel_to_add):
        self.channel_list.append(channel_to_add)
    
    def show_channels(self):
        print("Your saved channels:\n-------------------")
        for i in self.channel_list:
            print(i)




samsung = tv()

samsung.show_status()

samsung.turn_on()
samsung.show_status()

samsung.show_channels()

channel_arr = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
for i in channel_arr:
    samsung.set_channels(i)

samsung.show_channels()

samsung.show_status()

samsung.turn_off()
