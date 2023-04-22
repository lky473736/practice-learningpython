import math

print ("각도, sin값, cos값")

for i in range (0, 100, 10) : 
    angle = i
    math.degrees(angle)
    
    sinval = math.sin(angle)
    cosval = math.cos(angle)
    
    print (angle, " ", sinval, " ", cosval)