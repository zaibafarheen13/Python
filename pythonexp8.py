#Program- To immplement Exception Handling
def main():
    try:
        #division by zero
        a=int(input("Enter first integer value:"))
        b=int(input("Enter the second integer value:"))
        #list1=[10,20,30]
        list1=[10,20,30,40,50,60]
        x=8
        #This statement will raise an exception if second integer value is 0
        c=a/b
        print("The result of division is %d"%c)
        print('\n')
        print("Second element  of list1 is %d"%list1[1])
        #This statement will raise an Exception
        print("Fifth element of list1 is %d"%list1[5])
        #This statement will raise an Exception
        print('\n')
        print("The value of x is %d"%x)
        #This statement will raise an Exception
        print('\n')
        print('10'+a)
    except ZeroDivisionError as e:
        print(e)
    except IndexError as e:
        print(e)
    except TypeError as e:
        print(e)
    except NameError as e:
        print(e)
    finally:
        print("Outside the exception block")
main()
