class Function:
    def __init__(self, function):
        self.__function = function

    def call(self, *args):
        return self.__function(*args)
