#This is kind of tricky..

#You will update/modify the program below to complete the following
# ask a user to enter their first name and store it in a variable
# ask a user to enter their last name and store it in a variable
# ask the user how many cups of coffee that they have had today
# ask the user how many cups of coffee that they had yesterday
#calculate the total number of cups of coffee by adding the 2 numbers together

# print out hello followed by their full name you have drank XX cups of coffee in the last two days!!!

# Make sure you have that your sentence is formatted correctly with appropriate number of spaces
# Make sure the first letter of first name and last name is uppercase
# Make sure the rest of the name is lowercase
###############################################################################################
#The program below is close but will require some modfication

first_name = input('What is your first name? ')

coffee_yesterday = input("How many cups of java yesterday? ")
total_coffee = int(coffee_yesterday)

print("Hello " + first_name.capitalize() + ' ' + " you drank " + str (total_coffee) + " of coffee yesterday" )
