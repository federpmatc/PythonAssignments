# The function below accepts three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'sub'
# the function returns the result of the two numbers added or subtracted based on the value passed in for the operator

#Your assignment - 
#1.)  Add a div and mult operation

#2.)  Use the function below to verify that the user enters a numeric value
def check_number(test_string):
# Check for float string 
    try :  
        float(test_string) 
        return(True)
    except : 
        print("Not a float") 
        return(False)

def calculator(first_number, second_number, operation):
    if operation.upper() == 'ADD':
        return(float(first_number) + float(second_number))
    elif operation.upper() =='SUBTRACT':
        return(float(first_number) - float(second_number))
    else:
        return('Invalid operation please specify add or sub')

    
# Test your function with the values 6,4, add 
# Should return 10
#
print('Adding 6 + 4 = ' + str(calculator(6,4,'add')))
# Test your function with the values 6,4, subtract 
# Should return 2
print('Subtracting 6 - 4 = ' + str(calculator(6,4,'subtract')))
# Test your function with the values 6,4, divide 
# Should return some sort of error message
print('Dividing 6 / 4 = ' + str(calculator(6,4,'divide')))
