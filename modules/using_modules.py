import my_module as areas
# OR from my_module import circle, rectangle
# OR from my_module import *

""" 
if we use from my_module import *, whole of my_module will run 
To prevent this we use __name__ in the module file (check module file)
"""

radius = 7
area_circle = areas.circle(radius)

l = 10
b = 6

area_rect = areas.rectangle(l, b)
print(area_rect)