import random

# winning_number=43
winning_number=random.randint(1,100)
guess=1
number = int(input("Guess a number between 1 and 100 : "))
game_over=False
while not game_over:
    if number == winning_number:
        print(f"you win and you guessed this number in {guess}times")
        game_over=True
        # Win
    else:
        if winning_number>number:
            print('too low')
            # guess+=1
            # number = int(input("Guess again :"))
            # low guess
        else:
            print('too high')
            # guess+=1
            # number = int(input("Guess again :"))
            # High guess
        guess += 1
        number = int(input("Guess again :"))
        #guess wrong


# DRY - Dont Repeat Yourself


# import random
#
# number = int(input("Enter the number  within 1 to 50: "))
# winning_number = random.randint(1,50)
# guess=1
# game_over = False
# while not game_over:
#     if number == winning_number:
#         print(f'you win and you guessed this number {guess} times')
#         game_over = True
#     else:
#         if number<winning_number:
#             print('Number is too low')
#             guess += 1
#             number=int(input("Guess again : "))
#         else:
#             print('Number is too high')
#             guess += 1
#             number = int(input("Guess again : "))