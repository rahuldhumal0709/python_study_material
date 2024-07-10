class shape:
    def triangle(self):
        Breadth=int(input("Enter Breadth of triangle: "))
        Height=int(input("Enter Height of triangle :"))
        Area_of_triangle =1/2*(Breadth * Height)  # Area of triangle
        return ("Area of triangle",Area_of_triangle)
    def squre(self):
        area=int(input("Enter area : "))
        Area_of_squre =(area**2)     # Area of squre
        return ("Area of Squre",Area_of_squre)
    def circle(self):
        radius=int(input("Enter radius of circle: "))
        Area_of_circle = 3.14 * (radius**2)     # Area of circle
        return ("Area of circle",Area_of_circle)
s =shape()
print(s.triangle())
print(s.squre())
print(s.circle())