
# Functions accepts nothing and return nothing
def fun():
    print("Functin fun")

# 2: Function which accepts parameter and accepts nothing
def gun(no):
    print("Function gun with parameter : ",no)

# 3: Function which accepts parameter and return the value
def sun(no):
    print("Function sun with parameter : ",no)
    return no+1

# 4: Functions accepts multiple values and return multiple values
def AddSub(no1,no2):
    add=no1+no2
    sub=no1-no2
    return add,sub

def main():
    fun()
    gun(11)
    ret=sun(10)
    print("Return value of sun",ret)

    ret1,ret2=AddSub(12,10)
    print("Addition : ",ret1)
    print("Substraction : ",ret2)

if __name__=="__main__":
    main()