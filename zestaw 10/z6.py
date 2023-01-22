class University():
    def __init__(self, name):
        self.name = name
        
    def display_name(self):
        print(self.name)
        
        
uni = University("UEK")
uni.display_name()