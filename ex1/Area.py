import math
'''
This function takes 5 numbers and returns the area of the shape discribed (4 first numbers are the sides and 5th is the diametere)
If the 4th number is zero the 3 prior numbers count as a triangle
'''
def Area(A,B,C,D,E):
    if (D == 0):
        P = (A + B + C) / 2
        AreaAmount = math.sqrt(P * (P - A) * (P - B) * (P - C))
    else:
        P1 = (A + B + E) / 2
        P2 = (E + D + C) / 2
        AreaAmount = math.sqrt(P1 * (P1 - A) * (P1 - B) * (P1 - E)) + math.sqrt(P2 * (P2 - C) * (P2 - D) * (P2 - E))
    return AreaAmount
