class Race:
    def __init__(self,name: str):
        self.name = name
        self.drivers=[]
    @property
    def name(self):
        return 
    
    @name.setter
    def name(self, value):
        if value=="":
            raise ValueError("Name cannot be an empty string!")