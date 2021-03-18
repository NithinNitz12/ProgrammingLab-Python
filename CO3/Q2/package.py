
import graphics.rectangle
#selective import
from graphics.graphics3D.cuboid import area
#import using *
from graphics.circle import *


l = 20
b = 30
h = 60
r = 6


print("Area of rectangle=",graphics.rectangle.area(l,b))
print("Area of cuboid=",area(l,b,h))
print("Perimeter of circle=",cperimeter(r))
