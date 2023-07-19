less = float(input("Enter the number of containers <= 1 Liters: "))
more = float(input("Enter the number of containers > 1 Liters: "))

total = less * 0.10 + more * 0.25

total_dec = "%.2f" % total

print("Total deposit you will get is: ", total_dec, "$", sep="")
