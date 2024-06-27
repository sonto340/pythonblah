coordinates = (1, 2, 3)
# coordinates[0] * coordinates[2] *coordinates[3]
#   this is bad code. repetitive for multiple draws
#   instead define the coordinates first and simply call the labels instead
#       x = coordinates[0] 
#       y = coordinates[1]
#       z = coordinates[2]
#       area = (x * y * z)
#       print(area)
# this is also inefficient and wastes lines defining them
# python can unpack tuples and lists
# line 13 and lines 5-7 are identical functionality wise
x, y, z = coordinates
area = (x * y * z)
print(area)
