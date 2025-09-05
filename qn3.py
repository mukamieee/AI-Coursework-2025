side_length = input("Input length of a side of a square: ")

# function to calculate area
def area(side_length):
    return float(side_length) * float(side_length)

# function to calculate perimeter
def perimeter(side_length):
    return 4 * float(side_length)

# display results
print("Area of the square:", area(side_length))
print("Perimeter of the square:", perimeter(side_length))