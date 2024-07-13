import math
def circler(radius):
    area= math.pi*(radius**2)
    circumference= 2*math.pi*radius
    diameter= 2*radius
    return area , circumference , diameter

def main():
    a , c , d =circler(25)
    print(f"Area = {round(a,4)}\nCircumference = {round(c,2)}\nDiameter = {round(c,4)} ")


if __name__=='__main__':
    main()