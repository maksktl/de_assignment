import config
from DE.errors import DE_Error
from DE.exact_solution import ExactSolution
from DE.numerical_methods import NumericalMethod
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox, CheckButtons


def max_in_lists(*args):
    res = None
    for i in args:
        if not res:
            res = max(i)
        else:
            tmp = max(i)
            res = max(res, tmp)
    return res


def min_in_lists(*args):
    res = None
    for i in args:
        if not res:
            res = min(i)
        else:
            tmp = min(i)
            res = min(res, tmp)
    return res


class PlotGraphic:
    def __init__(self, numerical_solution: NumericalMethod, exact_solution: ExactSolution):
        self.numerical_solution = numerical_solution
        self.exact_solution = exact_solution
        self.text_x0 = None
        self.text_y0 = None
        self.text_n = None
        self.text_x = None
        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.p4 = None
        self.lines = None
        self.names = None
        self.e1 = None
        self.e2 = None
        self.e3 = None
        self.em1 = None
        self.em2 = None
        self.em3 = None

    def change_info(self, event):
        """
        The method is change initial values according to textboxes  at the plot.

        :param event:
        :return:
        """
        self.numerical_solution.set_y_0(float(self.text_y0.text))
        self.numerical_solution.set_x_0(float(self.text_x0.text))
        self.numerical_solution.set_n(float(self.text_n.text))
        self.numerical_solution.set_x(float(self.text_x.text))

        self.exact_solution.set_y_0(float(self.text_y0.text))
        self.exact_solution.set_x_0(float(self.text_x0.text))
        self.exact_solution.set_n(float(self.text_n.text))
        self.exact_solution.set_x(float(self.text_x.text))

        euler_x, euler_y = self.numerical_solution.euler_method()
        improved_euler_x, improved_euler_y = self.numerical_solution.improved_euler_method()
        runge_kutta_x, runge_kutta_y = self.numerical_solution.runge_kutta_method()
        exact_solution_x, exact_solution_y = self.exact_solution.get_exact_solution()

        e_euler_x, e_euler_y = \
            DE_Error.compute_gte(exact_solution_x, euler_y, exact_solution_y)
        e_improved_euler_x, e_improved_euler_y = \
            DE_Error.compute_gte(exact_solution_x, improved_euler_y, exact_solution_y)
        e_runge_kutta_x, e_runge_kutta_y = \
            DE_Error.compute_gte(exact_solution_x, runge_kutta_y, exact_solution_y)

        plt.subplot(3, 1, 2)
        max_x, min_x = max_in_lists(e_euler_x, e_improved_euler_x, e_runge_kutta_x), \
                       min_in_lists(e_euler_x, e_improved_euler_x, e_runge_kutta_x)

        max_y, min_y = max_in_lists(e_euler_y, e_improved_euler_y, e_runge_kutta_y), \
                       min_in_lists(e_euler_y, e_improved_euler_y, e_runge_kutta_y)
        plt.xlim(min_x, max_x)
        plt.ylim(min_y, max_y)

        self.e1.set_data(e_euler_x, e_euler_y)
        self.e2.set_data(e_improved_euler_x, e_improved_euler_y)
        self.e3.set_data(e_runge_kutta_x, e_runge_kutta_y)

        plt.subplot(3, 1, 1)
        max_x, min_x = max_in_lists(exact_solution_x, euler_x, improved_euler_x, runge_kutta_x), \
                       min_in_lists(exact_solution_x, euler_x, improved_euler_x, runge_kutta_x)
        max_y, min_y = max_in_lists(exact_solution_y, euler_y, improved_euler_y, runge_kutta_y), \
                       min_in_lists(exact_solution_y, euler_y, improved_euler_y, runge_kutta_y)

        plt.xlim(min_x, max_x)
        plt.ylim(min_y, max_y)

        self.p1.set_data(euler_x, euler_y)
        self.p2.set_data(improved_euler_x, improved_euler_y)
        self.p3.set_data(runge_kutta_x, runge_kutta_y)
        self.p4.set_data(exact_solution_x, exact_solution_y)

        _n = [i for i in range(1, int(self.exact_solution.n) + 1)]
        euler_max_error = DE_Error.compute_euler_max_error(self.numerical_solution, self.exact_solution, len(_n))
        improved_euler_max_error = DE_Error.compute_improved_euler_max_error(self.numerical_solution, self.exact_solution, len(_n))
        runge_kutta_max_error = DE_Error.compute_runge_kutta_max_error(self.numerical_solution, self.exact_solution, len(_n))

        self.em1.set_data(_n, euler_max_error)
        self.em2.set_data(_n, improved_euler_max_error)
        self.em3.set_data(_n, runge_kutta_max_error)

        plt.subplot(3, 1, 3)
        max_x, min_x = len(_n), 1
        max_y, min_y = max_in_lists(euler_max_error, improved_euler_max_error, runge_kutta_max_error), \
                       min_in_lists(euler_max_error, improved_euler_max_error, runge_kutta_max_error)
        plt.xlim(min_x, max_x)
        plt.ylim(min_y, max_y)

        plt.draw()
    # qefasd4wsdf4rqq34fqq4432dfaFASdf
    def hide_or_show(self, label):
        """
        Method to hide or show the line in a plot

        :param label:
        :return:
        """
        index = self.names.index(label)
        if index == 0:
            self.p1.set_visible(not self.p1.get_visible())
            self.e1.set_visible(not self.e1.get_visible())
            self.em1.set_visible(not self.em1.get_visible())
        if index == 1:
            self.p2.set_visible(not self.p2.get_visible())
            self.e2.set_visible(not self.e2.get_visible())
            self.em2.set_visible(not self.em2.get_visible())
        if index == 2:
            self.p3.set_visible(not self.p3.get_visible())
            self.e3.set_visible(not self.e3.get_visible())
            self.em3.set_visible(not self.em3.get_visible())
        if index == 3:
            self.p4.set_visible(not self.p4.get_visible())

        plt.draw()

    def show(self):
        """
        Method shows the graphic of solution by Euler, Improved Euler, and Runge Kutta methodsm then
        exact solution.
        And according the following data draw a local error graphic
        :return:
        """

        # Getting x,y values for graphic
        euler_x, euler_y = self.numerical_solution.euler_method()
        improved_euler_x, improved_euler_y = self.numerical_solution.improved_euler_method()
        runge_kutta_x, runge_kutta_y = self.numerical_solution.runge_kutta_method()
        exact_solution_x, exact_solution_y = self.exact_solution.get_exact_solution()

        # Plot the graphic
        fig, ax = plt.subplots()
        plt.grid()

        plt.subplots_adjust(right=0.5)
        plt.subplot(3, 1, 1)
        plt.title("f(x,y)=y/x-y-x")
        max_x, min_x = max_in_lists(exact_solution_x, euler_x, improved_euler_x, runge_kutta_x), \
                       min_in_lists(exact_solution_x, euler_x, improved_euler_x, runge_kutta_x)
        max_y, min_y = max_in_lists(exact_solution_y, euler_y, improved_euler_y, runge_kutta_y), \
                       min_in_lists(exact_solution_y, euler_y, improved_euler_y, runge_kutta_y)

        plt.xlim(min_x, max_x)
        plt.ylim(min_y, max_y)
        self.p1, = plt.plot(euler_x, euler_y, linewidth=2, color=config.EULER_COLOR,
                            label="Euler method")
        self.p2, = plt.plot(improved_euler_x, improved_euler_y, linewidth=2, color=config.IMPROVED_EULER_COLOR,
                            label="Improved euler method")
        self.p3, = plt.plot(runge_kutta_x, runge_kutta_y, linewidth=2, color=config.RUNGE_KUTTA_COLOR,
                            label="Runge kutta method")
        self.p4, = plt.plot(exact_solution_x, exact_solution_y, linewidth=2, color=config.EXACT_SOLUTION_COLOR,
                            label="Exact solution")
        plt.grid()
        plt.legend()

        # Place textboxes for change some values
        ax_text_x0 = plt.axes([0.6, 0.9, 0.2, 0.05])
        self.text_x0 = TextBox(ax=ax_text_x0, label="x0: ", initial=config.x0)

        ax_text_y0 = plt.axes([0.6, 0.8, 0.2, 0.05])
        self.text_y0 = TextBox(ax=ax_text_y0, label="y0: ", initial=config.y0)

        ax_text_n = plt.axes([0.6, 0.7, 0.2, 0.05])
        self.text_n = TextBox(ax=ax_text_n, label="N: ", initial=config.N)

        ax_text_x = plt.axes([0.6, 0.6, 0.2, 0.05])
        self.text_x = TextBox(ax=ax_text_x, label="X: ", initial=config.X)

        # Place a button for applying changes
        ax_change_button = plt.axes([0.6, 0.5, 0.2, 0.05])
        change_button = Button(ax_change_button, 'apply')
        change_button.on_clicked(self.change_info)

        ax_checkbox = plt.axes([0.5, 0.0, 0.5, 0.5])
        self.lines = [self.p1, self.p2, self.p3, self.p4]
        self.names = [str(name.get_label()) for name in self.lines]

        hide_shower = CheckButtons(ax_checkbox, self.names, [True, True, True, True])

        hide_shower.on_clicked(self.hide_or_show)

        ''' Local Errors'''
        plt.subplot(3, 1, 2)
        plt.title("gte")

        e_euler_x, e_euler_y = DE_Error.compute_gte(exact_solution_x, euler_y, exact_solution_y)
        e_improved_euler_x, e_improved_euler_y = DE_Error.compute_gte(exact_solution_x, improved_euler_y,
                                                                      exact_solution_y)
        e_runge_kutta_x, e_runge_kutta_y = DE_Error.compute_gte(exact_solution_x, runge_kutta_y, exact_solution_y)

        max_x, min_x = max_in_lists(e_euler_x, e_improved_euler_x, e_runge_kutta_x), \
                       min_in_lists(e_euler_x, e_improved_euler_x, e_runge_kutta_x)

        max_y, min_y = max_in_lists(e_euler_y, e_improved_euler_y, e_runge_kutta_y), \
                       min_in_lists(e_euler_y, e_improved_euler_y, e_runge_kutta_y)
        plt.xlim(min_x, max_x)
        plt.ylim(min_y, max_y)
        self.e1, = plt.plot(e_euler_x, e_euler_y, linewidth=2, color=config.EULER_COLOR,
                            label="Euler method error")
        self.e2, = plt.plot(e_improved_euler_x, e_improved_euler_y, linewidth=2, color=config.IMPROVED_EULER_COLOR,
                            label="Improved euler method error")
        self.e3, = plt.plot(e_runge_kutta_x, e_runge_kutta_y, linewidth=2, color=config.RUNGE_KUTTA_COLOR,
                            label="Runge kutta method error")
        plt.legend()
        plt.grid()

        '''Max Error'''

        plt.subplot(3, 1, 3)
        plt.title("Max Error")

        _n = [i for i in range(1, int(self.exact_solution.n)+1)]
        euler_max_error = DE_Error.compute_euler_max_error(self.numerical_solution, self.exact_solution, len(_n))
        improved_euler_max_error = DE_Error.compute_improved_euler_max_error(self.numerical_solution, self.exact_solution, len(_n))
        runge_kutta_max_error = DE_Error.compute_runge_kutta_max_error(self.numerical_solution, self.exact_solution, len(_n))

        max_x, min_x = len(_n), 1
        max_y, min_y = max_in_lists(euler_max_error, improved_euler_max_error, runge_kutta_max_error), \
                       min_in_lists(euler_max_error, improved_euler_max_error, runge_kutta_max_error)
        plt.xlim(min_x, max_x)
        plt.ylim(min_y, max_y)

        self.em1, = plt.plot(_n, euler_max_error, linewidth=2, color=config.EULER_COLOR, label="Euler max error")
        self.em2, = plt.plot(_n, improved_euler_max_error, linewidth=2, color=config.IMPROVED_EULER_COLOR, label="Improved Euler max error")
        self.em3, = plt.plot(_n, runge_kutta_max_error, linewidth=2, color=config.RUNGE_KUTTA_COLOR, label="Runge Kutta max error")
        plt.legend()
        plt.grid()

        plt.show()
