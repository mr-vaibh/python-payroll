from math import pi

def arclength(diameter, angle):
	if angle >= 360: return None
	
	arc_length = (pi*diameter) * (angle/360)
	return arc_length


diameter = float(input('Diameter of circle: '))
angle = float(input('Angle measure(in degrees): '))

arc_length = arclength(diameter, angle)

if (not None): print(f"Arc length is {arc_length} units\n..or {round(arc_length, 2)} in round figures")
else: print("Angle is not possible.")