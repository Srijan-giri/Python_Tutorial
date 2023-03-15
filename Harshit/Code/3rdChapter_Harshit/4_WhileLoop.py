#loops
# While loop,for loop

#print("Hello world") #10 times

# i=1   #initialize
# while i<=10: # condition
#     print(f"Hello world {i}")
#     i=i+1 #increment or decrement
#
# print(i)
# hello world


# sum : 1 to 10

sum=0
i=1
while i<=10:
    sum=sum+i
    i=i+1
print(f'Sum of 1 to 10 is {sum}')



# Exercise 1 :

n =int(input('enter the n number :'))
i=1
s1=0
while i<=n:
    s1=s1+i
    i=i+1
print(f'Sum of n natural numbers are {s1}')


# Exercise2 :

n1=input("Enter a number containing more than one digit : ")
#"1256"
# int(n1[i])---->length
s2=0
i=0
while i<len(n1):
    s2=s2+int(n1[i])
    i=i+1
print(f'sum of this number :{s2}')


#Example - 3

n2=input("Please enter your name : ")
#harshit vashisth


#harshit
#name.count('h'), name.count(name[0]) =2
#name.count('a'),name.count(name[1]) = 1
#name.count('r'),name.count(name[2]) = 1
#name.count('s'),name.count(name[3]) = 1
#name.count('h'),name.count(name[4]) = 2
#name.count('i'),name.count(name[5]) = 1
#name.count('t'),name.count(name[6]) = 1

#output :
#name[0] = h : 2
#a : 1
#r : 1
# s : 1
#h : 2
#i : 1
#t : 1

i=0
temp_var=""
while i<len(n2):
    if n2[i] not in temp_var:
        temp_var=temp_var+n2[i]
        print(f'{n2[i]} : {n2.count(n2[i])}')
    i=i+1


