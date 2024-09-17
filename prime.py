#prime number

n = int(input("Enter number:"))
crazy = False

for i in range(2,n):
    if(n%i == 0):
        crazy = True
        break

if(crazy == True):
    print("Not Prime Number")
else:
    print("Prime number")
