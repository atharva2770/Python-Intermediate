class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(f"My name is {self.name} and roll number is {self.rollno} ")
        self.lap.show()

    class Laptop:

        def __init__(self):

            self.brand = "HP"
            self.ram = 16
            self.cpu = "i5"

        def show(self):

            print(f"My laptop brand is {self.brand} and ram is {self.ram} and cpu is {self.cpu}")


s1 = Student('Atharva' , 30)
s1.show()
