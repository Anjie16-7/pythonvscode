#Converting data from one type to another

# types of data

# 1. integer == whole numbers
# 2. string == Anything in quotes
# 3. float == decimal
# 4.boolean == True or False

# Method 1:
score = int('60')#convert the original data before storing in the variable

# Method 2:
score = '60' #keep original state of data
score2 = int(score) #create a new variable to save a diff data type
print(score) #str
print(score2) #int

#int, float, str, bool

#please note, the default data type for input is a STRING

# classwork:


# convert these to float or integer or string using a new variable
#print and all must run and display well

score = 75.9
score2=str(score)
print(score2)

age = 12
age2= float(age)
print(age2)

height = 9.7
height2=str(height)
print(height2)

weight = "75.9"
weight2=float(weight)
print(weight2)

weight2 = int(weight) #integer

reject = False

# convert these to float or integer or string without using a variable

age = int(27.8)

allow = float(True)

reject = int(False)

weight = str(170.989687967567)

date = int(2023.8)

average = float(75)


#Ask the user to enter any 3 digit number and mulitply it by 2

num=int(input("Enter a 3 digit number: "))
ans= num*2
print(ans)

#Ask the user to enter a word and then convert it to a boolean
word=bool(input("Enter a word: "))


"""
create a python program to ask the daily sales of a store which as the following departments (food, clothings, equipments, bags and books).
 Then get the total sales 
"""

print("Hello! Please enter the number of sales here.")

food=int(input("Enter food sales here: "))
cloth=int(input("Enter clothing sales here: "))
equip=int(input("Enter equipment sales here:"))
bag=int(input("Enter bages sold here: "))
book=int(input("Enter books sold here:"))
total=food+cloth+equip+bag+book
print("The total sales is ",total)




num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
total= num1+num2
print("The total is: ",total)
