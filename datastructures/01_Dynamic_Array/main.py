from dynamic_array import *

array = DynamicArray()
array.append('a')
array.append('b')
array.append('d')
array.append('e')
print(array)

array.insert(-4, 'c')

print(array)