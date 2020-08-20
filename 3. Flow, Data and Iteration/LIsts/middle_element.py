"""
	Author: AnOnYmOus001100
	Date: 20/08/2020
	Description:
Create a function called middle_element that has one parameter named lst.

If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.
"""
#Code:
#Write your function here
def middle_element(lst):
  l = len(lst)
  mid = l//2
  if l%2 == 0:
    return (lst[mid-1]+lst[mid])/2
  else:
    return lst[mid]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
