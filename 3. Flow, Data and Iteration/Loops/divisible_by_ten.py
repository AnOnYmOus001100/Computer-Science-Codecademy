"""
	Author: AnOnYmOus001100
	Date: 21/08/2020
	Description:
.
Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

Return the count of how many numbers in the list are divisible by 10.
"""
#Code:
#Write your function here
def divisible_by_ten(nums):
  count = 0
  for i in nums:
    if i%10 == 0:
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
