#Access and read a value
new_list = [1, 2, 3]
result = new_list[0]

#Linear search for a value
if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)

        break

#Insert, Append & Extend
    #insert adds the item to the start of the list which has a linear runtime

numbers = []
len(numbers)
numbers.insert(1, 2)
    #appending adds the item at the end of the list which has a constant time

numbers = []
numbers.append(2)
numbers.append(200)

    #extend adds a set of new items or list to an empty of existing list of array and has a runtime of O(k) where k represent the number of elements that is added to the existing list

numbers = []
numbers.extend([4, 5, 6])

#Delete operation; similar to insert operation in that when the operation occurs, there is need to maintain direct index of the values. Just as insert shifts every element to the right, delete shifts them to the left. it also has upper bound time of O(n) Linear runtime.

