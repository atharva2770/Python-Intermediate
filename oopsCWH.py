# class Calculator:
#
#     def __init__(self,num):
#         self.num = num
#
#     def output(self):
#         print(f"The number is {self.num} \n square is {self.num**2} \n cube is {self.num**3} \n "
#               f"square root is {self.num**0.5}")
#
# num = Calculator(25)
#
# num.output()


# ##Program 2 (Get Information regarding Train)
# class Train:
#
#     def __init__(self,name,fare,seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats
#
#     def book_a_ticket(self):
#         if(self.seats > 0):
#             print("Your ticket is Booked!!!")
#             self.seats = self.seats - 1
#         else:
#             print("Tickets are not available try tatkal")
#
#
#     def getStatus(self):
#         print(f"The name of the train is {self.name}")
#         print(f"The seats available in the train are {self.seats}")
#
#     def get_fare_info(self):
#         print(f"The price of your ticket is : Rs {self.fare}")
#
#
# a = Train("'12086' Deogiri Train",150,5)
#
# a.getStatus()
# a.book_a_ticket()
# a.get_fare_info()
#
# a.getStatus()
# a.book_a_ticket()

