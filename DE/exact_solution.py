import math

from DE.base_equation import BDE
from function import Function


class ExactSolution(BDE):
    def __init__(self, y_0: float, x_0: float, n: float, x: float, f: Function):
        super().__init__(y_0, x_0, n, x, f)

    def get_exact_solution(self):
        """
        The method to get exact solution
        :return:
        """
        res_x = [self.x_0]
        res_y = [self.y_0]
        C = math.exp(self.x_0)*(self.x_0+self.y_0)/self.x_0

        for i in range(1, int(self.n)+1):
            res_x.append(res_x[i - 1] + self.h)
            res_y.append(self.f.call(res_x[i], C))

        return res_x, res_y
