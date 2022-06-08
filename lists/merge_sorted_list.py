#!/bin/python3

# # merge sorted lists
# """
# Step 1: Define a function that takes two lists as arguments
# Step 2: Create an empty list (result list) to store the out put of both lists
# Step 3: Create indexes (index1 for list1, index2 for list2, indexr for result) for both lists and set them to 0
# Step 4: Iterate through both lists to combine them into one list (result list)
# Step 5: order the result list while comparing the elements of both lists
#         condition: while both indexes are less than the length of their respective lists
#         compare the first index of both lists and add the smaller element to the result list
#         Increase the index of the smaller list by 1
# Step 6: copy the remaining elements of the list that is not empty into the result list
# Step 7: return the result list
# """

"""
Step 1: initialize two new variables to track the index of both the lists (to zero as the first elemetn of the list is 0)
Step 2: compare the current elements of both. 
Step 3: Filter if the current element of the first list is greater than the current element of the second list,
Step 4: insert the current element of the second list in place of the current element of the first list 
        and increment both index variables by 1
Step 5: copy the reamining elements of the second list into the first list
"""

def merge_sorted_list(list1, list2):   # step 1
    index1 = 0                         # step 3
    index2 = 0

    while index1 < len(list1) and index2 < len(list2): #
        if list1[index1] > list2[index2]:
            list1.insert(index1, list2[index2])
            index2 += 1
            index1 += 1
        else:
            index1 += 1
# this is the pythonic way to copy the remaining elements of the list that is not empty into the result list
    if index2 < len(list2): 
        list1.extend(list2[index2:])
    return list1           

    
print(merge_sorted_list([4, 5, 6], [-2, -1, 0, 7]))