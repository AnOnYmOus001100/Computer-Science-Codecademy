"""
	Author: AnOnYmOus001100
	Date: 16/08/2020
	Description:
	Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

Premium Ground Shipping

Flat charge: $125.00

Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.
"""

#Code:
flat_charge = 0.00
cost = 0.00
# ground shipping, takes weight and returns cost
def ground_shipping(weight):
  cost = 0.00
  flat_charge = 20.00
  if weight <= 2:
    cost = 1.50
  elif weight > 2 and weight <= 6:
    cost = 3.00
  elif weight > 6 and weight <= 10:
    cost = 4.00
  else:
    cost = 4.75
  
  return weight*cost + flat_charge

# testing ground_shipping function with weight 8.4lbs
print (ground_shipping(8.4))

flat_charge = 125.00
premium_ground_shipping = cost + flat_charge

# drone_shipping functions takes weight returns cost
def drone_shipping(weight):
  cost = 0.00
  flat_charge = 0.00
  if weight <=2:
    cost = 4.50
  elif weight > 2 and weight <= 6:
    cost = 9.00
  elif weight > 6 and weight <= 12:
    cost = 12.00
  else:
    cost = 14.25

  return weight*cost + flat_charge

# testing drone_shipping function with weight 1.5lbs
print (drone_shipping(1.5))

# returns the cheapest shipping method and cost, takes weight
def cheapest_shipping_method(weight):
  if (ground_shipping(weight) < drone_shipping(weight)) and ground_shipping(weight) < premium_ground_shipping:
    print ("Ground Shipping is Cheapest.")
    return ground_shipping(weight)
  elif (drone_shipping(weight) < ground_shipping(weight)) and (drone_shipping < premium_ground_shipping):
    print ("Drone Shipping is Cheapest.")
    return drone_shipping(weight)
  else:
    print ("Premium Ground Shipping is Cheapest.")
    return premium_ground_shipping

# testing cheapest_shipping_method with weight 4.8lbs and  41.5lbs
print (cheapest_shipping_method(4.8))
print (cheapest_shipping_method(41.5))
