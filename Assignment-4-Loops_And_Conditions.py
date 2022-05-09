#Figure out what the program below does
#Add Comments to it so that your instructor can tell that you understand what program does

#In this activity you will need to update the code to print out the total number of guesses

names = []

print("I'm thinking of someone's name, see if you can guess it")

name = input("Enter someone's name ")
while name != "Pat":
	names.append(name)
	name = input("Nope! Guess again....Enter a name ")

########## Add code to printout the number of guesses ###########################

print("Here are the names that you guessed incorrectly:")
for guesses in names:
	print("     " + guesses)

