
#Euclids Algoritham
def calculate_GCD(n,m):
    if m==0:
        return n
    else:
        return (calculate_GCD(m,n%m))
n=int(input("Enter First Number"))
m=int(input("Enter Second Number"))
print(calculate_GCD(n,m))