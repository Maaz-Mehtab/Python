# Q5)Write a Python program which accepts the user's first and last name and
# print them in reverse order with a space between them.

firstName = raw_input("Enter your First Name : ")
lastName = raw_input("Enter your Last Name : ")
print(firstName+" "+lastName)
fullName=firstName+" "+lastName
reverseOrder = fullName[::-1]
print(reverseOrder)
