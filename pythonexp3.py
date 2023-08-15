def main():
    my_dict={'name':'Jack','age':26,'address':'Bangalore','DOB':'16.9.1994'}
    print("My dictionary contents are:#####")
    print(my_dict)
    my_dict['age']=30
    print("\n My dictioanry contents after updating:#####")
    print(my_dict)
    cubes={1:1,2:8,3:27,4:64,5:125}
    print("\n Cubes are:#####")
    print(cubes)
    print("\nSorted cubes:#####")
    print(sorted(cubes))
    print("\nThe item removed is %d" %cubes.pop(4))
    print(cubes.keys())
    cubes[4]=64
    print(cubes)
    print("\n No of elements in the cubes %d" %len(cubes))
    print("\n No of elements in my_dict....using for loop")
    for i in my_dict.items():
        print(i)
    new_dict=my_dict.copy()
    print("\n New dict after copying")
    print(new_dict)
    new_dict.clear()
    print("\n Contents after clearing:#####")
    print(new_dict)
main()
