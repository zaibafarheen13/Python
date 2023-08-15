def main():
  #tuple
  tup1 = (10,20,30,20,50)
  tup2 = ('English', 'Maths' , 'Physics' , 'Computer')
  print('tuple 1 contains:###########')
  print(tup1)
  print('tuple 2 contains:###########')
  print(tup2)
  print(tup1.count(20))
  print(tup2.index('Maths'))
  print('############ sets ###########')
  #sets
  set1 = {'red', 'yellow', 'biscuit', 'candy', 'fiction'}
  set2 = {'blue','red','orang'}
  set3 = {'candy', 'biscuit','wafers','blue'}
  print('elements of set1 ###########', set1)
  print('elements of set2 ###########', set2)
  print('elements of set3 ###########', set3)
  print('before adding an element to set1', set1)
  set1.add('India')
  print('after adding an element to set1', set1)
  print('#########################')
  print ('the difference of set1 and set 2 is', set1.difference(set2))
  print('#########################')
  print('the intersection of set2 and set3 is',set2.intersection(set3))
  print('#########################')
  print('the union of set2 and set3 is',set2.union(set3))
  print('#########################')
  print('set1 is subset of set2 ? ', set1.issubset(set2))
  print('#########################')
  print('set2 is subset of set3 ? ', set2.issubset(set3))
  print('#########################')
  print('is set1 disjoint to set2?',set1.isdisjoint(set2))
  print('#########################')
  print('set3 after popping an element',set3.pop())
  print('set3 contains:', set3)
  print('#########################')
  set1.remove('fiction')
  print('set1 after removing an element',set1)
  print('#########################')
  set4=set2.copy()
  print('set4 contains',set4)
  print('#########################')
  set2.clear()
  print('set2 contains',set2)
main()
