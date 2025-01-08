def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return "Zero Division Error"
    return x/y
def calculator():
    print("Welcome to Mini Calculator")
    print("operations")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    while True:
        choice=input("enter operation number(1-5:)").strip()
        if choice=="5":
            print("Thank you for using this calculator!")
            break
        if choice not in['1','2','3','4']:
            print("invalid operation! try again")
            continue
        try:
            num1=float(input("Enter First Value:"))
            num2=float(input("Enter Second Value:"))
        except ValueError:
            print("Invalid input please valid input")
            continue
#perform calculations based on numbers
        if choice == '1':
            result = add(num1,num2)
            operation = '+'
        elif choice == '2':
            result = sub(num1,num2)
            operation = '-'
        elif choice == '3':
            result = mul(num1,num2)
            operation = '*'
        else:# choice == '4'
            result == div(num1,num2)
            operation == '/'
        #display result
        if isinstance(result,str): #Error message for division by zero
            print(result)
        else:
            print("{} {} {}={}".format(num1,operation,num2,result))
if __name__=="__main__":
    calculator()

