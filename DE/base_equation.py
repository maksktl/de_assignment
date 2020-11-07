from function import Function


class BDE:
    def __init__(self, y_0: float, x_0: float, n: float, x: float, f: Function):
        self.y_0 = y_0
        self.x_0 = x_0
        self.n = n
        self.x = x
        self.f = f
        self.h = ((self.x - self.x_0) / self.n)

    def set_x_0(self, x_0):
        self.x_0 = x_0
        self.h = ((self.x - self.x_0) / self.n)

    def set_y_0(self, y_0):
        self.y_0 = y_0

    def set_x(self, x):
        self.x = x
        self.h = ((self.x - self.x_0) / self.n)

    def set_n(self, n):
        self.n = n
