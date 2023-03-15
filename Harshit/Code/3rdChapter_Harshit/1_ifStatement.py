#syntax
#if condition
#     #code #if condition is true then this code will execute
#     # code

# age =int(input("enter your age : "))
# if age>=14:
#     print("you are above 14")


# pass statement

# x=18
# if x>18:
#     pass  # if i dont want to write anything then i can write this pass statement

# if-else statement

# age =int(input("enter your age : "))
# if age>=14:
#     print("you are above 14")
# else:
#     print("you are not above 14")
#
#
# year = int(input("Enter the year :"))
# if year%400==0 :
#     print(f'{year} is a leap year')
# elif year%100==0:
#     print(f'{year} is not a leap year')
# elif year%4==0 :
#     print(f'{year} is  a leap year')
# else:
#     print(f'{year} is not a leap year')
#


# Exercise
#Number Guessing Game
# user_input = int(input("guess a number b/w 1 and 100 : "))
# winning_number = 27
# if user_input == winning_number:
#     print("You win !!!")
# else:
#     if user_input<winning_number:
#         print("too low")
#     else:
#         print("too high")
#


# if elif else statements

#show ticket pricing
#0 to 3 (free)
#4 to 10 (150)
#11 to 60(250)
#above 60(200)

user_age=int(input("Enter your age : "))
if user_age >=0 and user_age<=3:
    print('free')
elif 4<user_age<=10:
    print('150')
elif user_age>=11 and user_age<=60:
    print('250')
else:
    print('200')

