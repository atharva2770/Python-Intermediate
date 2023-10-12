
a = 5
b = 2

try:
    print(a / b)
    b = int(input("Enter a number "))
    print(b)

except ZeroDivisionError:
    print("Divided By Zero")

except ValueError:
    print("Invalid input not a number")

except Exception:
    print("Something is wrong")

finally:
    print("Zhala ekdacha")

print("Jamla")
