# Import the math module so I can use math.pi and math.sqrt.
import math
from datetime import datetime, timedelta

current_date = datetime.now().date()

warranty_duration = timedelta(weeks=1)
waranty_date = current_date + warranty_duration

new = input('Are these new tires? (yes or no): ')
new = new.lower()

# Get the width, aspect ratio, and diameter of the tire
width = abs(float(input('Enter the width of the tire in mm (ex 205): ')))
ratio = abs(float(input('Enter the aspect ratio of the tire (ex 60): ')))
diameter = abs(float(input('Enter the diameter of the wheel in inches (ex 15): ')))

# Compute the volume of the tire
bracket = width * ratio + 2540 * diameter
volume = math.pi * width**2 * ratio * bracket / 10000000000

#Round the volume to two digits after the decimal point
volume = round(volume, 2)

# Print the volume for the user to see
print(f'The approximate volume is {volume} liters')

# open volumes.txt
# add line to it with the following data:
    # current date
    # width of the tire
    # aspect ratio of the tire
    # diameter of the wheel
    # volume of the tire

with open('volumes.txt', 'at') as volumes_file:
    if new == 'yes':
        response = f'These tires are under waranty until {waranty_date}'
    
    else:
    
        response = 'These tires are not under waranty'
    
    print(f'{current_date}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.02f}', file=volumes_file)
    print(f'{response}', file=volumes_file)

