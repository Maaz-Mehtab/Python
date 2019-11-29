# Question 2:  Write a program which take input from user and identify that the given
# number is even or odd?

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))