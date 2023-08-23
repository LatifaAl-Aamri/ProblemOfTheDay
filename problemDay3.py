"""
write a function in python that take variables hight h and radius r
and calculate the volume of a cone.
"""
import math
#formula for volume of a cone
#coneVolume = (1/3) · π · r2 · h
def cone_volume(h, r):
    if h <= 0 or r <= 0:
        raise ValueError("Height and radius must be positive values.")
    
    volume = (1/3) * math.pi * r**2 * h
    return volume

# Example usage
#height = 7.0  # Replace with the actual height of the cone
#radius = 4.0 # Replace with the actual radius of the cone
height = float(input("write the height of the cone: "))
radius = float(input("write the radius of the cone: "))
cone_vol = cone_volume(height, radius)
print(f"The volume of the cone is: {cone_vol:.2f} cubic units") #:.2f this mean round in 2 decimal num