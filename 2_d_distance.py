#request coords of both points
point_1_x = int(input ("what is x value of point 1?: "))
point_1_y = int(input ("what is the y value of point 1?: "))
point_2_x = int(input ("what is the x value of point 2?: "))
point_2_y = int(input ("what is the y value of point 2?: "))
# x sub two minus x sub one
delta_x = point_2_x - point_1_x
# y sub two minus y sub one
delta_y = point_2_y - point_1_y
# square delta x
x_final = delta_x**2
# square delta y
y_final = delta_y**2
# line 11 plus line 13
radicand = int(x_final + y_final)
#import sqrt
from math import sqrt
# take square root of line 15
sqrt(radicand)
# return line 17
print( sqrt(radicand) , "is the answer")
