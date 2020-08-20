"""

	Author: AnOnYmOus001100
	Date: 20/08/2020
	Description:
Write a function named larger_list that has two parameters named lst1 and lst2.

The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.
"""

#Code:
#Write your function here
def larger_list(lst1,lst2):
  # if both lst1 has more elements or both equal, then return last element of lst1
  if (len(lst1) > len(lst2)) or (len(lst1) == len(lst2)):
    return lst1[-1]
  # otherwise return last element of lst2
  else:
    return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
