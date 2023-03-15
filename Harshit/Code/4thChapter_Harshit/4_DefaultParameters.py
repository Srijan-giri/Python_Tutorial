#default parameters


# here age is a default parameter
#21---> override 23
# None ----> special value of python , jiska matlab kuch nehi

# def user_info(first_name,last_name,age=23):
# def user_info(first_name='unknown',last_name='unknown',age=None):
def user_info(first_name='unknown',last_name='unknown',age=None):
    print(f'Your first name is : {first_name}')
    print(f'Your last name is : {last_name}')
    print(f'your age is {age}')

# user_info("Srijan","Giri",21)
# user_info("Srijan","Giri")
# user_info("Srijan","Giri")
# user_info()
user_info(first_name="Harshit",age=24) # error
