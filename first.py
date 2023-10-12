#
# class Computer:  #construct class
#
#     def config(self):  #define method
#         print("i5 , 16GB , 1TB")
#
# com1 = Computer()
# com2 = Computer()   #constructor
#
#
# com2.config()  #methodcall

## OOPS CWH First

class Programmer:
    company = 'Microsoft'

    def __init__(self,name,product):

        self.name = name
        self.product = product

    def getInfo(self):

        print(f"The Programmer name is {self.name} and product is {self.product}")

Atharva = Programmer('Atharva','WebDevelopment')
Ganesh = Programmer('Ganesh','AWS')

Atharva.getInfo()
Ganesh.getInfo()



