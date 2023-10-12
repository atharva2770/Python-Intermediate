
class Calculator:

    def __init__(self, m1, m2):

        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):

        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        s3 = s1 + s2
        return s3

    def __gt__(self, other):

        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1 , self.m2)

cal1 = Calculator(50,60)
cal2 = Calculator(40,60)
cal3 = cal1 + cal2

if cal1 > cal2:
    print("Cal1 Wins")
else:
    print("Cal2 Wins")

print(cal1)

print(cal3)

print(cal2)


