value = input("Enter value: ")
value = int(value)

def function():
    if(value == 7):       
        print("Goodbye!")
    elif(value > 0):    
        print("Number is positive")
    elif(value < 0):
        print("Number is negative")
    elif(value == 0):
        print("Number is equal to zero")

function()
input("")