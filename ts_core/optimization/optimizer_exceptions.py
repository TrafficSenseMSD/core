class OptimizerException(Exception):
    """
    Base Exception class for Optimizer objects
    """


class OptimizerInputError(OptimizerException):
    """
    Parameters
    ----------
    message: explanation of the error

    """

    def __init__(self, message):
        self.message = message

