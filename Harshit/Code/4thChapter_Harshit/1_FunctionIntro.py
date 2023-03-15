# functions

# name = "harshit"
# print(len(name))  # inbuilt function

# def is a keywword
def add_two(a,b):
    return a+b

# total = add_two(5,4)
# print(total)

print(add_two(5,4))

# a=int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))
#
# total1=add_two(a,b)
# print(total1)
#
# str1 = input("Enter 1st string : ")
# str2 = input("Enter 2nd string : ")
#
# total2 = add_two(str1,str2)
# print(total2)



# return vs print




def add_three(a,b,c):
    return a+b+c
    # print(a+b+c)


# print(add_three(5,5,5))
add_three(5,5,5)





# function Practise

def last_char(name):
    # return name[len(name)-1]
    return name[-1]

print(last_char("Srijan Giri"))


# def odd_even(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "Odd"

def odd_even(n):
    if n%2==0:
        return "Even"
    return "Odd"
print(odd_even(4))


def song():
    return "Happy Birthday Song"
print(song())



# Exercise

def greater_check(a,b,c):
    if a>b and a>c :
        return a
    elif b>a and b>c:
        return b
    else:
        return c

num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))
num3 = int(input("Enter the 3rd number : "))
print(f'greatest number is {greater_check(num1,num2,num3)}')