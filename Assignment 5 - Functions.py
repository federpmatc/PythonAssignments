# The function below accepts three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'sub'
# the function returns the result of the two numbers added or subtracted based on the value passed in for the operator

#Your assignment - 
#1.)  Add a div and mult operation
#2.)  Fix the if/else errors on lines 41, 42 and 43 so that check_number functio verifies that the user enters numeric values
#3.)  Test your code with the mult and div operators.  Also test your code with bad numeric values

def check_number(test_string):
# Check for float string 
    try :  
        float(test_string) 
        return(True)
    except : 
        return(False)

def calculator(first_number, second_number, operation):
    if operation.upper() == 'ADD':
        return(float(first_number) + float(second_number))
    elif operation.upper() =='SUBTRACT':
        return(float(first_number) - float(second_number))
    else:
        return('Invalid operation please specify add or sub')

    
# Test the function with the values 6,4, add 
print('Adding 6 + 4 = ' + str(calculator(6,4,'add')))
# Test the function with the values 6,4, subtract 
print('Subtracting 6 - 4 = ' + str(calculator(6,4,'subtract')))
# Test your function with the values 6,4, divide 
print('Dividing 6 / 4 = ' + str(calculator(6,4,'div')))
# Test your function with the values 6,4, mult 
print('Dividing 6 / 4 = ' + str(calculator(6,4,'mult')))

first_number = input('Enter a number ')
second_number = input('Enter a number ')
operation = input('Enter the operation add, sub, mult or div ')
if check_number(first_number) = True and check_number(second_number) = True :
    answer = calculator(first_number, second_number, operation)
    print(first_number + ' ' + operation + ' ' + second_number + ' = ' + answer )
else:
    print("Dude make sure to enter actual numbers")
