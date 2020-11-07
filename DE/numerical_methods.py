from DE.base_equation import BDE
from function import Function


class NumericalMethod(BDE):
    def __init__(self, y_0: float, x_0: float, n: float, x: float, f: Function):
        super().__init__(y_0, x_0, n, x, f)

    def euler_method(self):
        res_x = [self.x_0]
        res_y = [self.y_0]

        for i in range(int(self.n)):
            res_x.append(res_x[i] + self.h)
            res_y.append(res_y[i] + self.h * self.f.call(res_x[i], res_y[i]))

        return res_x, res_y

    def improved_euler_method(self):
        res_x = [self.x_0]
        res_y = [self.y_0]

        for i in range(int(self.n)):
            f = self.f.call(res_x[i], res_y[i])
            k1 = res_x[i] + self.h / 2
            k2 = res_y[i] + self.h * f / 2
            res_x.append(res_x[i] + self.h)
            res_y.append(res_y[i] + self.h*self.f.call(k1, k2))

        return res_x, res_y

    def runge_kutta_method(self):
        res_x = [self.x_0]
        res_y = [self.y_0]

        for i in range(int(self.n)):
            k1 = self.f.call(res_x[i], res_y[i])
            k2 = self.f.call(res_x[i] + self.h / 2, res_y[i] + self.h * k1 / 2)
            k3 = self.f.call(res_x[i] + self.h / 2, res_y[i] + self.h * k2 / 2)
            k4 = self.f.call(res_x[i] + self.h, res_y[i] + self.h * k3)
            res_x.append(res_x[i] + self.h)
            res_y.append(res_y[i] + (self.h / 6) * (k1 + 2 * k2 + 2 * k3 + k4))

        return res_x, res_y
