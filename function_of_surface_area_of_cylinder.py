def area(surface_area):
    """
    This is called doc string.    print(functionsurface area of cylinder
    """
    pi=3.14
    r= int(input('radius of cylinder'))
    h= int(input('height of cylinder'))

    c= (pi**2 * r)
    c1=2*pi*r
    d=h * c1
    surface_area = c + d

area()
help(area)
# print(c)
print(surface_area)
