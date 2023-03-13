# from datetime import datetime


class Person:
    description: str = "A simple normal human being"

    def __init__(self, name: str, surname: str, agr: int):

        self.name: str = name
        self.surname: str = surname

    def greet(self):
        return f"Hello {self.name} {self.surname}"
    

    
    def calculate_days_left_to_blackfriday(self):
         # Get today's date
         # initialize black friday_date
        #  blackfriday_date = datetime.date.today() + datetime.timedelta(days=1

        today = datetime.today()
        black_friday_date = datetime(2024, 11, 24)
        delta = black_friday_date - today
        return delta.days

    def get_eye_color(self, eye_color: str = 'Brown') -> str:
        return eye_color
    
    def __repr__(self):
        return f"Person: {self.name} {self.surname}"
    
    def __str__(self):
        return
        
        


person = Person('Jakov', 'Solovov', 37)
print(person.get_eye_color('Blue'))




    