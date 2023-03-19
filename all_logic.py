""" This is for to calaculate the sum of digit,to find out Armstriong or not
    To get the reverse number of given number,To find the number is palindrom or not"""
def sum_of():#defination of function
    num=(int(input("Enter the number to calculate the sum of digit")))
    temp=num
    sum=0
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
    print("The sum of digit",temp,"is",sum)

def Armstrong():#defination of function
    num=(int (input("Enter the number to check the number is armstrong or not")))
    temp=num
    sum=0
    while num>0:
        rem=num%10
        sum=sum+(rem*rem*rem)
        num=num//10
    if sum==temp:
        print("The number",temp,"is Armstrong")
    else:
        print("The number",temp,"is not Armstrong")

def rev():#defination of function
    num=(int (input("Enter the number to reverse")))
    temp=num
    rev=0
    while num>0:
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    print("The",temp,"by reverse is ",rev)

def palin():#defination of function
    num=(int (input("Enter the number to check the given number is palindrom or not")))
    temp=num
    rev=0
    while num>0:
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    if temp==rev:
        print("The number",temp,"is an Palindrom")
    else:
        print("The number",temp,"is not Palindrom")
    

print("To find sum of digit")
sum_of()#function call
print("To find the Armstrong or not")
Armstrong()#function call
print("To find the Reverse number")
rev()#function call
print("To find the number is palindrom or not")
palin()#function call