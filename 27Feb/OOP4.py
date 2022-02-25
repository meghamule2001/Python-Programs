# thinking in c++ - krus ekel
# design and evolution c++

# kay karaych ahe? ->Addition
# Te karnyasathi kay kay pahije? ->Two numbers

# START 37 38 22 24 10 12 13 27 15 16 17 28 29 19 20
class Arithmatic:                       # Class definition
    value=111                           # Class variable
    def __init__(self,i,j):             # Class constructor       # Instance Method
        print("Inside Constructor")
        self.no1=i                      # Class Instance variable
        self.no2=j                      # Instance variable

    def Add(self):                      # Instance method
        print(Arithmatic.value)
        return self.no1+self.no2

    def Sub(self):                      # Instance method
        return self.no1-self.no2

def main():
    print("Value is : ",Arithmatic.value)
    obj1=Arithmatic(21,11)              # __init__(obj1,21,11)      # Arithmatic(obj) -> __init__(obj)
    obj2=Arithmatic(101,51)             # __init__(obj2,101,51)
    print("value is : ",obj1.value)
    ret=obj1.Add()                     # ret=Add(obj1)
    print("Addition is : ",ret)
    ret=obj1.Sub()                      # ret=Sub(obj1)
    print("Subtraction is : ",ret)

    ret=obj2.Add()                     # ret=Add(obj2)
    print("Addition is : ",ret)
    ret=obj2.Sub()                      # ret=Sub(obj2)
    print("Subtraction is : ",ret)

if __name__=="__main__":
    main()