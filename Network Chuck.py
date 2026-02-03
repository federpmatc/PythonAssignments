import os #import the builtin OS module, which contains functions to interact with OS 

os.system('clear')  #send clear command to OS (change this to CLS for Windows)
###in class, change to cls, which clears the console in Windows

# --- STEP 1: GREETING AND NAME CAPTURE ---


print("\n\nHello, welcome to Network Chuck Coffee!!!!!!!!!!")
name = input("What is your name?\n")

# --- STEP 2: THE BOUNCER LOGIC (Logical Operators) ---
# We check if the customer is one of the "evil" ones
if name == "Ben" or name == "Patricia" or name == "Lokey":
    evil_status = input("Are you evil?\n")
    # If they are evil, they need 4 or more good deeds to enter
    good_deeds = int(input("How many good deeds have you done today?\n"))

    if evil_status == "yes" and good_deeds < 4:
        print("You're not welcome here, " + name + "!! Get out!!")
        exit()
    else:
        print("Oh, so you're one of those good ones. Come on in!")
else:
    print("Hello " + name + ", thank you so much for coming in today!")

# --- STEP 3: THE MENU AND ORDERING ---
menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappuccino"
#print(name + ", what would you like from our menu today? Here is what we are serving:\n" + menu)

###in class - convert the above to an fstring
###in class - as them after Black Coffee, if they want cream (it costs .25 extra)
###in class - maybe ask about almond milk with their latte's, charge them $1

order = input()

# --- STEP 4: DYNAMIC PRICING (If/Elif Logic) ---
# Prices vary based on the specific order
if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    # Optional challenge: Whipped cream increases latte price
    whipped_cream = input("Do you want extra whipped cream?\n")
    if whipped_cream == "yes":
        price = 11
    else:
        price = 9
elif order == "Cappuccino":
    price = 10
else:
    print("Sorry, we don't have that here.")
    price = 0
    exit()

# --- STEP 5: QUANTITY AND MATH ---
quantity = input("How many " + order + "s would you like?\n")

# Calculate total (converting quantity string to integer)
total = price * int(quantity)

# --- STEP 6: FINAL CONFIRMATION ---
# Convert total back to string to concatenate for the final message

###inclass convert lines 68 & 69 to fstrings
print("Sounds good " + name + ", we'll have your " + quantity + " " + order + "(s) ready in a moment.")
print("Your total is: $" + str(total))