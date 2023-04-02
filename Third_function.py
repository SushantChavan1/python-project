###3.Function Without Argument with return###

def addition():#defination
    print("Enter the value of a&b")
    a,b=input().split(",")
    return int(a)+int(b)

c=addition()#obtain result from function
print("The Adition=",c)