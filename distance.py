import math
def calculate_distance(x1,y1,x2,y2):
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance    
x1=float(input("enter x-coordinate of the first point:"))
y1=float(input("enter y-coordinate of the first point:"))
x2=float(input("enter x-coordinate of the second point:"))
y2=float(input("enter y-coordinate of the second point:"))
distance=calculate_distance(x1,y1,x2,y2)
print (f"the distance between the points ({x1},{y1} and ({x2},{y2})is{distance:.2f}")
