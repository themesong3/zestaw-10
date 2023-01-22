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
            if len(self.channel_list) == 0:
                print(f"TV is on. Channel nr. {self.channel_num} (no programmed channel)")
            else:
                if self.channel_num > len(self.channel_list):
                    print(f"No channel programmed for number {self.channel_num}. You have only {len(self.channel_list)} channels")
                else:
                    print(f"TV is on. Channel nr. {self.channel_num} ({self.channel_list[self.channel_num - 1]})")
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
samsung.turn_on()
samsung.show_status()


channel_arr = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
for i in channel_arr:
    samsung.set_channels(i)
    
samsung.show_status()

samsung.set_channel_num(4)
samsung.show_status()

samsung.set_channel_num(10)
samsung.show_status()
