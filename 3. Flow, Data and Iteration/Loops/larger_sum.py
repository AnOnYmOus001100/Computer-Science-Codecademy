"""
	Author: AnOnYmOus001100
	Date: 21/08/2020
	Description:
Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.
"""
#Code:
#Write your function here
def larger_sum(lst1,lst2):
  sum_lst1 = 0
  sum_lst2 = 0
  for e in lst1:
    sum_lst1 += e
  for e in lst2:
    sum_lst2 += e

  if (sum_lst1 > sum_lst2) or (sum_lst1 == sum_lst2):
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
