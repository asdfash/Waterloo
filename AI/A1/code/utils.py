import os
from math import radians, cos, sin, asin, sqrt
from typing import Set, Callable

import pandas as pd
import numpy as np

class State:
    '''
    Represents a state in the search problem. Each state corresponds to a location and a set of locations yet to visit.
    Contains the following member variables:
    loc_id (int): The ID of the state's location
    remaining_locs (Set[int]): The set of IDs of locations left to visit
    :param locations: A 2D array where locations[i] is [location_id, latitude, longitude]
    :param distances: A 2D array where the value at index [i,j] is the distance between locations i and j. If i and j
                      are not connected, the distance is -1.
    longitude (float): longitude of the state's location
    latitude (float): latitude of the state's location
    '''

    def __init__(self, loc_id: int, locations: np.array, distances: np.array, remaining_locs: Set[int]):
        self.loc_id = loc_id
        self.remaining_locs = remaining_locs
        self.locations = locations
        self.distances = distances
        self.latitude = self.locations[self.loc_id][0]
        self.longitude = self.locations[self.loc_id][1]

    # Custom equality operator for object comparison
    def __eq__(self, other):
        return self.loc_id == other.loc_id and self.remaining_locs == other.remaining_locs

    # Custom less-than operator for object comparison
    def __lt__(self, other):
        if len(self.remaining_locs) < len(other.remaining_locs):
            return True
        elif len(self.remaining_locs) == len(other.remaining_locs):
            return self.loc_id < other.loc_id
        else:
            return False

    # Custom greater-than operator for object comparison
    def __gt__(self, other):
        if len(self.remaining_locs) > len(other.remaining_locs):
            return True
        elif len(self.remaining_locs) == len(other.remaining_locs):
            return self.loc_id > other.loc_id
        else:
            return False

    # Custom string representation for printing
    def __str__(self):
        remaining_locs_str = self.remaining_locs if len(self.remaining_locs) > 0 else "{}"
        return f"{{Location: {self.loc_id}, Remaining: {remaining_locs_str}}}"

    # Custom hash operation for set membership
    def __hash__(self):
        return hash((self.loc_id, tuple(self.remaining_locs)))


class Node:
    '''
    Represents a node in the search tree. Contains the following member variables:
    state (State): The state at the current node
    depth (int): The depth of the node in the search tree
    parent (Node): The node's parent in the search tree. Set to None if this is the root of the search tree.
    cost (float): The cost of the path from the initial state to the current state in the search tree
    h_fn (Callable): The heuristic function that will be used to calculate h. Set to None if using an
                     informed search algorithm.
    f (float): The f-value of the current node (h = cost + f). Set to None if h is None.
    '''

    def __init__(self, state: State, depth: int, cost: float, h_fn: Callable = None, parent = None):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        if h_fn is not None:
            self.h = h_fn(self)     # Calculate the value of the heuristic function for this node
        self.f = -1. if h_fn is None else self.cost + self.h

    # Custom equality operator for object comparison
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.f == other.f and self.state == other.state
        return False

    # Custom less-than operator for object comparison
    def __lt__(self, other):
        if self.f < other.f:
            return True
        elif self.f == other.f:
            return self.state < other.state     # Use state ordering as tie-breaking scheme
        else:
            return False

    # Custom greater-than operator for object comparison
    def __gt__(self, other):
        if self.f > other.f:
            return True
        elif self.f == other.f:
            return self.state > other.state     # Use state ordering as tie-breaking scheme
        else:
            return False


def orthodromic_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    '''
    Computes the orthodromic distance (a.k.a. great circle distance) between two locations on Earth.
    This is the shortest possible distance traversed by anyone going from location 1 to location 2.
    Modified from https://www.geeksforgeeks.org/program-distance-two-points-earth/
    :param lat1: Latitude of location 1
    :param lon1: Longitude of location 1
    :param lat2: Latitude of location 2
    :param lon2: Longitude of location 1
    :return: Orthodromic distance between locations 1 and 2
    '''

    # Convert degrees to radians
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    a = sin((lat2 - lat1) / 2) ** 2 + cos(lat1) * cos(lat2) * sin((lon2 - lon1) / 2) ** 2

    r = 6371.   # Radius of Earth in kilometres
    return 2. * r * asin(sqrt(a))


def load_map_info(location_csv_path: str, distance_csv_path: str) -> (np.array, np.array):
    '''
    Loads the location information for each state and the distances between each location
    :param location_csv_path: A CSV file containing the latitude and longitude of each location
    :param distance_csv_path: A CSV file containing the distances between each destination on the map
    return: 2D array where row i gives the latitude and longitude of location i, 2D array where entry [i,j] gives
            the distance between locations i and j. Locations are not connected by road if the distance is -1.
    '''

    assert os.path.exists(location_csv_path), f"No CSV file found at {location_csv_path}"
    assert os.path.exists(distance_csv_path), f"No CSV file found at {location_csv_path}"

    locations = pd.read_csv(location_csv_path, header=None).to_numpy()[:, 0:2]
    distances = pd.read_csv(distance_csv_path, header=None).to_numpy()
    return locations, distances
