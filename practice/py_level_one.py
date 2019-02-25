# String
x = "Name: {b} Name: {a}".format(a = "Sagar", b = "Suvash")
print(x)

#list
my_list = [3, 'A', "Sagar", True]
print(my_list)
print(len(my_list))

my_list.append("Suvash")
print(my_list)

second_list = [3,5,6]
# use extend to merge the elements of the second list into the original list
my_list.extend(second_list)
print(my_list)

popped_item = my_list.pop()
print(my_list)
print(popped_item)

my_list.reverse()

print(my_list)

#LIST COMPREHENSION
matrix = [[1,2,3], [4,5,6],[7,8,9]]
first_row = [row[0] for row in matrix]
print(first_row)

# dictionary

my_day = {"breakfast": "eggs", "lunch": "noodles"}
# add a new entry (key-value pair)
my_day["dinner"] = "rice"
print(my_day["lunch"])
print(my_day)

# tuple - they are immutable
t = (1,2,3)
print(t)

#sets
s = set()
s.add(1)
s.add(3)
s.add(3)
s.add(5)
print(s)

second_set = set([1,2,3,4,5,5,6,7,6])
print(second_set)
