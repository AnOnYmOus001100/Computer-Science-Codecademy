"""
	Author: AnOnYmOus001100
	Date: 20/08/2020
	Description:
Create a function called append_size that has one parameter named lst.

The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.

For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.
"""
#Code:
#Write your function here
def append_size(lst):
  lst.append(len(lst))
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))
