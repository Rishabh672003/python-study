import math

print(
    'THis is a program to solve a equation in the form ax^3 + bx^2 + cx + d = 0'
)
print('Write the coefficients below i.e a,b,c and d.')

try:
    alpha = input(
        print(
            """what do you want to do -
                        a2 = simple mathematic
                        b2 = solve equation
                        c2 = trigonometric"""
        )
    )
    if alpha == 'a':
        beta = input(
            print(
                """what do you want to do- 
                     1.add
                     2.subtract
                     3.multiply
                     4.divide
                     5.logarithm"""
            )
        )

    elif alpha == 'b':
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        d = float(input('d = '))
        if a == 0:
            if b == 0:
                print('roots is ', -d / c)
            else:
                if math.pow(c, 2) - 4 * b * d > 0:
                    print('Roots are Real and Unequal')
                    print(
                        'Roots are',
                        (-c + math.sqrt(c**2 - 4 * b * d)) / (2 * b),
                        'and',
                        (-c - math.sqrt(c**2 - 4 * b * d)) / (2 * b),
                    )
                elif math.pow(c, 2) - 4 * b * d < 0:
                    print('Roots are Complex and Imaginary ')
                elif math.pow(c, 2) - 4 * b * d == 0:
                    print('Roots are Real and Equal')
                    print(
                        'both Roots are ',
                        (-c - math.sqrt(c**2 - 4 * b * d)) / (2 * b),
                    )
        else:
            f = ((3 * c) / a - ((math.pow(b, 2)) / math.pow(a, 2))) / 3
            g = (
                (2 * math.pow(b, 3)) / math.pow(a, 3)
                - ((9 * b * c) / math.pow(a, 2))
                + ((27 * d) / a)
            ) / 27
            h = math.pow(g, 2) / 4 + math.pow(f, 3) / 27
            if h < 0:
                i = math.pow(((math.pow(g, 2) / 4) - h), 0.5)
                j = math.pow(i, 1 / 3)
                k = math.acos(-g / (2 * i))
                z = -1 * j
                m = math.cos(k / 3)
                n = math.sqrt(3) * math.sin(k / 3)
                p = (b / (3 * a)) * (-1)
                x1 = (2 * j * math.cos(k / 3)) - (b / (3 * a))
                x2 = (z * (m + n)) + p
                x3 = (z * (m - n)) + p
                print('All roots are real.')
                print('Roots are', x1, x2, 'and', x3)
            elif h > 0:
                r = (-g / 2) + math.pow(h, 0.5)
                s = math.pow(abs(r), 1 / 3)
                t = (-g / 2) - math.pow(h, 0.5)
                if t > 0:
                    u = math.pow(t, float(1) / 3)
                elif t < 0:
                    u = -math.pow(abs(t), float(1) / 3)
                elif t == 0:
                    u = 0
                i1 = 'i'
                x4 = (s + u) - (b / (3 * a))
                x51 = -((s + u) / 2) - (b / (3 * a))
                x52 = ((s - u) * math.sqrt(3)) / 2
                print('Only one root is real. ')
                print(
                    'roots are',
                    x4,
                    ',',
                    x51,
                    '+ i*',
                    x52,
                    'and',
                    x51,
                    '- i*',
                    x52,
                )
            elif f == 0 and g == 0 and h == 0:
                x6 = math.pow(d / a, 1 / 3) * (-1)
                print('All roots are', x6)
except:
    print('please enter a valid number')
