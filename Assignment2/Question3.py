# Question 3. Write a program which print the length of the list?
test_list = [ 1, 4, 5, 7, 8 ] 
print ("The list is : " + str(test_list)) 
counter = 0
for i in test_list: 
    counter = counter + 1
print ("Length of list using naive method is : " + str(counter))