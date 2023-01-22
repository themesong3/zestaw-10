class University():
    def __init__(self):
        self.name = "NAME NOT SET"
        
    def display_name(self):
        print(self.name)
    
    def set_name(self):
        self.name = input("Please set the university name: ")
        
        
uni = University()
uni.display_name()
uni.set_name()
uni.display_name()