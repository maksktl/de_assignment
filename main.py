import math

from DE.exact_solution import ExactSolution
from DE.numerical_methods import NumericalMethod
from Graphic.plotgraphic import PlotGraphic
from function import Function

# differential equation
de = Function(lambda x, y: y / x - y - x)
# exact_solution of equation
exact_solution = Function(lambda x, c: x * (c*math.exp(-x) - 1.0))

if __name__ == "__main__":
    numerical_methods = NumericalMethod(0, 1, 10, 10, de)
    de_solution = ExactSolution(0, 1, 10, 10, exact_solution)
    graphic = PlotGraphic(numerical_methods, de_solution)

    graphic.show()
