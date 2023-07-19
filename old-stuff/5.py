# try:
#     x = float(input("Enter Hours: "))
#     y = float(input("Enter Rate: "))
#     if x > 40:
#         x1 = x - 40
#         pay = 40 * y + (x1 * y * 1.5)
#         print(pay)
# except:
#     print("plaese only wite numbers")
try:
    x = float(input('Enter score: '))
    if x > 1.0:
        print('Bad Score')
    elif x >= 0.9:
        print('A')
    elif x >= 0.8:
        print('B')
    elif x >= 0.7:
        print('C')
    elif x >= 0.6:
        print('D')
    elif x < 0.6:
        print('F')
    elif x < 0.0:
        print('Bad score')

except:
    print('enter a valid score')
