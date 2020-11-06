import config
from DE.errors import DE_Error
from DE.exact_solution import ExactSolution
from DE.numerical_methods import NumericalMethod
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox, CheckButtons


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

        self.e1.set_data(e_euler_x, e_euler_y)
        self.e2.set_data(e_improved_euler_x, e_improved_euler_y)
        self.e3.set_data(e_runge_kutta_x, e_runge_kutta_y)

        self.p1.set_data(euler_x, euler_y)
        self.p2.set_data(improved_euler_x, improved_euler_y)
        self.p3.set_data(runge_kutta_x, runge_kutta_y)
        self.p4.set_data(exact_solution_x, exact_solution_y)

        plt.draw()

    def hide_or_show(self, label):
        """
        Method to hide or show the line in a plot

        :param label:
        :return:
        """
        self.lines[self.names.index(label)].set_visible(not self.lines[self.names.index(label)].get_visible())
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
        plt.subplot(2, 1, 1)
        plt.title("f(x,y)=y/x-y-x")
        plt.xlim(1, 10)
        plt.ylim(-10, 20)
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

        # Local Errors
        plt.subplot(2, 1, 2)
        plt.title("Local Errors")
        plt.xlim(1, 10)
        plt.ylim(0, 10)
        e_euler_x, e_euler_y = DE_Error.compute_gte(exact_solution_x, euler_y, exact_solution_y)
        e_improved_euler_x, e_improved_euler_y = DE_Error.compute_gte(exact_solution_x, improved_euler_y,
                                                                      exact_solution_y)
        e_runge_kutta_x, e_runge_kutta_y = DE_Error.compute_gte(exact_solution_x, runge_kutta_y, exact_solution_y)

        self.e1, = plt.plot(e_euler_x, e_euler_y, linewidth=2, color=config.EULER_COLOR,
                            label="Euler method local error")
        self.e2, = plt.plot(e_improved_euler_x, e_improved_euler_y, linewidth=2, color=config.IMPROVED_EULER_COLOR,
                            label="Improved euler method local error")
        self.e3, = plt.plot(e_runge_kutta_x, e_runge_kutta_y, linewidth=2, color=config.RUNGE_KUTTA_COLOR,
                            label="Runge kutta method local error")
        plt.legend()
        # Show the graphic
        plt.grid()
        plt.show()
