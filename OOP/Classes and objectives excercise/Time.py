class Time:
    max_seconds=59
    max_minutes=59
    max_hours=23
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def set_time(self,hours,minutes,seconds):
        self.hours=hours
        self.minutes = minutes
        self.seconds = seconds
    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
    def next_second(self):
        self.seconds+=1
        if Time.max_seconds<=self.seconds:
            self.seconds=0
            self.minutes+= 1
        if Time.max_minutes<=self.minutes:
            self.minutes=0
            self.hours +=1
        if Time.max_hours<=self.hours:
            self.hours=0

        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
