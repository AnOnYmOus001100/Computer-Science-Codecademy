"""
	Author: AnOnYmOus001100
	Date: 20/08/2020
	Description:
Create a function named more_frequent_item that has three parameters named lst, item1, and item2.

Return either item1 or item2 depending on which item appears more often in lst.

If the two items appear the same number of times, return item1.
"""
#Code:
#Write your function here
def more_frequent_item(lst,item1,item2):
  if (lst.count(item1) > lst.count(item2)) or  (lst.count(item1) == lst.count(item2)):
    return item1
  else:
    return item2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
