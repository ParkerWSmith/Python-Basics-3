#Parker Smith
#1/9/2018
#CCIS 1505-02
#Program 3

#Name
strFname = input("What is your first name?")
strMname = input("What is your middle name?")
strLname = input("What is you last name?")
print("Your name is: "+ strFname.lower() + " " + strMname.lower() + " " + strLname.lower())

#Age
strAge = input("How old are you?")
intAge = int(strAge)
intAgeDbl = intAge * 2
print ("Your age doubled is:", intAgeDbl)


#Add
intAdd1 = int(input("Enter a number:"))
intAdd2 = int(input("Enter another number:"))
intAdd = intAdd1 + intAdd2
print("The sum of these numbers is:", intAdd)

#Sub
intSub1 = int(input("Enter a number:"))
intSub2 = int(input("Enter another number:"))
intSub = intSub1 - intSub2
print("The difference of these numbers is:", intSub)

#Mult
intMult1 = int(input("Enter a number:"))
intMult2 = int(input("Enter another number:"))
intMult = intMult1 * intMult2
print("The product of these numbers is:", intMult)

#Div
intDiv1 = int(input("Enter a number:"))
intDiv2 = int(input("Enter another number:"))
intDiv = intDiv1 / intDiv2
print("The quotient of these numbers is:", intDiv)

#Power of 10
intPower = int(input("Enter a number:"))
intTotal = intPower**intPower
print("The number raised to the power of 10 is:", intTotal)

#Average
intAve1 = int(input("Enter a number:"))
intAve2 = int(input("Enter another number:"))
intAve3 = int(input("Enter another number:"))
intMean = (intAve1 + intAve2 + intAve3) / 3
print("The average of these numbers is:", intMean)

#Temp
intF = int(input("Enter a temperature in fahrenheit:"))
intC = (intF - 32)*5/9
print("Temperature in Celsius is:", intC)
