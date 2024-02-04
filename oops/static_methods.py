from datetime import datetime
# Static Methods 
# methods that cant be accessed using self 
# they are just normal functions placed inside a class to keep things organised
# use decorator @staticmethod

class Calendar:
    def __init__(self) -> None:
        self.events = []

    def add_events(self, event) -> None:
        self.events.append(event)
    
    # self aur class se koi lena dena hi nhi h is function ka
    @staticmethod
    def check_weekend(date: datetime):
        if date.weekday() > 4:
            print("It's weekend")
        else:
            print("It's weekday")

# no need to make an object
current_time = datetime.now()
Calendar.check_weekend(current_time)