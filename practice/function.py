def add(a,b):
    """
    Adds two numbers
    """
    return a+b

print(add(2,22))

#Lamda Expressions
my_list = [1,2,3,4,5,6,7,8,9]

x = filter(lambda num: num%2==0, my_list)
print(list(x))
