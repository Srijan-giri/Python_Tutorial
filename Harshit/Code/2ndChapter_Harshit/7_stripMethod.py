

name = "    Harshit    "
dots=".................."

#lstrip() method
print(name)
print(name+dots)
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)

name1="    Har    shit    "
print(name1.strip()+dots)
print(name1.replace(" ","")+dots)


name,char = input("Enter your name and a character : ").split(",")
print(f'Length of your name is : {len(name)} ')
print(f'Character count is : {name.count(char)} , case sensitive ')  # case sensitive
print(f'Character count is : {name.strip().lower().count(char.strip().lower())},case insensitive')  # case insensitive



