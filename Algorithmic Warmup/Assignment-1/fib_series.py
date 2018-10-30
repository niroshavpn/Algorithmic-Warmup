#0 1 1 2 3 5 space complexityime Complexity: O(n) Extra Space: O(1)
def fib_series(n):
    a=0
    b=1
    if(n<0):
        print("Entered Negative Number ")
    elif(n==0):
        return a
    elif(n==1):
        return b
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b

n=int(input("Enter A Number"))
for i in range (n) :
    print(fib_series(i))

