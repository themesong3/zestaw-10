class TV():
    def __init__(self):
        self.is_on = False
        self.channel_num = 1
        self.channel_list = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel_num(self, new_channel_no):
        self.channel_num = new_channel_no
    
    def set_channel_name(self, channel_name_to_add):
        self.channel_list.append(channel_name_to_add)
    
    def show_channels(self):
        print("Channel list:\n")
        for index, channel in enumerate(self.channel_list):
            print(f"{index+1}. {channel}")

    def increase_vol(self):
        if self.volume < 10:
            self.volume += 1
    
    def decrease_vol(self):
        if self.volume > 0:
            self.volume -= 1

    def show_status(self):
        if self.is_on:
            # if there is at least one channel in list and the set channel number is not higher than the length of the list
            if len(self.channel_list) > 0 and (self.channel_num <= len(self.channel_list)):
                print(f"TV is on. Channel number: {self.channel_num} ({self.channel_list[self.channel_num-1]})")
                # if the channel number is higher than the number of channels in channel listt)
                if self.channel_num > len(self.channel_list):
                    print(f"TV is on. Channel number: {self.channel_num} (No channel set for this number. You only have {len(self.channel_list)} channels")
            else:
                # if there are no channels in the channel list
                print(f"TV is on. Channel number: {self.channel_num} (Channel not programmed))")
            # show volume status
            print(f"Volume level: {self.volume}")
        else:
            print("TV is off")


samsung = TV()

samsung.turn_on()
samsung.set_channel_name("Polsat")
samsung.set_channel_name("TVN")

samsung.set_channel_num(3)
samsung.show_status()

samsung.set_channel_name("TVN")
samsung.decrease_vol()
samsung.increase_vol()
samsung.show_status()

