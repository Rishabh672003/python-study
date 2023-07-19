RATE = 0.04

principle = float(input("Enter the Principle amount: "))

principle_1 = principle * RATE + principle
principle_2 = principle_1 * RATE + principle_1
principle_3 = principle_2 * RATE + principle_2

print("Principle at 1 year: ","%.2f" % principle_1)
print("Principle at 2 year: ","%.2f" % principle_2)
print("Principle at 3 year: ","%.2f" % principle_3)
