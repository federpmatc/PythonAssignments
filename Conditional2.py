# When you join a hockey team you get your name on the back of the jersey
# but the jersey may not be big enough to hold all the letters
# Ask the user for their first name
first_name = input('Please enter your first name: ')
first_length = len(first_name)

# Ask the user for their last name
last_name = input('Please enter your last name: ')
last_length = len(last_name)

print("Hello " + first_name + ' ' + last_name)
print("Your first name is " + str(first_length) + " characters long")

print("Your initials are " +   first_name[0:1] + " " +last_name[0:1])

# if first name is < 10 characters and last name is < 10 characters 
#       print first and last name on the jersey
# if first name >= 10 characters long and last name is < 10 characters
#       print first initial of first name and the entire last name
# if first name < 10 characters long and last name is >= 10 characters
#       print entire first name and first initial of last name
# if first name >= 10 characters long and last name is >= 10 characters
#       print last name only

# Test with the following values
# first name: Susan  last name: Ibach
# output: Susan Ibach
# first name: Susan  last name: ReallyLongLastName
# output: Susan R.
# first name: ReallyLongFirstName  last name: Ibach
# output: R. Ibach
# first name: ReallyLongFirstName  last name: ReallyLongLastName
# output: ReallyLongLastName
