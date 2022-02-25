

# Positional arguments
def Student(name,rno,address,marks):
    print("Name is : ",name)
    print("Roll number is : ",rno)
    print("Address is : ",address)
    print("Marks is : ",marks)

# Kerword arguments
def Computer(RAM,Processor,HDD):
    print("RAM size is : ",RAM)
    print("Processor name is : ",Processor)
    print("Size of HDD is : ",HDD)

# Default argument(Should be from right to left order)
def CircleArea(Radious,PI=3.14):
    print("Value of PI is : ",PI)
    return PI*Radious*Radious

# Variable number of arguments
def Fun(*Value): # Here * is not a pointer it's syntactical part of pyhton
                # * shows we are taking multiple numbers of inputs
    print(type(Value))
    print("Number of arguments are : ",len(Value))

def main():
    Student("Megha",43,"Latur",99)
    Computer(Processor="i7",RAM=8,HDD="1TB")
    Computer(RAM=16,HDD="512GB",Processor="i5")

    CircleArea(10.5)
    CircleArea(10.5,7.12)

    Fun(10,20,30)
    Fun(11,51,34,43,12)
    Fun()

if __name__=="__main__":
    main()