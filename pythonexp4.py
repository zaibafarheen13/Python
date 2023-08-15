import sys
def main():
    try:
        choice=int(sys.argv[1])
        x=int(sys.argv[2])
        y=int(sys.argv[3])
        if choice==1:
            result=x+y
            print("Additional result is:",result)
        elif choice==2:
            result=x-y
            print("The subtraction result is:",result)
        elif choice==3:
            result=x*y
            print("The multiplication result is:",result)
        elif choice==4:
            result=x/y
            print("The division result is:",result)
        else:
            print("Invalid choice try again")
    except Exception as e:
        print("Exception raised is:",e)
main()
