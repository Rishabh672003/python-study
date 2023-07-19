def commute_pay(x, y):
    if x <= 40.0:
        return x * y
    z = x - 40.0
    return (z * y * 1.5) + (40 * y)
def is_float(a):
    try:
        b = float(a)
        return b
    except:
        print("Type a number")
        quit()
d = input("Enter hours: ")
hours = is_float(d)
e = input("Enter rate: ")
rate = is_float(e)
pay = commute_pay(hours, rate)
print("Pay: ",pay)
