# def commute_pay(x, y):
#     # x = float(input('Enter Hours: '))
#     # y = float(input('Enter Rate: '))
#     if x > 40:
#         x1 = x - 40
#         pay = 40 * y + (x1 * y * 1.5)
#         return pay
#     else:
#         pay = x * y
#         return pay
# # a = commute_pay(45, 12)
# # return(a)
# a = commute_pay(45, 10)
# return(a)
# b = commute_pay(50, 100)
# return(b)

# x = float(input('Enter score: '))
def commute_grade(y):
    if y > 1.0:
        return 'Bad Score'
    elif y >= 0.9:
        return 'A'
    elif y >= 0.8:
        return('B')
    elif y >= 0.7:
        return('C')
    elif y >= 0.6:
        return('D')
    elif y < 0.6:
        return('F')
    elif y < 0.0:
        return('Bad score')
    else:
        return "bad score"

x = float(input("score: "))
grade = commute_grade(x)
print(grade)

# return(a)
# return('enter a valid score')
