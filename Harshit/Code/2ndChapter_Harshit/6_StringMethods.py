# String Methods

name = "HARshit Vashistha"


#1 . len() function

print(len(name))
print(len("harshit"))
print(len("Srijan"))

#2 . lower() method

print(name.lower())
print(name)


#3. upper() method

print(name.upper())


#4. title() method

print(name.title())

# 5. count() method

print(name.count('h'))
print(name.count('H'))

#Exercise

name,char = input("Enter your name and a character : ").split(",")
print(f'Length of your name is : {len(name)} ')
print(f'Character count is : {name.count(char)} , case sensitive ')  # case sensitive
print(f'Character count is : {name.lower().count(char.lower())},case insensitive')  # case insensitive

# Harshit - harshit
# H-h

# name.lower().count(char.lower())
