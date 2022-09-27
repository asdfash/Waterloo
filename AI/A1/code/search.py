import math
from typing import List, Set
from heapq import heappush, heappop
from collections import deque

import numpy as np

from utils import State, Node, orthodromic_distance


def is_goal(state: State, init_state: State) -> bool:
    '''
    Returns True if state is a goal state
    :param state: Current state
    :init_state: Initial state
    '''
    return len(state.remaining_locs)
    # raise NotImplementedError


def get_path(node: Node) -> List[State]:
    """
    Returns a list of states containing the nodes on the path, in order from the initial state to the current state
    :param node: The current node in the search tree
    :return: The sequence of states in the path
    """
    raise NotImplementedError


def get_successors(state: State, locations: np.array, distances: np.array) -> Set[State]:
    '''
    :param state: The current state
    :param locations: A 2D array where locations[id] is [latitude, longitude]
    :param distances: A 2D array where the value at index [i,j] is the distance between locations i and j. If i and j
                      are not connected, the distance is -1.
    :return: List of successor states for the current state
    '''
    raise NotImplementedError


def BFS(init_state: State, locations: np.array, distances: np.array) -> (List[State], float):
    """
    Executes the breath-first search algorithm, with multi-path pruning, from the given start state.
    :param init_state: The initial state
    :param locations: A 2D array where locations[i] is [location_id, latitude, longitude]
    :param distances: A 2D array where the value at index [i,j] is the distance between locations i and j. If i and j
                      are not connected, the distance is -1.
    :return: Path to goal state (empty list if no solution exists), total cost of path (-1 if no solution exists)
    """
    raise NotImplementedError


def A_star(init_state: State, h_fn, locations: np.array, distances: np.array) -> (List[State], float):
    """
    Executes the A* search algorithm, with multi-path pruning, from the given start state and heuristic function.
    :param init_state: The initial state
    :param h_fn: The heuristic function. It should take a single state as an argument
    :param locations: A 2D array where locations[i] is [location_id, latitude, longitude]
    :param distances: A 2D array where the value at index [i,j] is the distance between locations i and j. If i and j
                      are not connected, the distance is -1.
    :return: Path to goal state (empty list if no solution exists), total cost of path (-1 if no solution exists)
    """
    raise NotImplementedError


def sample_heuristic(node: Node) -> float:
    '''
    An example of a consistent heuristic.
    The heuristic is the minimum distance between any two locations multiplied by the number of locations yet
    to visit, including the initial location. Evaluates to 0 if at a goal node.
    :param node: The current node in the search tree
    :return: The value of the heuristic function
    '''

    init_state = get_path(node)[0]
    if is_goal(node.state, init_state):
        return 0.

    cur_state = node.state
    remaining_locs = list(cur_state.remaining_locs)

    dists = cur_state.distances.copy()
    dists[dists == -1.] = np.inf
    min_dist = np.min(dists)                # The minimum distance between any 2 destinations
    min_n_trips = len(remaining_locs) + 1   # The minimum number of trips remaining
    return min_dist * min_n_trips


def custom_heuristic(node: Node) -> float:
    '''
    A heuristic of your own design. It should be consistent.
    :param node: The current node in the search tree
    :return: The value of the heuristic function
    '''
    raise NotImplementedError

