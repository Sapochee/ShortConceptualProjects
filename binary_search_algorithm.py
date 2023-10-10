"""A simple binary search algorithm thats finds its target by splitting a list by half until target is reached
"""

def binary_search(list, target):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end):
        print("Step", steps, ":", list[start:end+1])
        
        steps = steps+1
        middle = (start + end) // 2
        
        if target == list[middle]:
            return middle
        if target < list[middle]:
            end =  middle - 1
        else:
            start = middle + 1
            
    return -1

my_list = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 9

binary_search(my_list, target)