# ============================================+
# Distance Calculator Program
# Converts distances from kilometers to miles.
# ============================================+

# x was the previous variable name, change it to kilometers because it asks the
# user to input the distance in km.
kilometers = float(input("Enter distance in kilometers: "))

# y was the previous variable name, change it to km2miles (short for kilometers to
# miles) to know that the conversion factor of km to miles is 1 km = 0.621371 miles.
km2miles = 0.621371

# z was the previous variable name, change it to miles to know that the formula for
# getting miles is km * 0.621371
miles = kilometers * km2miles

# Outputs the conversion of kilometers to miles.
print(f"Distance of {kilometers} kilometers in miles is {miles} miles.")

# Asks the user if they want to convert another distance. If yes, it will ask for 
# the distance in kilometers again and perform the conversion. If no, it will end 
# the program. Change the variable name from a to reconvert to know that it is 
# asking the user if they want to convert another distance.
reconvert = input("Do you want to convert another distance? (yes/no): ").strip().lower()

# If the user wants to convert another distance, it will ask for the distance in 
# kilometers again and perform the conversion. If not, it will end the program.
# Change the variable name from q to kilometers to know that it is asking the user
# to input the distance in km again. Change the variable name from r to miles to 
# know that it is performing the conversion of km to miles again.
if reconvert == "yes":
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * km2miles
    print(f"Distance of {kilometers} kilometers in miles is {miles} miles.")

else:
    print("Program ended.")