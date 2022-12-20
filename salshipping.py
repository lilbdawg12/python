weight = 80
cost_ground = 0
cost = 0
#ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <=2 or weight <=6:
  cost_ground = weight * 3 + 20
elif weight <=6 or weight <=10:
  cost_ground = weight * 4 + 20 
else: 
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $",cost_ground)

cost_ground_premium = 125.00
print('Ground Shipping Premium $', cost_ground_premium)
#drone shipping
if weight <=2:
  cost = weight * 4.50
elif weight <=2 or weight <=6:
  cost = weight * 9.00
elif weight <= 6 or weight <= 10:
  cost = weight * 12

else:
  cost = weight * 14.25

print("Drone Shipping $",cost)

