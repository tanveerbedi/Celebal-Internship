# Lower Triangular Pattern
def lower_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()

lower_triangle(5)


# Upper Triangular Pattern
def upper_triangle(rows):
    for i in range(rows):
        for j in range(i):
            print(" ", end="  ") 
        for k in range(rows - i):
            print("*", end=" ")
        print()

upper_triangle(5)


# Pyramid Triangular Pattern
def pyramid(rows):
    for i in range(rows):
        for j in range(rows - i - 1):
            print(" ", end=" ") 
        for k in range(i + 1):
            print("*", end=" ")
        print()

pyramid(5)


# Animated Triangular Pattern
import time
def animated_pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1), end="")
        for j in range(i + 1):
            print("*", end=" ")
            time.sleep(0.05)
        print()

animated_pyramid(5)


# User Input
def main():
    rows = int(input("Enter number of rows: "))
    print("Lower Triangle:")
    lower_triangle(rows)
    
    print("\nUpper Triangle:")
    upper_triangle(rows)
    
    print("\nPyramid:")
    pyramid(rows)

main()
