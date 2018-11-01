def calculate_LCM(a,b):
    if a > b :
        a, b = b, a
    for i in range(b, a * b + 1, b):
        if(i % a == 0):
            return i

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number: "))
print(calculate_LCM(a,b))


