from utils import State, load_map_info
from search import sample_heuristic, custom_heuristic, A_star, BFS

# Load the list of locations, along with the driving distances between locations.
locations, distances = load_map_info("locations.csv", "distances.csv")

init_loc = 0                            # Start and end in Waterloo
destinations = {8, 15}                  # Stops in Hamilton and Toronto
init_state = State(init_loc, locations, distances, destinations)  # Define the initial state

# Breadth-first search
path, cost = BFS(init_state, locations, distances)
path_str = ",\n".join([str(state) for state in path])
print(f"BFS Search: The solution (with cost {cost:.2f}) is:\n{path_str}")

# A* search
h_fn = sample_heuristic
path, cost = A_star(init_state, h_fn, locations, distances)
path_str = ",\n".join([str(state) for state in path])
print(f"A* Search: The solution (with cost {cost:.2f}) is:\n{path_str}")
