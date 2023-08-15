def main():
    dlist=[]
    n=int(input("ENTER THE LIST SIZE:"))
    #FUNCTION TO ACCEPT LIST ELEMENTS
    def input_list():
        print("\n")
        for i in range(0,n):
            print("ENTER THE NUMBER AT THE LOCATION",i,":")
            item=int(input())
            dlist.append(item)
            #DISPLAY THE ELEMENTS IN THE list
        print("\n")
        print("USER LIST IS",dlist)
        print("\n")
    #SEARCH FUNCTION
    def sequential_search(dlist,item):
        pos=0
        found=False
        while pos<len(dlist) and not found:
            if dlist[pos]==item:
                found=True
            else:
                pos=pos+1
        if found==True:
            print("ITEM",item,"IS FOUND AT THE POSITION",pos+1)
        else:
            print("ITEM",item,"WAS NOT FOUND IN THE LIST")
    #TYPE CAST THE INPUT ITEM TO INT
    input_list()
    item=int(input("ENTER THE ELEMENT TO BE SEARCHED : "))
    print("\n")
    sequential_search(dlist,item)
main()
