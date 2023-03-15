#data structure
#List
# Ordered collection of items

# You can store anything in the lists int,float,string

numbers=[1,2,3,4]
print(numbers)

words=["word1",'word2','word3']
print(words)

# diff between None and 0 is none means kuch nehi
mixed=[numbers,words,'five','six',2.3,None]
print(mixed)



# acces the elements in the list
print(numbers[1])
print(numbers[0:2])
print(numbers[-1])

numbers[3]=5
print(numbers)
numbers.append(10)
print(numbers)


m = [1,2,3,4,'five','six',2.3,None]
print(m[-1])

print(m[1:])
# m[1:]="String"
m[1:]=["three","four"]
print(m)