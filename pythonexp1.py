def main():
  print('\n#######################\n')
  list1=['India',251,4000,'Ajmer',5478]
  list2=[3000,1000,5000,2000,4000]
  list3=["Yellow","Orange","Blue","Green","Red"]
  #1.len:This function returns the total length of the list1
  print("Length of list1:\t\t",len(list1))
  #2.max:This function returns the item from list have largest value
  #max not works for list1 it will throw TypeError
  print("max[integer]:in list2 is\t",max(list2))
  print("max[string]:in list3 is\t",max(list3)) #Check first alphabet only
  #3.min:This function returns the item from list have smallest value
  #min not works for list1 it will throw TypeError
  print("min[integer]:\t",min(list2))
  print("min[string]:\t",min(list3)) #Check first alphabet only
  #4.append:This function add new item into list at end
  list1.append('Japan')
  print("After APPEND list1 is:",list1)
  #5.insert:This function inserts item into the list at offset index
  list1.insert(3,'China')
  print("After INSERT at offset index 3 list1 is:",list1)
  #6.reverse:This function reverses items of list in place
  list1.reverse()
  print("After REVERSE list1 is",list1)
  #7.count:This function count of how many times item  exist in the list
  print("count:",list1.count('Pakistan'))
  print("count:",list1.count(4000))
  print("count:",list1.count('4000'))
  #8.index:This function returns the INDEX position of the item
  #if item not found in list it will throw ValueError
  print("index:",list1.index(4000))
  print("index:",list3.index("Yellow"))
  #9.sort:This function sorts the item in the list so they appear in ascending order(from the lowest value to the highest value)
  #if we sort list1 it will  show below Error
  #builtin.TypeError:unorderable types:int()<str()
  list3.sort()
  print("after SORT list3 is:",list3)
  list2.sort()
  print("After SORT list2 is:",list2)
  #10.extend:This function appends one list to another
  list2.extend(list3)
  print("extend:",list2)
main()
