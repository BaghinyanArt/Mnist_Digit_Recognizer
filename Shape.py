class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def display_info(self):
        return (f"Name      : {self.__class__.__name__}\n"
                f"Area      : {self.calculate_area()}\n"
                f"Perimeter : {self.calculate_perimeter()}\n")
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius**2)
        
    def calculate_perimeter(self):
        return 3.14 * (self.radius*2) 
    
    def display_info(self):
        return super().display_info() + f"Radius    : {self.radius}\n"
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width) 
        
    def display_info(self):
        return super().display_info() + f"Length    : {self.length}\nWidth     : {self.width}\n"
                                        
class Triangle(Shape):
    def __init__(self, ab, bc, ca):
        self.ab = ab
        self.bc = bc
        self.ca = ca

    def calculate_area(self):
        p = (self.ab + self.bc + self.ca) / 2
        return (p * (p - self.ab) * (p - self.bc) * (p - self.ca)) ** 0.5

    def calculate_perimeter(self):
        return self.ab + self.bc + self.ca
        
    def display_info(self):
        return super().display_info() + f"Side 1    : {self.ab}\nSide 2    : {self.bc}\nSide 3    : {self.ca}\n"

def process_shapes(shapes_list):
    largest_shape = None
    largest_area = -float('inf')
    
    for shape in shapes_list:
        shape.calculate_area()
        shape.calculate_perimeter()
        print(shape.display_info())

        area = shape.calculate_area()
        if area > largest_area:
            largest_area = area
            largest_shape = shape

    return largest_shape

c = Circle(2)
r = Rectangle(6, 8)
t = Triangle(3, 4, 5)
 
shapes_list = [c, r, t]

largest_shape = process_shapes(shapes_list)

print("Shape with the largest area:")
print(largest_shape.__class__.__name__)
