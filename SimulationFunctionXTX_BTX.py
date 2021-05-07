import numpy
import scipy.optimize


class SimulationFunctionXTX_BTX:
    """This class representing the simulation function which has been considered as \"Transpose(X) * A * X +Bi * X
      (Assumed A=2*In in)\". This class can be used to calculate the gradient and hessian of the mentioned function. """

    def __init__(self, b_sum, b_list):
        self.b_sum = b_sum
        self.b_list = b_list

    @staticmethod
    def get_fn(x: numpy.array, b: numpy.array) -> numpy.array:
        """This method can be used to calculate the outcome of the function for each given Xi and Bi"""
        # XTAX +BiX
        f = numpy.matmul(numpy.matmul(numpy.transpose(x)), x) + numpy.matmul(numpy.transpose(b), x)
        return f

    @staticmethod
    def get_gradient_fn(x: numpy.array, b: numpy.array) -> numpy.array:
        """This method can be used to calculate the gradient for any given Xi."""
        # 2Ax+Bi
        A = 2 * numpy.eye(x.size)
        return numpy.matmul(A, x) + b

    @staticmethod
    def get_hessian_fn(x: numpy.array) -> numpy.array:
        """This method can be used to calculate the hessian for any given Xi."""
        # 2A
        return 2 * numpy.eye(x.size)

    def get_optimum_x(self, number_of_nodes):
        return ((1 / (number_of_nodes)) * self.b_sum)

    # """This part has been recently added"""

    def get_min_fn_i(self, i):
        """This method can be used to calculate the outcome of the function for each given Xi and Bi"""

        # XTAX +BiX
        def function(x, b):
            return numpy.matmul(numpy.transpose(x), x) + numpy.matmul(numpy.transpose(b), x)

        return scipy.optimize.fmin(function, numpy.array([2, 2, 1, 4]), xtol=1e-8, args=(self.b_list[i],))
        # self.x0 = np.array([2, 2, 1, 4])
        # return f

    @staticmethod
    def get_gradient_g(x: numpy.array) -> numpy.array:
        """This method can be used to calculate the gradient for any given Xi."""
        # 2Ax
        A = 2 * numpy.eye(x.size)
        return numpy.matmul(A, x)

    @staticmethod
    def get_hessian_g(x: numpy.array) -> numpy.array:
        """This method can be used to calculate the hessian for any given Xi."""
        # 2A
        #print("Inside Hessian of G:  \n")
        #print("x.size  " + str(x.size))

        #print(numpy.eye(x.size))
        return numpy.eye(x.size)
