import numpy as np
from math import *

"""
Calculates the sum of an infinite variety 
"""
def sum_infinite_variety(first_number, quotient):                     
    if -1 < quotient < 1:
        print(first_number / (1 - quotient))
    else:
        print("You can not sum an infinite variaty where the quotient is greater than 1 or less than -1!")

"""
Finds the first c numbers in a fibonacci sequence with the first to numbers being a and b
"""
def fibonacci(a, b, c):
    numbers = [a, b]
    for i in range(2, c):
        numbers.append(numbers[i - 1] + numbers[i - 2])       
    print(numbers)

"""
Makes a list of the first n numbers in the tribonacci sequence 
"""
def tribonacci(n):
    numbers = [1, 1, 2]
    for i in range(3, n + 1):
        numbers.append(numbers[i - 1] + numbers[i - 2] + numbers[i - 3])
    print(numbers[n])

"""
Checks if the given number is in the tribonacci sequence
"""
def tribonacci_check(number):
    tribonacci_number = 0
    numbers = [1, 1, 2]
    i = 3
    while tribonacci_number < number:
        numbers.append(numbers[i - 1] + numbers[i - 2] + numbers[i - 3])
        tribonacci_number = numbers[i]
        i += 1
    for i in range(len(numbers)):
        if number == numbers[i]:
            print(i + 1)
        elif number not in numbers:
            print("\nYour number is not in the tribonacci sequence.")
            break

"""
Calculates factorial of any whole number
"""
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

"""
Uses gaussian elimination to see if the matrix given has one solution 
"""
def gaussian_elimination(m, eps = 1.0/(10**10)):
  (h, w) = (len(m), len(m[0]))
  for y in range(0,h):
    maxrow = y
    for y2 in range(y+1, h):    # Find max pivot
      if abs(m[y2][y]) > abs(m[maxrow][y]):
        maxrow = y2
    (m[y], m[maxrow]) = (m[maxrow], m[y])
    if abs(m[y][y]) <= eps:     # Singular?
      return False
    for y2 in range(y+1, h):    # Eliminate column y
      c = m[y2][y] / m[y][y]
      for x in range(y, w):
        m[y2][x] -= m[y][x] * c
  for y in range(h-1, 0-1, -1): # Backsubstitute
    c  = m[y][y]
    for y2 in range(0,y):
      for x in range(w-1, y-1, -1):
        m[y2][x] -=  m[y][x] * m[y2][y] / c
    m[y][y] /= c
    for x in range(h, w):       # Normalize row y
      m[y][x] /= c
  return True

"""
Calculate determinant of given matrix
"""
def calculate_determinant(A):
    return np.linalg.det(A)

"""
Calculate determinant, but better. (no decimals, more efficient). Only for square matrices for now.
"""
def determinant(matrix):
    
    # Check if matrix is just 1x1. The exit clause for the recursion
    if len(matrix) == 1 and len(matrix[0]) == 1: return matrix[0][0]
    
    result = 0    
    r = 0    
    for c in range(len(matrix[r])):        
        # The previous value
        p = matrix[r][c]
        
        # Rest value is telling what matrix remains after the row and column of the inspecting value are gone
        # Copy the matrix. Way too long because Python likes passing pointers instead of copying values 
        rest = []
        for v in matrix:
            x = []
            for w in v: x.append(w)
            rest.append(x)
        
        del rest[r] # Delete the current row
        
        # Delete the current column
        for i in range(len(rest)):
            del rest[i][c] # Delete the at the same column in row i 
            
        sign = (1 if (c % 2 == r % 2) else -1)
        result += sign * p * determinant(rest)
        
    return result
    


"""
Use Cramer's rule to find the value of the variables from given matrix
"""
def Cramers_rule(A):
    B = [[],[],[]]
    for index in range(len(A)):
        for number in A[index]:
            B[index].append(number)
            
    determinant = calculate_determinant([[B[0][0], B[0][1], B[0][2]],
                                       [B[1][0], B[1][1], B[1][2]],
                                       [B[2][0], B[2][1], B[2][2]]])
    
    x = calculate_determinant([[A[0][3], A[0][1], A[0][2]],
                             [A[1][3], A[1][1], A[1][2]],
                             [A[2][3], A[2][1], A[2][2]]])/determinant
    
    y = calculate_determinant([[A[0][0], A[0][3], A[0][2]],
                             [A[1][0], A[1][3], A[1][2]],
                             [A[2][0], A[2][3], A[2][2]]])/determinant
    if len(A) == 3:
        z = calculate_determinant([[A[0][0], A[0][1], A[0][3]],
                                 [A[1][0], A[1][1], A[1][3]],
                                 [A[2][0], A[2][1], A[2][3]]])/determinant
        return x, y, z
    return x, y

"""
Calculate radians from degrees
"""
def radians(degrees):
    return degrees * (math.pi / 180)

"""
Calculate degrees from radians
"""
def degrees(radians):
    return degrees / (math.pi / 180)

"""
Find arclength with known angle in radians and radius
"""
def arclength(angle_in_rad, radius):
    return angle_in_rad * radius

"""
Find radius with known arclength and angle in radians
"""
def radius(arclength, angle_in_rad):
    return arclength / angle_in_rad
"""
Find the angle in radians with known arclength and radius 
"""
def angle_in_rad(arclength, radius):
    return arclength / radius

"""
Find which quadrant an angle is in
"""
def quadrant(degrees):
    while not (0 <= degrees <= 360):
        if degrees < 0:
            degrees += 360
        else:
            degrees -= 360

    if degrees > 270:
        return "fourth quadrant, sine has sign -, cosine has sign + and tangent has sign -"
    elif degrees > 180:
        return "third quadrant, sine has sign -, cosine has sign - and tangent has sign +"
    elif degrees > 90:
        return "second quadrant, sine has sign +, cosine has sign - and tangent has sign -"
    else:
        return "first quadrant, sine has sign +, cosine has sign + and tangent has sign +"

def print_sin_cos_tan():
    degrees = 0
    for i in range(13):      
        sine = round(np.sin(math.pi * (degrees / 180)),3)
        cosine = round(np.cos(math.pi * (degrees / 180)),3)
        if not cosine == 0:
            tangent = sine / cosine
        else:
            tangent = "infinite"

        print(f"{degrees} degrees has sine = {sine}, cosine = {cosine} og tangent = {tangent}")
        degrees += 30

"""
From n numeral system to decimal numeral system
"""
def fromnto10(number_string, n):
    ten_number = 0
    number_string = number_string[::-1]
    for i in range(len(number_string)):
        if int(number_string[i]) != 0:
            ten_number += int(number_string[i]) * n ** i
    return ten_number

"""
From decimal numeral system to n numeral system
"""
def from10ton(ten_number_int, n):
    if ten_number_int < n:
        return str(ten_number_int)
    remainder = ten_number_int % n
    return str(remainder) + from10ton(int((ten_number_int - remainder) / n), n)

"""
From x numeral system to y numeral system
"""
def fromxtoy(number_string, x, y):
    ten_number = fromnto10(number_string, x)
    print(from10ton(ten_number, y)[::-1])

"""
Check if the lengths a, b and c can make a triangle
"""
def isTriangle(a,b,c):
    return a < b + c and b < a + c and c < b + a

"""
Find semiperimeter of a triangle
"""
def semiperimeter(a,b,c):
        return (a + b + c) / 2

"""
Calculates area of a triangle with three known sides
"""
def herons_formula(a,b,c):   
    if isTriangle(a,b,c):
        s = semiperimeter(a, b, c)
        return math.sqrt(s * (s-a) * (s-b) * (s-c))
    else:
        return "Not a triangle"
    
"""
Calculates area of triangle with one given angle and the two sides next to it
"""
def side_angle_side(a, b, C):
    return round(1 / 2 * a * b * sin(C), 2)

"""
Function to calculate where y = 0 for a sine function
"""
def solve_sin_second_degree(a,b,c):
    def find_angles(operator):
        x = eval(f"(-{b} {operator} {square_root}) / (2*{a})")
        if -1 <= x <= 1:
            x = asin(x)
            result.append(x)  
            result.append(pi - x)
            
    if b ** 2 - 4 * a * c < 0:
        return []
    
    result = []
    square_root = sqrt(b**2-4*a*c)

    find_angles("+")      
    find_angles("-")
    
    correct_result = []
    for item in result:
        correct_result.append(round((item + 2*pi) % (2 * pi),2)) 
    correct_result = list(set(correct_result))
    
    return correct_result

def sphereSurfaceDistance(lat1, long1, lat2, long2, r):
    # Convert the equator prime meridian based degrees
    # to north pole prime meridian based radians
    
    u1 = (90 - lat1) * pi/180
    v1 = long1 * pi/180

    u2 = (90 - lat2) * pi/180
    v2 = long2 * pi/180

    pos1 = (r*sin(u1)*cos(v1), r*sin(u1)*sin(v1), r*cos(u1))
    pos2 = (r*sin(u2)*cos(v2), r*sin(u2)*sin(v2), r*cos(u2))

    angle = acos((pos1[0]*pos2[0]+pos1[1]*pos2[1]+pos1[2]*pos2[2])/(r*r))
    
    return angle * r

def  leftStairSum(function, a, b, n):
    dX = (b-a)/n
    return sum([function(a + i*dX) * dX for i in range(n)])
    
def rightStairSum(function, a, b, n):
    dX = (b-a)/n
    return sum([function(a + i*dX) * dX for i in range(1,n+1)])

def trapezoidSum(function, a, b, n):
    dX = (b-a)/n
    return sum([dX * (function(a + i * dX) + function(a + (i + 1) * dX))/2 for i in range(n)])

def simpsonsWay(function, a, b, n):
    dX = (b-a)/n
    print(function(a))
    print(function(b))
    print([function(a + i*dX) * 4 for i in range(1,n, 2)])
    print([function(a + i*dX) * 2 for i in range(2,n-1, 2)])
    return (dX/3)*sum([function(a), function(b)] + [function(a + i*dX) * 4 for i in range(1,n, 2)] + [function(a + i*dX) * 2 for i in range(2,n-1, 2)])
