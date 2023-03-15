# scope

x=5  # global variable
def func():
    global x
    x=7 # local variable ---> scope inside
    return x

# def func2():
#     print(x)

print(x)
print(func())
print(x)