"""	
	Author: AnOnYmOus001100
	Date: 21/08/2020
	Description:
Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums

"""
#Code:
#Write your function here
def max_num(nums):
  max_num = nums[0]
  for e in nums:
    if e > max_num:
      max_num = e
  return max_num

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
