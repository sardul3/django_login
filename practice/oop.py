class Friend():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return "Name: {}, Email: {}, Friend".format(self.name, self.email)

saree = Friend("Saransh", "bhandas@gmail.com")
print(saree)



class Circle():
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

my_circle = Circle(5)
print(my_circle.area())
my_circle.set_radius(10)
print(my_circle.area())
