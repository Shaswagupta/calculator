import logo
print(logo.calculator_logo)
def calculation ( number,number2):
    operation = input("""choose the operation which you want to perform on numbers:
                    '+' for adding ,
                    '-' for subtracting ,
                    '*' for multiplication ,
                    '/' for divide 
""")
    if operation == "+":
        return number + number2
    elif operation == "-":
        return number - number2
    elif operation == "*":
        return number * number2
    elif operation == "%":
        return number % number2
    else :
        return 0 

num1 = int(input("enter a  1st number : "))
num2 = int(input("enter a  2nd number : "))
result = calculation(num1,num2)
should =True

while should:
    
    play_more = input("want perform operation on more number \n     'yes' or 'no' \n        ") 
    if play_more =="yes":
        # while should :
            print(f"so the result is {result}")
            num3 = int(input("enter a number :"))
            result = calculation(result,num3)
            print(f"so the result is {result}")
    else :
        should = False
        print(f"so the result is {result}")        


  
