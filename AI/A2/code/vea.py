from typing import Dict, List, Tuple

import numpy as np
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
        i = factor.var_list.index(variable)
        n = factor.values.copy()
        n = np.take(n,value,i)
        l = factor.var_list.copy()
        l.pop(i)
        nf = Factor(l,n)
        return nf
    return factor



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
    
    #get overall shape
    ashape = list(factor_a.values.shape)
    bshape = list(factor_b.values.shape)
    amissing = list(set(factor_b.var_list).difference(factor_a.var_list))
    if len(amissing)>0:
        amissing.reverse()
    amissingi = [factor_b.var_list.index(i) for i in amissing]
    bmissing = list(set(factor_a.var_list).difference(factor_b.var_list))
    if len(amissing)>0:
        bmissing.reverse()
    bmissingi = [factor_a.var_list.index(i) for i in bmissing]
    newvar = sorted(list(set(factor_b.var_list).union(set(factor_a.var_list))))

    #pad first
    for i in amissingi:
        ashape += [factor_b.values.shape[i]]
    for i in bmissingi:
        bshape += [factor_a.values.shape[i]]


    print(factor_a)
    print(factor_b)

    aval = np.broadcast_to(factor_a.values,ashape)
    bval = np.broadcast_to(factor_b.values,bshape)
    print("before")
    print("aval")
    print(aval)
    print("bval")
    print(bval)
    x = amissing + factor_a.var_list.copy() 
    for i, e in enumerate(x):
        if e != newvar[i]:
            j = newvar.index(e)
            x[i],x[j] = x[j],x[i]
            aval =np.swapaxes(aval,i,j)

    x = bmissing+factor_b.var_list.copy() 
    for i, e in enumerate(x):
        if e != newvar[i]:
            j = newvar.index(e)
            x[i],x[j] = x[j],x[i]
            bval =np.swapaxes(bval,i,j)
    print("after")
    print("aval")
    print(aval)
    print("bval")
    print(bval)
    newval = aval*bval

    nf = Factor(newvar,newval)
    print(nf)
    return nf


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
        copied = factor.values.copy()
        shape = factor.values.shape
        i = factor.var_list.index(variable)
        newvalue = np.sum(copied,i)
        np.squeeze(newvalue)
        newvar = factor.var_list.copy()
        newvar.pop(i)
        newfactor = Factor(newvar,newvalue)
        return newfactor
    return factor


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
    sum = ov.sum()
    
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
    if verbose:
        print("Starting")
        print("Evidence list:", evidence)
        print("Factors:")
    for i in factor_list:
        if verbose:
            print(i)
            print()
    if verbose:
        print("Restricting")

    for i,j in evidence.items():
        factor_list = [restrict(k,i,j) for k in factor_list]
    if verbose:
        print("restriction done")
        print("Factors:")
        for i in factor_list:
                print(i)
        print("hidden variables:",ordered_hidden_variables)
        print("begin elmination")
        
    flscopy1 = factor_list.copy()
    print(flscopy1)
    for i in ordered_hidden_variables:
        if verbose:
            print("eliminate",i)
        working = []
        for j in factor_list:
            if j.has_variable(i):
                working+=[j]
                flscopy1.remove(j)
        print(working)
        while len(working)>1:
            b = working.pop()
            working[0]=multiply(working[0],b)
        if len(working)>0:
            flscopy1 += [sum_out(working[0],i)]


    if verbose:
        print("elmination done")
        print("removing irrelevant values")
    flscopy2 = flscopy1.copy()
    for i in flscopy1:
        if verbose:
            print(i)
            print()
        for j in query_variables:
            if i.has_variable(j):
                break
        else:
            flscopy2.remove(i)
            if verbose:
                print("removed")
    if verbose:
        print("removal done")
        print(flscopy2)
        print("multiply")
    final_factor = flscopy2.pop()
    for i in flscopy2:
        final_factor = multiply(final_factor,i)

    final_factor = normalize(final_factor)

    treewidth = 0
    return final_factor, treewidth