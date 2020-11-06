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
