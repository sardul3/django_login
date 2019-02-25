list = [1,2,3,4,5,6]

for item in list:
    print(item*3)

# conditionals
if 1<2:
    if 11>3:
        print('I am sane')
    elif 11=="11":
        print("Let me think")
    else:
        print("LOL")

# Tuple Unpacking
my_pair = [(1,2), (3,4), (5,6)]

for items in my_pair:
    print(items)

for tup1, tup2 in my_pair:
    print(tup2)
    print(tup1)
