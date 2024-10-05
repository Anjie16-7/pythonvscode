
#1.Write a Python program that checks if a given number is positive, negative, or zero and prints the result.

# num=input("Enter Number Here:")
# num2=int(num)
# if num2>0:
#     print('This number is even')
# if num2<0:
#     print('This number is odd')
# if num2==0:
#     print('This number is zero')

#Create a Python function that takes two numbers as input and prints the greater number. If the numbers are equal, print "Both numbers are equal".

# num1=int(input("Enter First Number:"))
# num2=int(input("Enter Second Number"))
# if num1>num2:
#     print(num1,"is greater than",num2)
# if num1<num2:
#     print(num2,"is greater than",num1)
# if num1==num2:
#     print("Both numbers are equal")

#Write a Python script that asks the user for their age and prints "Eligible to vote" if they are 18 or older. Otherwise, it prints "Not eligible to vote".

# age=int(input("Enter age:"))
# if age<18:
#     print("Not eligible to vote")
# if age>18:
#     print("You are eligible to vote")

#Write a Python program that checks if a year is a leap year. A year is a leap year if it is divisible by 4, but not divisible by 100, unless it is also divisible by 400.

# year=int(input("Enter year:"))
# test1=year%4
# test2=year%100
# if test1==0 and test2!=0:
#     print("It's a leap year")
# else:
#     print("It's not a leap year")

#Create a Python program that accepts a student's score as input and prints "Pass" if the score is 50 or higher and "Fail" otherwise.

# score=int(input("Enter score:"))
# if score>50:
#     print("You passed!")
# else:
#     print("You did not pass")

#Write a Python script to add two lists element-wise. For example, given lists `[1, 2, 3]` and `[4, 5, 6]`, the result should be `[5, 7, 9]`.

list=["1","2","3"]
list2=["4","5","6"]

first=int(list[0])+int(list2[0])
second=int(list[1])+int(list2[1])
third=(list[2])+list2[2]
print(first,second,third)