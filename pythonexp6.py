def main():
    my_string1='WELCOME TO PYTHON PROGRAM'
    my_string2="""String holds a sequence of
                              unicode characters"""
    my_string3="COMPUTER SCIENCE STUDENTS"
    print("My first string is #######################")
    print(my_string1)
    print('\n')
    print("My second string is #######################")
    print(my_string2)
    print('\n')
#STRING FUNCTIONS
    print("SLICING OF STRING #######################")
    print(my_string1[0:6])
    print('\n')
    print("USE OF NEGATIVE INDEX #######################")
    print(my_string1[-7:])
    print('\n')
    print("LENGTH OF THE STRING-1 #######################")
    print(len(my_string1))
    print('\n')
    print("JOIN STRING-1 AND STRING-2")
    print(my_string1+" "+my_string2)
    print('\n')
    print("FIND THE OCCURENCE OF A CHARACTER #######################")
    print(my_string1.count("O"))
    print('\n')
    print("TO FIND THE INDEX POSITION OF CHARACTER #######################")
    print(my_string1.find('P'))
    print('\n')
    print("LOWER CASE OF STRING-1:",my_string1.lower())
    print('\n')
    print("USING FORMAT METHOD")
    pos_order="{0},{1} and {2} ARE BEST FRIENDS".format('SITA','GITA','RITA')
    print(pos_order)
    print('\n')
    print("SPLIT FUNCTION:")
    s="WE ARE JYOTINIVITES".split()
    print(s)
main()
