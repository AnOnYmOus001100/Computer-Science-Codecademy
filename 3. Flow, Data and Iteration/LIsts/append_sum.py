"""
	Author: AnOnYmOus001100
	Date: 20/08/2020
	Description:
	Write a function named append_sum that has one parameter — a list named named lst.

The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].
"""
#Code:
#Write your function here
def append_sum(lst):
  for i in range(0,3):
    lst.append(lst[-2]+lst[-1])
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
