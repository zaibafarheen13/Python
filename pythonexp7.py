#TO IMPLEMENT INHERITANCE
def main():
    class Polygon:
        def __init__(self,no_of_sides):
            self.n=no_of_sides
            self.sides=[0 for i in range(no_of_sides)]
        def inputsides(self):
            for i in range(self.n):
                print("Enter the side-",i+1)
                self.sides[i]=int(input())
        def dispsides(self):
            for i in range(self.n):
                print("Side",i+1,"is",self.sides[i])
    class Triangle(Polygon):
        def __init__(self):
            Polygon.__init__(self,3)
        def triarea(self):
            a,b,c=self.sides
            #CALCULATE THE SEMI-PERIMETER
            s=(a+b+c)/2
            area=(s*(s-a)*(s-b)*(s-c))**0.5
            print('The area of the triangle is %0.2f'%area)
            #CREATING OBJECT OF THE DERIVED CLASS
    t=Triangle()
    t.inputsides()
    t.dispsides()
    t.triarea()
main()
