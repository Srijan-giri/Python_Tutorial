# check two conditions at same time
# and , or

name = 'abc'
age=19

if name=='abc' and age==19:
    print('condition true')  ## yes
else:
    print('condition false')

if name == 'abc' and age == 23:
    print('condition true')
else:
    print('condition false') ## yes



if name == 'abc' or age == 23:
    print('condition true')# yes
else:
    print('condition false')

if name == 'acb' or age == 23:
    print('condition true')
else:
    print('condition false')#yes




# Exercise

name,age=input("Enter your name and age:").split(",")
age=int(age)

if (name[0]=='A' or name[0]=='a') and age>=10:
    print('you can watch coco movie')
else:
    print('sorry,you cannot watch movie')

