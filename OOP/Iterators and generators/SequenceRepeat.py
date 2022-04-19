class sequence_repeat:
    def __init__(self,letter,repeater):
        self.letter = letter
        self.repeater = repeater
        self.idx=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.repeater==0:
            raise StopIteration
        ch=self.letter[self.idx]
        self.repeater-=1
        self.idx+=1
        if self.idx>=len(self.letter):
            self.idx=0
        return ch


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')