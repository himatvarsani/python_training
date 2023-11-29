#5 apples  = 1kg
#input the apples
#weight needs to be in kg or lbs
#calculate the weight of all apples

weight = int(input("Enter the number of apples: "))
unit = input ("Enter kgs or lbs: ")
pound = 2.2

print(weight)
print(unit)

if unit == "kgs":
    convert = weight / 5
    print("Your weight is " + str(convert))
elif unit == "lbs":
    convert = weight / 5 * (pound)
    print("Your weight is " + str(convert))
else:
    print("That is not a valid input. Please try again.")

