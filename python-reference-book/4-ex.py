width = float(input("Enter the width of field (in feet): "))
length = float(input("Enter the length of field (in feet): "))

area = width * length
area_in_acre = area / 43560

print("The area of the  is", area_in_acre, "acre")
