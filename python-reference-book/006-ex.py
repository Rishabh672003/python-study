cost = float(input("Enter the total cost of meal: "))

gst = cost * 0.18
tip = cost * 0.18

total_cost = cost + gst + tip

print("Total cost of meal is:", "%.2f" % total_cost)
