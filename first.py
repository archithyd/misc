def multiply(f, b):
    x = str(f)
    y = str(b)
    n = max(len(x), len(y))
    if n == 1:
        return x*y
    xl, xr = x[:len(x) // 2], x[len(x) // 2:len(x)]
    yl, yr = y[:len(y) // 2], y[len(x) // 2:len(y)]

    xl, xr = int(xl), int(xr)
    yl, yr = int (yl), int (yr)


    p1 = xl*yl
    p2 = xr * yr
    p3 = (xl+xr) * (yl+yr)

    return p1*pow(10, n) + (p3-p2-p1)*pow(10, n//2) + p2

print(multiply(3456,2324))