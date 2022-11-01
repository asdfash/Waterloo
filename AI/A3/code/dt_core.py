# version 1.0
import math
from typing import List,Tuple
from anytree import Node

import dt_global
import dt_provided
from dt_provided import less_than as lt
from dt_provided import less_than_or_equal_to as lte

def get_splits(examples: List, feature: str) -> List[float]:
    """
    Given some examples and a feature, returns a list of potential split point values for the feature.
    
    :param examples: a set of examples
    :type examples: List[List[Any]]
    :param feature: a feature
    :type feature: str
    :return: a list of potential split point values 
    :rtype: List[float]
    """ 

    return None


def choose_feature_split(examples: List, features: List[str]) -> Tuple[str, float, float]:
    """
    Given some examples and some features,
    returns a feature and a split point value with the max expected information gain.

    If there are no valid split points for the remaining features, return None, -1, and -inf.

    Tie breaking rules:
    (1) With multiple split points, choose the one with the smallest value. 
    (2) With multiple features with the same info gain, choose the first feature in the list.

    :param examples: a set of examples
    :type examples: List[List[Any]]    
    :param features: a set of features
    :type features: List[str]
    :return: the best feature, the best split value, the max expected information gain
    :rtype: str, float, float
    """   

    return None, -1, -math.inf


def split_examples(examples: List, feature: str, split: float) -> Tuple[List, List]:
    """
    Given some examples, a feature, and a split point,
    splits examples into two lists and return the two lists of examples.

    The first list of examples have their feature value <= split point.
    The second list of examples have their feature value > split point.

    :param examples: a set of examples
    :type examples: List[List[Any]]
    :param feature: a feature
    :type feature: str
    :param split: the split point
    :type split: float
    :return: two lists of examples split by the feature split
    :rtype: List[List[Any]], List[List[Any]]
    """ 

    return None, None


def split_node(cur_node: Node, examples: List, features: List[str], max_depth=math.inf):
    """
    Given a tree with cur_node as the root, some examples, some features, and the max depth,
    grows a tree to classify the examples using the features by using binary splits.

    If cur_node is at max_depth, makes cur_node a leaf node with majority decision and return.

    This function is recursive.

    :param cur_node: current node
    :type cur_node: Node
    :param examples: a set of examples
    :type examples: List[List[Any]]
    :param features: a set of features
    :type features: List[str]
    :param max_depth: the maximum depth of the tree
    :type max_depth: int
    """ 


def learn_dt(examples: List, features: List[str], max_depth=math.inf) -> Node:
    """
    Given some examples, some features, and the max depth,
    creates the root of a decision tree, and
    calls split_node to grow the tree to classify the examples using the features, and
    returns the root node.

    This function is a wrapper for split_node.

    Tie breaking rule:
    If there is a tie for majority voting, always return the label with the smallest value.

    :param examples: a set of examples
    :type examples: List[List[Any]]
    :param features: a set of features
    :type features: List[str]
    :param max_depth: the max depth of the tree
    :type max_depth: int, default math.inf
    :return: the root of the tree
    :rtype: Node
    """ 

    return None


def predict(cur_node: Node, example, max_depth=math.inf) -> int:
    """
    Given a tree with cur_node as its root, an example, and optionally a max depth,
    returns a prediction for the example based on the tree.

    If max_depth is provided and we haven't reached a leaf node at the max depth, 
    return the majority decision at this node.
    
    This function is recursive.

    Tie breaking rule:
    If there is a tie for majority voting, always return the label with the smallest value.

    :param cur_node: cur_node of a decision tree
    :type cur_node: Node
    :param example: one example
    :type example: List[Any]
    :param max_depth: the max depth
    :type max_depth: int, default math.inf
    :return: the decision for the given example
    :rtype: int
    """ 

    return -1


def get_prediction_accuracy(cur_node: Node, examples: List, max_depth=math.inf) -> float:
    """
    Given a tree with cur_node as the root, some examples, 
    and optionally the max depth,
    returns the accuracy by predicting the examples using the tree.

    The tree may be pruned by max_depth.

    :param cur_node: cur_node of the decision tree
    :type cur_node: Node
    :param examples: the set of examples. 
    :type examples: List[List[Any]]
    :param max_depth: the max depth
    :type max_depth: int, default math.inf
    :return: the prediction accuracy for the examples based on the cur_node
    :rtype: float
    """ 

    return -1


def post_prune(cur_node: Node, min_info_gain: float):
    """
    Given a tree with cur_node as the root, and the minimum information gain,
    post prunes the tree using the minimum information gain criterion.

    This function is recursive.

    Let leaf parents denote all the nodes that only have leaf nodes as its descendants. 
    Go through all the leaf parents.
    If the information gain at a leaf parent is smaller than the pre-defined value,
    convert the leaf parent into a leaf node.
    Repeat until the information gain at every leaf parent is greater than
    or equal to the pre-defined value of the minimum information gain.

    :param cur_node: the current node
    :type cur_node: Node
    :param min_info_gain: the minimum information gain
    :type min_info_gain: float
    """
