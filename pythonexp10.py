def main():
    #To write the contents into the file
    str_data=input("Enter the file contents: ")
    try:
        fptr=open("myfile01.txt","w")
        fptr.write(str_data)
    except IOError as e:
        print("Exception raised is",e)
    else:
        print("\n Successfully, contents written into the file.")
    fptr.close()
    #To read the contents from the file and display
    try:
        fptr=open("myfile01.txt","r")
        print("\nThe file contents: ")
        print(fptr.read())
    except EOFError as e:
        print("Exception raised is",e)
    fptr.close()
    fptr=open("myfile01.txt","r")
    file_data=fptr.read()
    from collections import Counter
    #split the str_data
    split_data=file_data.split()
    Counter=Counter(split_data)
    most_occur=Counter.most_common(3)
    print(most_occur)
    fptr.close()
main()
