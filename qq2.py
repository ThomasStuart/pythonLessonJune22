class Circle:

    def __init__(self, name, radius):
        self.name   = name
        self.radius = radius

    def getArea(self):
        area =  3.14 * (self.radius * self.radius)
        return area

    def getPerimeter(self):
        perimeter = 2  * 3.14  * self.radius
        return perimeter

# END CLASS


# object 1
circle1 = Circle("circle1", 5)
print( circle1.name )

# Get area
print( "Get area ", circle1.getArea() )
