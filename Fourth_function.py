#4.Function With Arguments With Return

def addition(a,b):#defination of function
    return int(a)+int(b)

p,q=input("Enter the value of a&b=").split()
print("The addition=",addition(p,q))# call of function