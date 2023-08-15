def main():
    #To write the contents into the file
    str_data=input("Enter the file contents: ")
    try:
        fptr=open("myfile01.txt","w")
        fptr.write(str_data)
    except IOError as e:
        print("Exception raised is",e)
    else:
        print("\n Successfully, contents witten into the file.")
    fptr.close()
    #To read the contents from the file and display
    try:
        fptr=open("myfile01.txt","r")
        print("\n The file contents: ")
        print(fptr.read())
    except EOFError as e:
        print("Exception raised is",e)
    fptr.close()
    #To append the contents into the file
    try:
        fptr=open("myfile01.txt","a")
        str_data=input("Enter the contents to be appended: ")
        fptr.write(str_data)
    except IOError as e:
        print("Exception raised is",e)
    else:
        print("Successfully, contents appended.")
    fptr.close()
    #To display contents after appending
    try:
        fptr=open("myfile01.txt","r")
        print("\n The file contents after appending: ")
        print(fptr.read())
    except EOFError as e:
        print("Exception raised is",e)
    fptr.close()
main()
