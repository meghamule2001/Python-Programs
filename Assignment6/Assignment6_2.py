
# Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius ,Area, Circumference.
# That class contains one class variable as PI which is initialise to 3.14.
# Inside init method initialise all instance variables to 0.0.
# There are three instance methods inside class as Accept(), CalculateArea(),
# CalculateCircumference(), Display().
# Accept method will accept value of Radius from user.
# CalculateArea() method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate circumference of circle and store it into instance
# variable Circumference.
# And Display() method will display value of all the instance variables as Radius , Area,
# Circumference.
# After designing the above class call all instance methods by creating multiple objects.

class Circle:
    PI=3.14
    def __init__(self):
        self.Rd=0.0
        self.Ar=0.0
        self.Ci=0.0

    def __del__(self):
        print("Deallocating the memory of object")
        del self.Rd
        del self.Ar
        del self.Ci

    def Accept(self):
        print("Enter Radius of Circle : ")
        self.Rd=float(input())

    def CalculateArea(self):
        self.Ar=(Circle.PI* (self.Rd * self.Rd))

    def CalculateCircumference(self):
        self.Ci=(2*Circle.PI*self.Rd)

    def Display(self):
        print("Radius of circle : ",self.Rd)
        print("Area of circle : ",self.Ar)
        print("Circumference of circle : ",self.Ci)
        print("\r")

def main():
    obj1=Circle()
    obj2=Circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

if __name__=="__main__":
    main()