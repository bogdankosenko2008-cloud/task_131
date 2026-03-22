import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        p = self.perimeter() / 2
        if (self.a + self.b <= self.c or
                self.a + self.c <= self.b or
                self.b + self.c <= self.a):
            return None
        p = self.perimeter() / 2
        value = p * (p - self.a) * (p - self.b) * (p - self.c)
        if value < 0:
            return None
        return math.sqrt(value)

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a, self.b = a, b
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.b

class Trapeze(Shape):
    def __init__(self, a, b, c, d):
        self.a, self.b = a, b  # основи
        self.c, self.d = c, d  # бокові сторони
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        try:
            p = self.perimeter() / 2
            value = ((p - self.a) * (p - self.b) * (p - self.a - self.b)) / (self.a + self.b)
            if value <= 0:
                return None
            h = math.sqrt(value)
            return (self.a + self.b) / 2 * h
        except:
            return None
class Parallelogram(Shape):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h
        def perimeter(self):
            return 2 * (self.a + self.b)
        def area(self):
            return self.a * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        return 2 * math.pi * self.r
    def area(self):
        if self.r <= 0:
            return None
        return math.pi * self.r ** 2
def create_shape(line):
    parts = line.strip().split()
    name = parts[0]
    params = list(map(float, parts[1:]))
    if name == "Triangle":
        return Triangle(*params)
    elif name == "Rectangle":
        return Rectangle(*params)
    elif name == "Trapeze":
        return Trapeze(*params)
    elif name == "Parallelogram":
        return Parallelogram(*params)
    elif name == "Circle":
        return Circle(*params)
    else:
        return None

shapes = []
with open("input01.txt", "r") as file:
    for line in file:
        shape = create_shape(line)
        if shape:
            shapes.append(shape)
valid_shapes = [s for s in shapes if s and s.area() is not None]
print(max(valid_shapes, key=lambda s: s.area()).area())
print(max(valid_shapes, key=lambda s: s.perimeter()).perimeter())
