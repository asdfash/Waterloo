from typing import Dict, List, Tuple
from factor import Factor

'''
########## READ CAREFULLY #############################################################################################
You should implement all the functions in this file. Do not change the function signatures.
#######################################################################################################################
'''

def restrict(factor: Factor, variable: str, value: int) -> Factor:
    '''
    Restrict a factor by assigning value to variable
    :param factor: a Factor object
    :param variable: the name of the variable to restrict
    :param value: the value to restrict variable to
    :return: a new Factor object resulting from restricting variable. This factor no longer includes variable in its
             var_list.
    '''

    '''
    ##### YOUR CODE HERE #####
    '''
    if factor.has_variable(variable):
        for i in range(factor.n_vars):
            if factor.var_list[i] == variable:
                n = factor.values.copy()
                del n[i]
                l = factor.var_list.copy().remove(variable)
        nf = Factor(l,n)
        return nf
    pass

def multiply(factor_a: Factor, factor_b: Factor) -> Factor:
    '''
    Multiply two tests (factor_a and factor_b) together.
    :param factor_a: a Factor object representing the first factor in the multiplication operation
    :param factor_b: a Factor object representing the second factor in the multiplication operation
    :return: a new Factor object resulting from the multiplication of factor_a and factor_b. Note that the new factor's
             var_list is the union of the var_lists of factor_a and factor_b IN ALPHABETICAL ORDER.
    '''

    '''
    ##### YOUR CODE HERE #####
    '''
    new_factor = Factor()
    return new_factor


def sum_out(factor: Factor, variable: str) -> Factor:
    '''
    Sum out a variable from factor.
    :param factor: a Factor object
    :param variable: the name of the variable in factor that we wish to sum out
    :return: a Factor object resulting from performing the sum out operation on factor. Note that this new factor no
             longer includes variable in its var_list.
    '''

    '''
    ##### YOUR CODE HERE #####
    '''
    if factor.has_variable(variable):
        for i in range(factor.n_vars):
            if factor.var_list[i] == variable:
                n = factor.values.copy()
                del n[i]
                l = factor.var_list.copy().remove(variable)
        nf = Factor(l,n)
        return nf
    pass


def normalize(factor: Factor) -> Factor:
    '''
    Normalize factor such that its values sum to 1.
    :param factor: a Factor object representing the factor to normalize
    :return: a Factor object resulting from performing the normalization operation on factor
    '''

    '''
    ##### YOUR CODE HERE #####
    '''
    ov =factor.values.copy()
    sum = ov.sum
    val = ov/sum

    new_factor = Factor(factor.var_list,val)
    return new_factor


def vea(factor_list: List[Factor], query_variables: List[str], evidence: Dict[str, int], ordered_hidden_variables: List[str], verbose: bool=False) -> Tuple[Factor,int]:
    '''
    Applies the Variable Elimination Algorithm for input tests factor_list, restricting tests according to the
    evidence in evidence_list, and eliminating hidden variables in the order that they appear in
    ordered_list_hidden_variables. The result is the distribution for the query variables. The query variables are, by
    process of elimination, those for which we do not have evidence for and do not appear in the list of hidden
    variables).
    :param factor_list: a list of Factor objects representing every conditional probability distribution in the
                        Bayesian network
    :param query_variables: a list of variable names corresponding to the query variables
    :param evidence_list: a dict mapping evidence variable names to corresponding values
    :param ordered_list_hidden_variables: a list of names of the hidden variables. Variables are to be eliminated in the
                                          order that they appear in this list.
    :param verbose: Whether to print results of intermediate VEA operations (use for debugging, if you like)
    :return: A Factor object representing the result of executing the Variable Elimination Algorithm for the given
             evidence and ordered list of hidden variables, treewidth of the network
    '''

    '''
    ##### YOUR CODE HERE #####
    '''
    final_factor = Factor()
    treewidth = 0
    return final_factor, treewidth