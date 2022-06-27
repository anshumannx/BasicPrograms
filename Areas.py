def area_cube (a):
    return a*a*a
def area_cuboid (a,b,c) :
    return a*b*c
def area_circle (a,pi=3.14) :
    return pi*a*a
def area_sphere(a,pi=3.14):
    return 3*pi*a*a
def area_cylinder(a,b,pi=3.14) :
    return (2*pi*a)*(a+b)

side = int(input("Enter side for cube :\t"))
ac = area_cube(side)
print("The area for cube is :\t", ac)

length = int(input("Enter length for cuboid :\t"))
breadth = int(input("Enter breadth for cuboid :\t"))
height = int(input("Enter height for cuboid :\t"))
acu = area_cuboid(length,breadth,height)
print("The area for cuboid is :\t",acu)

radius = int(input("Enter radius for circle :\t"))
aci = area_circle(radius)
print("The area for circle is :\t",aci)

radiuss = int(input("Enter radius for sphere :\t"))
asp = area_sphere(radiuss)
print("The area for sphere is :\t",asp)

radiusc = int(input("Enter radius for cylinder :\t"))
heightc = int(input("Enter height for cylinder :\t"))
acy = area_cylinder(radiusc,heightc)
print("The area for cylinder is :\t",acy)