import string

# replace() method

string1 = "she is beautiful and she is good dancer"
# print(string1.replace(" ","_"))
# print(string1.replace("is","si"))
# print(string1.replace("is","was"))
print(string1.replace("is","was",1))
print(string1.replace("is","was",2))



# find() method

# print(string1.find("is"))
# print(string1.find("is"))
# print(string1.find("is",1))
# print(string1.find("is",12))

is_pos1 = string1.find("is")
is_pos2 = string1.find("is",is_pos1+1)
print(is_pos1)
print(is_pos2)


# center method

name="harshit"
# **harshit**,11----> 7 +4 (quote)
print(name.center(11,"*"))
print(name.center(9,"*"))


# user=input("enter your username : ")
# length=len(user)
# print(user.center(length+8 , "*"))



# String are immutable
string="string"
print(string.replace('t','T')) # it does not effect on the originl string so it is immutable
print(string)