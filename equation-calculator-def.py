import math

print(
    'THis is a program to solve a equation in the form ax^3 + bx^2 + cx + d = 0'
)
print('Write the coefficients below i.e a, b, c and d.')


def eq(a: float, b: float, c: float, d: float) -> None:
    if a == b == c == d == 0:
        print('0 == 0')
    elif a == b == c == 0:
        print("learn maths")
    else:
        try:
            discriminant = math.pow(c, 2) - 4 * b * d
            beta = 2 * b
            if a == 0:
                if b == 0:
                    theta = -d / c
                    print('roots is ', theta)
                else:
                    if discriminant > 0:
                        print('Roots are Real and Unequal')
                        zeta = round((-c + math.sqrt(discriminant)) / (beta), 4)
                        gamma = round((-c - math.sqrt(discriminant)) / (beta), 4)
                        print('Roots are', zeta, 'and', gamma)
                    elif discriminant < 0:
                        iota = round(-c / (beta), 4)
                        delta = round(math.sqrt(abs(discriminant)) / (beta), 4)
                        print('Roots are Complex and Imaginary ')
                        print(
                            'Root are',
                            iota,
                            '+',
                            'i *',
                            delta,
                            'and',
                            iota,
                            '-',
                            'i *',
                            delta,
                        )
                    elif discriminant == 0:
                        print('Roots are Real and Equal')
                        epsilon = -c / (2 * beta)
                        print('both Roots are ', epsilon)
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
                    x1 = round((2 * j * math.cos(k / 3)) - (b / (3 * a)), 4)
                    x2 = round((z * (m + n)) + p, 4)
                    x3 = round((z * (m - n)) + p, 4)
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
                    x4 = round((s + u) - (b / (3 * a)), 4)
                    x51 = round(-((s + u) / 2) - (b / (3 * a)), 4)
                    x52 = round(((s - u) * math.sqrt(3)) / 2, 4)
                    print('Only one root is real. ')
                    print(
                        'roots are -',
                        x4,
                        ',',
                        x51,
                        '+ i *',
                        x52,
                        'and',
                        x51,
                        '- i *',
                        x52,
                    )
                elif f == 0 and g == 0 and h == 0:
                    x6 = round(math.pow(d / a, 1 / 3) * (-1), 4)
                    print('All roots are', x6)
        except:
            print("error")
            exit()

try:
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    d = float(input('d = '))
    alpha = eq(a, b, c, d)
except:
    print("math is done through numbers not alphabets you dumb shit")

