""""
Write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the following 12 steel can sizes. Then visually examine the output and answer this question, "Which can size has the highest storage efficiency?"

name	       radius   Height    Cost per Can
 centimeter  (centimeters)   (U.S. dollars)
#1 Picnic	    6.83	10.16	$0.28
#1 Tall	        7.78	11.91	$0.43
#2	            8.73	11.59	$0.45
#2.5	        10.32	11.91	$0.61
#3 Cylinder	    10.79	17.78	$0.86
#5	            13.02	14.29	$0.83
#6Z	            5.40	8.89	$0.22
#8Z short	    6.83	7.62	$0.26
#10	            15.72	17.78	$1.53
#211	        6.83	12.38	$0.34
#300	        7.62	11.27	$0.38
#303	        8.10	11.11	$0.42

Your program must compute the volume of all 12 can sizes.
Your program must compute the surface area of all 12 can sizes.
Your program must compute and print the storage efficiency of all 12 can sizes.
"""

import math

def main():

    can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.40, 8.89, 0.22],
        ["#8Z Short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.38],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.10, 11.11, 0.42]
    ]
    
    storage_eff_max = 0
    storage_eff_can = ""
    cost_eff_max = 0
    cost_eff_can = ""
    

    for i in can_sizes:
        can = i[0]
        radius = i[1]
        height = i[2]
        cost_per_can = i[3]
        
        storage_eff = compute_storage_efficiency(radius, height)
        cost_effciency = compute_cost_efficiency(radius, height, cost_per_can)
        print(f"{can} {storage_eff:.1f} {cost_effciency:.0f}")

        
        if storage_eff_max < storage_eff:
            storage_eff_can = can
            storage_eff_max = storage_eff

        if cost_eff_max < cost_effciency:
            cost_eff_can = can
            cost_eff_max = cost_effciency
            
    print(f"The most efficient with storage is {storage_eff_can} at {storage_eff_max:.1f}")
    print(f"The most efficient with cost is {cost_eff_can} at {cost_eff_max:.0f}.")
    pass

def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    #surface_area = 2 * math.pi * (radius + height)
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    return surface_area 

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    return volume / surface_area

def compute_cost_efficiency(radius, height, cost_per_can):
    return compute_volume(radius, height) / cost_per_can

main()
