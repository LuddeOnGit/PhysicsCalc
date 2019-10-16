import numpy as np
import math

def sum_uendelig_rekke():
    første_ledd = float(eval(input("Hva er det første leddet i rekken din? ")))
    kvotient = float(eval(input("Hva er kvotienten til rekken din? ")))                      
    if kvotient < 1 and kvotient > -1:
        print(første_ledd / (1 - kvotient))
    else:
        print("Du kan ikke summere en uendelig rekke der kvotienten er >= 1 eller <= -1")

def fibonacci(a, b, c):
    numbers = [a, b]
    for i in range(2, c):
        numbers.append(numbers[i - 1] + numbers[i - 2])       
    print(numbers)

def tribonacci(n):
    numbers = [1, 1, 2]
    for i in range(3, n + 1):
        numbers.append(numbers[i - 1] + numbers[i - 2] + numbers[i - 3])
    print(numbers[n])

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
    
def fakultet(n):
    if n == 0: return 1
    return n * fakultet(n-1)

def gauss_jordan(m, eps = 1.0/(10**10)):
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

def regn_ut_determinant(A):
    np.linalg.det(A)

def Cramers_regel(A):
    B = [[],[],[]]
    for index in range(len(A)):
        for number in A[index]:
            B[index].append(number)

            
    determinant = regn_ut_determinant([[B[0][0], B[0][1], B[0][2]],
                                       [B[1][0], B[1][1], B[1][2]],
                                       [B[2][0], B[2][1], B[2][2]]])
    
    x = regn_ut_determinant([[A[0][3], A[0][1], A[0][2]],
                             [A[1][3], A[1][1], A[1][2]],
                             [A[2][3], A[2][1], A[2][2]]])/determinant
    
    y = regn_ut_determinant([[A[0][0], A[0][3], A[0][2]],
                             [A[1][0], A[1][3], A[1][2]],
                             [A[2][0], A[2][3], A[2][2]]])/determinant
    if len(A) == 3:
        z = regn_ut_determinant([[A[0][0], A[0][1], A[0][3]],
                                 [A[1][0], A[1][1], A[1][3]],
                                 [A[2][0], A[2][1], A[2][3]]])/determinant
        return x, y, z
    return x, y

def rad(grader):
    return grader * (math.pi / 180)

def grader(rad):
    return rad / (math.pi / 180)

def buelengde(radvinkel, radius):
    return radvinkel * radius

def radius(buelengde, radvinkel):
    return buelengde / radvinkel

def radvinkel(buelengde, radius):
    return buelengde / radius

def kvadrant(grader):
    while not (grader >= 0 and grader <= 360):
        if grader < 0:
            grader += 360
        else:
            grader -= 360

    if grader > 270:
        return "fjerde kvadrant, sinus har fortegn -, cos har + og tan har -"
    elif grader > 180:
        return "tredje kvadrant, sinus har fortegn -, cos har - og tan har +"
    elif grader > 90:
        return "andre kvadrant, sinus har fortegn +, cos har - og tan har -"
    else:
        return "første kvadrant, sinus har fortegn +, cos har + og tan har +"

def sin_cos_tan():
    grader = 0
    for i in range(13):      
        sinus = round(np.sin(math.pi * (grader / 180)),3)
        
        cosinus = round(np.cos(math.pi * (grader / 180)),3)
        if not cosinus == 0:
            tangens = sinus / cosinus
        else:
            tangens = "uendelig"

        print(f"{grader} grader har sin = {sinus}, cos = {cosinus} og tan = {tangens}")
        grader += 30

#fra n-tallsystemet til 10-tallsystemet
def frantil10(TallStreng, n):
    titall = 0
    TallStreng = TallStreng[::-1]
    for i in range(len(TallStreng)):
        if int(TallStreng[i]) != 0:
            titall += int(TallStreng[i]) * n ** i
    #print(titall)
    return titall

#fra 10-tallsystemet til n-tallsystemet
def fra10tiln(tiTallSomTall, n):
    if tiTallSomTall < n:
        return str(tiTallSomTall)
    rest = tiTallSomTall % n
    return str(rest) + fra10tiln(int((tiTallSomTall - rest) / n), n)

#fra x-tallsystemet til y-tallsystemet
def fraxtily(TallStreng, x, y):
    TiTall = frantil10(TallStreng, x)
    print(fra10tiln(TiTall, y)[::-1])

def isTriangle(a,b,c):
    return a < b + c and b < a + c and c < b + a
    
def semiperimeter(a,b,c):
        return (a + b + c) / 2

def herons_formel(a,b,c):   
    if isTriangle(a,b,c):
        s = semiperimeter(a, b, c)
        return math.sqrt(s * (s-a) * (s-b) * (s-c))
    else:
        return "Not a triangle"

def arealsetning(a, b, C):

    return round(1 / 2 * a * b * math.sin(C), 2)

def areal_eller_heron():
    ja_eller_nei = input("Vet du en vinkel og de to hosliggende sidene? ")

    if ja_eller_nei == "ja":
        a = int(input("a = "))
        b = int(input("b = "))
        D = float(input("Vinkel C = "))
        C = D * math.pi / 180
        print("Trekanten med sidelengdene a = " + str(a) + ", b = " + str(b) + " og vinkelen C = " + str(D) + " har arealet " + str(arealsetning(a, b, C)))
    else:
        herons_formel()
