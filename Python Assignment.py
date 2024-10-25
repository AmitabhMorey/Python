# Perimeter and Area of 2D Shapes
Circle = 2*3.14*float(input("Enter the radius of the circle: "))
print("The perimeter of the circle is:", Circle)
print("The area of the circle is:", 3.14*float(input("Enter the radius of the circle: "))**2)

Triangle = float(input("Enter the first side of the triangle: "))+float(input("Enter the second side of the triangle: "))+float(input("Enter the third side of the triangle: "))
print("The perimeter of the triangle is:", Triangle)
print("The area of the triangle is:", 0.5*float(input("Enter the base of the triangle: "))*float(input("Enter the height of the triangle: ")))

Square = 4*float(input("Enter the side of the square: "))
print("The perimeter of the square is:", Square)
print("The area of the square is:", float(input("Enter the side of the square: "))**2)

Rectangle = 2*(float(input("Enter the length of the rectangle: "))+float(input("Enter the breadth of the rectangle: ")))
print("The perimeter of the rectangle is:", Rectangle)
print("The area of the rectangle is:", float(input("Enter the length of the rectangle: "))*float(input("Enter the breadth of the rectangle: ")))

Parallelogram = 2*(float(input("Enter the length of the parallelogram: "))+float(input("Enter the breadth of the parallelogram: ")))
print("The perimeter of the parallelogram is:", Parallelogram)
print("The area of the parallelogram is:", float(input("Enter the base of the parallelogram: "))*float(input("Enter the height of the parallelogram: ")))

Rhombus = 4*float(input("Enter the side of the rhombus: "))
print("The perimeter of the rhombus is:", Rhombus)
print("The area of the rhombus is:", 0.5*float(input("Enter the first diagonal of the rhombus: "))*float(input("Enter the second diagonal of the rhombus: ")))

Trapezium = float(input("Enter the first side of the trapezium: "))+float(input("Enter the second side of the trapezium: "))+float(input("Enter the third side of the trapezium: "))+float(input("Enter the fourth side of the trapezium: "))
print("The perimeter of the trapezium is:", Trapezium)
print("The area of the trapezium is:", 0.5*(float(input("Enter the sum of the parallel sides of the trapezium: "))*float(input("Enter the height of the trapezium: "))))

# Surface Area and Volume of 3D Shapes
Sphere = 2*3.14*float(input("Enter the radius of the sphere: "))
print("The surface area of the sphere is:", Sphere)
print("The volume of the sphere is:", 4/3*3.14*float(input("Enter the radius of the sphere: "))**3)

Cylinder = 2*3.14*float(input("Enter the radius of the cylinder: "))+2*3.14*float(input("Enter the height of the cylinder: "))
print("The surface area of the cylinder is:", Cylinder)
print("The volume of the cylinder is:", 3.14*float(input("Enter the radius of the cylinder: "))**2*float(input("Enter the height of the cylinder: ")))

Cone = 3.14*float(input("Enter the radius of the cone: "))+3.14*float(input("Enter the slant height of the cone: "))
print("The surface area of the cone is:", Cone)
print("The volume of the cone is:", 1/3*3.14*float(input("Enter the radius of the cone: "))**2*float(input("Enter the height of the cone: ")))

Cube = 6*float(input("Enter the side of the cube: "))
print("The surface area of the cube is:", Cube)
print("The volume of the cube is:", float(input("Enter the side of the cube: "))**3)

Cuboid = 2*(float(input("Enter the length of the cuboid: "))+float(input("Enter the breadth of the cuboid: ")))+2*(float(input("Enter the breadth of the cuboid: "))+float(input("Enter the height of the cuboid: ")))+2*(float(input("Enter the height of the cuboid: "))+float(input("Enter the length of the cuboid: ")))
print("The surface area of the cuboid is:", Cuboid)
print("The volume of the cuboid is:", float(input("Enter the length of the cuboid: "))*float(input("Enter the breadth of the cuboid: "))*float(input("Enter the height of the cuboid: ")))

Prism = 2*(float(input("Enter the base of the prism: "))+float(input("Enter the height of the prism: ")))+3*(float(input("Enter the base of the prism: ")))
print("The surface area of the prism is:", Prism)
print("The volume of the prism is:", float(input("Enter the base of the prism: "))*float(input("Enter the height of the prism: ")))