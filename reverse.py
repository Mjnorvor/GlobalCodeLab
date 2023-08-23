#loop
#reverse




a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
    
def reverse (a, b):
    c = b -1
    while (c > a):
        if c%2 == 0:
         print (c)
        c = c-1

reverse(a, b) 