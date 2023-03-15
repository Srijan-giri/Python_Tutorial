# function insdide function
# greater(a,b) ----> a or b
# greater(a or b,c)------> greatest

def greater(a,b):
    if a>b :
        return a
    else:
        return b
def new_greatest(a,b,c):
    # bigger = greater(a,b)
    return greater(greater(a,b),c)

print(new_greatest(10,20,30))


# Exercise

def is_palindrome(str):
    if str[-1::-1] == str:
        return "Palindrome"
    else:
        return "not Palindrome"


str=input("Enter the string : ")
str=str.lower()
print(f'{str} is {is_palindrome(str)}')





