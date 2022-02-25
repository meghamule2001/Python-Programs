
class Demo:
    x=10        # Class variable
    y=20        # Class variable
    def __init__(self):     # used to create instance variable
                            # used to allocate the resourses (socket connection, database connection)
        print("Inside Constructor")
        self.i=30   # Instance variable
        self.j=40   # Instance variable

    def __del__(self):      # used to remove memory allocated on heap to the objects
        print("Inside Distructor")

    def fun(self):
        print("Inside fun")


def main():
    obj1=Demo()
    obj2=Demo()

    obj1.fun()  # fun(obj1)
    obj2.fun()  # fun(obj2

    del obj1
    del obj2    # we cannot access obj1 and obj2 after using del keyword

    obj1.fun()      # UnboundLocalError : local variable 'obj1' referenced before assignment

if __name__=="__main__":
    main()
