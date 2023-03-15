# for loop with range function

for i in range(1,11,1): # i ---> 0 to 9,1 to 10
    print(f'Hello world : {i}')

string="Srijan"
for i in string :
    print(f'{i}:')

# Example 1
# sum from 1 to 10 :

# sum=0
# for i in range(1,11,1):
#     sum=sum + i
# print(sum)

# n = int(input('Enter the number :'))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum + i
# print(sum)


# Example 2 :

# n = input('Enter the number :')
# sum=0
# for i in range(0,len(n)):
#     sum=sum + int(n[i])
# print(sum)


# Example 3

name = input('Enter the string :')
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        temp = temp+name[i]
        print(f'{name[i]}: {name.count(name[i])}')
