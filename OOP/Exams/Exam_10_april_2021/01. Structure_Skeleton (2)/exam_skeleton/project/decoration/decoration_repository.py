class DecorationRepository:
    def __init__(self):
        self.decorations=[]

    def add(self,decoration):
        self.decorations.append(decoration)

    def remove(self,decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True

        return False


    def find_by_type(self,decoration_type):
        for decor in self.decorations:
            if decoration_type==decor.__class__.__name__:
                return decoration_type

        return "None"