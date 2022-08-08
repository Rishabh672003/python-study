def is_float(a):
    try:
        b = float(a)
        c = True
        return c
    except:
        return False


while True:
    line = input('Enter a Number: ')
    count = 0
    total = 0.0
    if is_float(line) == True:
        for lines in line:
            try:
                count += 1
                print(count)
            except:
                break
        continue
    elif is_float(line) == False:
        if line == 'done':
            break
        else:
            print('Invalid input')
            continue


#
# def check_for_float(input1, exit=True):
#     """
#     Checks if the type of "input1" is a float and returns the value if so.
#     Input:    input1 -- variable to check
#     Output: val -- value of float
#     """
#     try:
#         val = float(input1)                   # Only allows input floats
#         return val
#     except (ValueError, TypeError):
#         print('Error, please enter numeric input')
#         if exit:
#             quit()
#         return False
#
#
#
# if __name__ == '__main__':
#     count = 0                                 # Initializes values
#     total = 0.0
#     average = 0.0
#
#     while True:                               # Stays in loop until break
#         input_number = input('Enter a number: ')
#         if input_number == 'done':
#             break                             # Exits the while loop
#
#         number = check_for_float(input_number, False)
#         if not number:
#             continue
#
#         count += 1                            # Counter
#         total = total + number                # Running total
#
#     # Ensures count is not 0 which would cause division error
#     if count:
#         average = total / count               # Computes the average
#
#     print(total, count, average)
