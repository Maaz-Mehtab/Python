# Question5 Guess the number game
# Write a program which randomly generate a number between 1 to 30 and ask the user in input field to
# guess the correct number. Give three chances to user guess the number and also give hint to user if
# hidden number is greater or smaller than the number he given to input field.


import random
count=0
random_number=random.randint(1, 30)

def main():
    global count
    if count <3:
        x=int(input('Guess a number one through one hundred'))
        if x !="":
            count = count +1
            print("count ",str(count))

            if x == random_number:
                print("You got it!")
            elif x > random_number:
                print("too high")
                main()
            else:
                print("too low")
                main()
    else:
        print("your game is end")
        exit()
main()
