def calculate_y_value(x: list):
    x1, y1, x2, y2, x3 = x.split(",")
    if x1 == x2:
        return None
    else:
        k = (y2-y1)/(x2-x1)
        b = y1-k*x1
        y3 = k*x3 + b
        return y3
