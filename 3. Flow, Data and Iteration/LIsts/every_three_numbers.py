"""
	Author: AnOnYmOus001100
	Date: 20/08/2020
	Description:
Create a function called every_three_nums that has one parameter named start.

The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.
"""
#Code:
#Write your function here
def every_three_nums(start):
  lst = []
  if start > 100:
    return lst
  for i in range(start,101,3):
    lst.append(i)
  return lst


#Uncomment the line below when your function is done
print(every_three_nums(91))
print (every_three_nums(110))
