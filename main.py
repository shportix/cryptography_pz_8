from ecdsa import curves, ellipticcurve
import secrets


class ECPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def double_ec_points(self):
        _curve = get_base_curve()
        point = ellipticcurve.Point(_curve, self.x, self.y)
        point = point.double()
        self.x = point.x()
        self.y = point.y()

def ec_point_gen(x, y):
    point = ECPoint(x, y)
    if is_on_curve_check(point):
        return point
    return False


def base_point_g_get():
    _curve = curves.NIST256p
    _base_point = _curve.generator
    _base_point = ECPoint(_base_point.x(), _base_point.y())
    return _base_point

def get_base_curve():
    _curve = curves.NIST256p.curve
    return _curve

def is_on_curve_check( _point: ECPoint):
    try:
        _curve  = get_base_curve()
        _f = ellipticcurve.Point(_curve, _point.x, _point.y)
    except AssertionError:
        return False
    return True

def add_ec_points(_a: ECPoint, _b: ECPoint):
    _curve = get_base_curve()
    _a = ellipticcurve.Point(_curve, _a.x, _a.y)
    _b = ellipticcurve.Point(_curve, _b.x, _b.y)
    _c = _a + _b
    _c = ECPoint(_c.x(), _c.y())
    return _c



def scalar_multiple(k, point: ECPoint):
    _curve = get_base_curve()
    point = ellipticcurve.Point(_curve, point.x, point.y)
    point_2 = k * point
    point_2 = ECPoint(point_2.x(),point_2.y())
    return point_2

def is_equal_points(point_1: ECPoint, point_2: ECPoint):
    return (point_1.x == point_2.x) and (point_1.y == point_2.y)

def ec_point_to_string(point: ECPoint):
    string = str(point.x) + " " + str(point.y)
    return string

def string_to_ec_point(string:str):
    res = string.split()
    point = ECPoint(int(res[0]), int(res[1]))
    return point

def print_ec_point(point: ECPoint):
    print(f"x: {point.x}, y: {point.y}")

if __name__ == '__main__':
    g = base_point_g_get()
    # вивід базової точки
    print_ec_point(g)
    # подвоєння точки
    g.double_ec_points()
    # вивід подвоєної точки
    print_ec_point(g)
    k = secrets.randbits(256)
    d = secrets.randbits(256)
    H1 = scalar_multiple(d, g)
    H2 = scalar_multiple(k, H1)

    H3 = scalar_multiple(k, g)
    H4 = scalar_multiple(d, H3)

    result = is_equal_points(H2, H4)
    print(result)
