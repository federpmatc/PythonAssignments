#As indicated on lines 38 and 40, you will need to create a dictionary with your name and then add it to the employees list.
###########################

#The last 2 lines of code automatically print our the first names from every dictionary in the list,
#so your instructor will be able to tell if you did this correctly


#define a dictionary (key/value) pair
pat = {}
pat['first'] ='Pat'
pat['last'] = 'Feder'
#print the dictionary
print([pat])

steve = {}
steve['first'] ='Steve'
steve['last'] = 'Webster'
print([steve])

brian = {}
brian['first'] ='Brian'
brian['last'] = 'Kirsch'
print([brian])

#Access items in the dictionary
print(pat.get("first"))
print(steve.get("first"))
print(brian.get("first"))

#define a list of dictinaries ... yikes :)
employees = [pat, steve, brian]
#print the list out, which contains multiple dictionaries
#print list of dictionaries out
print(employees)

#Add someone new to the list
employees.append (
    {'first': 'Bill', 'last': 'Gates'})
###################################################
#Create a dictionary with your first and last name

#add the dictionary with your first and last names to the employees list

#The following will print the first name of every person in the list
print("Here are first name values for all dictionaries in our employees list")
for employee in employees:
    print(employee.get("first"))
