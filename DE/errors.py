from DE.exact_solution import ExactSolution
from DE.numerical_methods import NumericalMethod


class DE_Error:
    def __init__(self):
        pass

    @staticmethod
    def compute_gte(list_x, y_to_compare, exact_y):
        """
        Calculate Local Errors

        :param list_x:
        :param y_to_compare:
        :param exact_y:
        :return:
        """
        res = []
        for i in range(len(list_x)):
            res.append(abs(exact_y[i] - y_to_compare[i]))
        return list_x, res

    @staticmethod
    def compute_euler_max_error(numerical_solution: NumericalMethod, exact_solution: ExactSolution, n: int):
        y_errors = []
        for i in range(1, n + 1):
            numerical_solution.set_n(i)
            exact_solution.set_n(i)
            e_x, e_y = numerical_solution.euler_method()
            x, y, = exact_solution.get_exact_solution()
            x_gte, y_gte = DE_Error.compute_gte(x, e_y, y)

            y_errors.append(max(y_gte))
        return y_errors

    @staticmethod
    def compute_improved_euler_max_error(numerical_solution: NumericalMethod, exact_solution: ExactSolution, n: int):
        y_errors = []
        for i in range(1, n + 1):
            numerical_solution.set_n(i)
            exact_solution.set_n(i)
            e_x, e_y = numerical_solution.improved_euler_method()
            x, y, = exact_solution.get_exact_solution()
            x_gte, y_gte = DE_Error.compute_gte(x, e_y, y)

            y_errors.append(max(y_gte))
        return y_errors

    @staticmethod
    def compute_runge_kutta_max_error(numerical_solution: NumericalMethod, exact_solution: ExactSolution, n: int):
        y_errors = []
        for i in range(1, n + 1):
            numerical_solution.set_n(i)
            exact_solution.set_n(i)
            e_x, e_y = numerical_solution.runge_kutta_method()
            x, y, = exact_solution.get_exact_solution()
            x_gte, y_gte = DE_Error.compute_gte(x, e_y, y)

            y_errors.append(max(y_gte))
        return y_errors
