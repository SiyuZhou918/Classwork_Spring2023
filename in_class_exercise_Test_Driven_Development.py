def calculate_y_value(x: list):
    x1 = x[0]
    y1 = x[1]
    x2 = x[2]
    y2 = x[3]
    x3 = x[4]
    if x1 == x2:
        return None
    else:
        k = (y2-y1)/(x2-x1)
        b = y1-k*x1
        y3 = k*x3 + b
        return y3
