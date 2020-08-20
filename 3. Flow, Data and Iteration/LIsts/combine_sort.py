"""
	Author: AnOnYmOus001100
	Date: 20/08/2020
	Description:
Write a function named combine_sort that has two parameters named lst1 and lst2.

The function should combine these two lists into one new list and sort the result. Return the new sorted list.
"""
#Code:
#Write your function here
def combine_sort(list1,list2):
  lst = list1 + list2
  lst.sort()
  return lst

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
