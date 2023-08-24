a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

def loop(a, b):
    c = a +1
    while (c < b):
    
        if c%2 == 0:
            
            print(c)
        c = c +1
loop(a, b)