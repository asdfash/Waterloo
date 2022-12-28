# version 1.1

from abc import ABC, abstractmethod, abstractproperty

import numpy as np

##################################################################################################################
# ACTIVATION FUNCTIONS
##################################################################################################################

class Activation(ABC):
    '''
    An abstract class that implements an activation function
    '''

    @abstractmethod
    def value(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of evaluating the activation function with input x
        :param x: input to activation function
        :return: value of the activation function, with shape x.shape
        '''
        return x

    @abstractmethod
    def derivative(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of evaluating the derivative of the activation function with input x
        :param x: input to activation function
        :return: derivative of the activation function, with shape x.shape
        '''
        return x

class Identity(Activation):
    '''
    Implements the identity activation function (i.e. g(x) = x)
    '''

    def value(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of applying the Identity activation function (i.e. returns the input)
        :param x: input to the activation function
        :return: value of the activation function, with shape x.shape
        '''
        return x

    def derivative(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of evaluating the derivative of the identity function with input x (i.e. 1s)
        :param x: input to identity function
        :return: derivative of the activation function, with shape x.shape
        '''
        return np.ones(x.shape)

class Sigmoid(Activation):
    '''
    Implements the sigmoid activation function
    :attr k: Parameter of the sigmoid function that controls its steepness around the origin
    '''

    def __init__(self, k: float=1.):
        '''
        :param k: Parameter of the sigmoid function that controls its steepness around the origin
        '''
        self.k = k
        super(Sigmoid, self).__init__()

    def value(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of evaluating the sigmoid function with input x
        :param x: input to sigmoid function
        :return: value of the activation function, with shape x.shape
        '''

        '''
        #### YOUR CODE HERE ####
        '''
        return x

    def derivative(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of evaluating the derivative of the sigmoid function with input x
        :param x: input to sigmoid function
        :return: derivative of the activation function, with shape x.shape
        '''
        '''
        #### YOUR CODE HERE ####
        '''
        return x

class Tanh(Activation):
    '''
    Implements the hyperbolic tangent activation function
    '''

    def __init__(self):
        super(Tanh, self).__init__()

    def value(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of evaluating the hyperbolic tangent function with input x
        :param x: input to activation function
        :return: value of the activation function, with shape x.shape
        '''
        '''
        #### YOUR CODE HERE ####
        '''
        return x

    def derivative(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of evaluating the derivative of the hyperbolic tangent function with input x
        :param x: input to hyperbolic tangent function
        :return: derivative of the activation function, with shape x.shape
        '''
        '''
        #### YOUR CODE HERE ####
        '''
        return x

class ReLU(Activation):
    '''
    Implements the rectified linear unit activation function
    '''

    def __init__(self):
        super(ReLU, self).__init__()

    def value(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of evaluating the ReLU function with input x
        :param x: input to ReLU function
        :return: value of the activation function, with shape x.shape
        '''
        '''
        #### YOUR CODE HERE ####
        '''
        return x

    def derivative(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of evaluating the derivative of the ReLU function with input x
        Set the derivative to 0 at x=0.
        :param x: input to ReLU function
        :return: derivative of the activation function, with shape x.shape
        '''
        '''
        #### YOUR CODE HERE ####
        '''
        return x

class LeakyReLU(Activation):
    '''
    Implements the leaky rectified linear unit activation function
    :attr k: Parameter of leaky ReLU function corresponding to its slope in the negative domain
    '''

    def __init__(self, k=0.1):
        '''
        :param k: Parameter of leaky ReLU function corresponding to its slope in the negative domain
        '''
        self.k = k
        super(LeakyReLU, self).__init__()

    def value(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of evaluating the Leaky ReLU function with input x
        :param x: input to Leaky ReLU function
        :return: value of the activation function, with shape x.shape
        '''
        '''
        #### YOUR CODE HERE ####
        '''
        return x

    def derivative(self, x: np.ndarray) -> np.ndarray:
        '''
        Returns the result of evaluating the derivative of the leaky ReLU function with input x
        Set the derivative to k at x=0.
        :param x: input to leaky ReLU function
        :return: derivative of the activation function, with shape x.shape
        '''
        '''
        #### YOUR CODE HERE ####
        '''
        return x

##################################################################################################################
# LOSS FUNCTIONS
##################################################################################################################

class Loss(ABC):
    '''
    Abstract class for a loss function
    '''

    @abstractmethod
    def value(self, y_hat: np.ndarray, y: np.ndarray) -> float:
        '''
        Computes the value of the loss function for n provided predictions and targets, averaged across n examples
        :param y_hat: Neural network predictions, with shape (n, 1)
        :param y: Targets, with shape (n, 1)
        :return loss: The value of the loss function
        '''
        return 0

    @abstractmethod
    def derivative(self, y_hat: np.ndarray, y: np.ndarray) -> np.ndarray:
        '''
        Computes the derivative of the loss function with respect to the predictions, averaged across n examples
        :param y_hat: Neural network predictions, with shape (n, 1)
        :param y: Targets, with shape (n, 1)
        :return dLdy_hat: The derivative of the loss function with respect to each prediction, with shape (n, 1)
        '''
        return y_hat

class CrossEntropy(Loss):
    '''
    Implements the binary cross entropy loss function
    '''

    def value(self, y_hat: np.ndarray, y: np.ndarray) -> float:
        '''
        Computes the binary cross entropy loss function for n predictions and targets. Assumes there is only 1 node
        in the output layer. The returned value should be the average loss across the n examples.
        :param y_hat: Neural network predictions, with shape (n, 1)
        :param y: Targets, with shape (n, 1)
        :return loss: The value of the cross entropy loss function averaged across all n examples
        '''
        '''
        #### YOUR CODE HERE ####
        '''
        return y_hat

    def derivative(self, y_hat: np.ndarray, y: np.ndarray) -> np.ndarray:
        '''
        Computes the derivative of the binary cross entropy loss function with respect to the predictions. Assumes there
        is only 1 node in the output layer. Returns the partial derivative with respect to each of the n predictions.
        :param y_hat: Neural network predictions, with shape (n, 1)
        :param y: Targets, with shape (n, 1)
        :return dLdy_hat: The derivative of the loss function with respect to each prediction, with shape (n, 1)
        '''
        '''
        #### YOUR CODE HERE ####
        '''
        return y_hat


class MeanSquaredError(Loss):
    '''
    Implements the mean squared error loss function
    '''

    def value(self, y_hat: np.ndarray, y: np.ndarray) -> float:
        '''
        Computes the mean squared error loss function. Assumes there is only 1 node in the output layer.
        The returned value should be the average loss across the n examples.
        :param y_hat: Neural network predictions, with shape (n, 1)
        :param y: Targets, with shape (n, 1)
        :return loss: The value of the mean squared error loss function
        '''
        '''
        #### YOUR CODE HERE ####
        '''
        return y_hat

    def derivative(self, y_hat: np.ndarray, y: np.ndarray) -> np.ndarray:
        '''
        Computes the derivative of the mean squared error loss function with respect to the predictions. Assumes there
        is only 1 node in the output layer. Returns the partial derivative with respect to each of the n predictions.
        :param y_hat: Neural network predictions, with shape (n, 1)
        :param y: Targets, with shape (n, 1)
        :return dLdy_hat: The derivative of the loss function with respect to each prediction, with shape (n, 1)
        '''
        '''
        #### YOUR CODE HERE ####
        '''
        return y_hat


##################################################################################################################
# METRICS
##################################################################################################################

def accuracy(y_hat: np.ndarray, y: np.ndarray, classification_threshold=0.5) -> float:
    '''
    Computes the accuracy of predictions, given the targets. Assumes binary classification (i.e. targets are either 0
    or 1). The predicted class of an example is 1 if the predicted probability is greater than or equal to the
    classification threshold, and 0 otherwise.
    :param y_hat: Neural network predictions, with shape (n, 1). Note that these are probabilities.
    :param y: Targets, with shape (n, 1)
    :param classification_threshold: Classification threshold for binary classification
    :return acc: accuracy
    '''
    '''
    #### YOUR CODE HERE ####
    '''
    return 0.

def mean_absolute_error(y_hat: np.ndarray, y: np.ndarray) -> float:
    '''
    Computes the mean absolute error between the predictions and the targets. This metric is useful for regression
    problems.
    :param y_hat: Neural network predictions, with shape (n, 1). These should be real numbers.
    :param y: Targets, with shape (n, 1). These should be real numbers.
    :return mae: mean absolute error
    '''
    '''
    #### YOUR CODE HERE ####
    '''
    return 0.