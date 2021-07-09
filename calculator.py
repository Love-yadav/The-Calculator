# today we are making the calculator with the help of the python programming
def addition(n1,n2):
    c=n1+n2
    return c

def substraction(n1,n2):
    c=n1-n2
    return c

def multiplication(n1,n2):
    c=n1*n2
    return c

def division(n1,n2):
    c=n1/n2
    return c

if __name__=='__main__':
    print("*******************************welome to our calculator************************************")
    print("*******************************author:-Mr. love yadav********************************")
    n1=int(input("enter your first number:"))
    n2=int(input("enter your second number:"))

    print("select an option")
    print("1. addition")
    print("2. substraction")
    print("3. multiplication")
    print("4. division")
    print("\n")
    option=int(input("select the number from above options:"))
    
    if option==1:
        print(f"your answer is:{addition(n1,n2)}")
    elif option==2:
        print(f"your answer is:{substraction(n1,n2)}")
    elif option==3:
        print(f"your answer is:{multiplication(n1,n2)}")
    elif option==4:
        print(f"your answer is:{division(n1,n2)}")
    else:
        print("you choose wrong number:")
    
    print("*********************Thanks for using our calculator***************************")