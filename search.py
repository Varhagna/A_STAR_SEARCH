from ast import Index
import copy


def main():
    p_mode = input("Welcome to my 8-Puzzle Solver! Would you like to solve your own puzzle? (Y / N) ")
    start = gen_puzzle(p_mode)
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    algorithm = select_algorithm(goal)
    search(start, goal, algorithm)


def search(start, goal, algorithm):
    nodes = [(start, 0)]
    num_nodes_expanded = 0
    depth = 1
    max_nodes_in_queue = 1
    while len(nodes) > 0:
        curr = nodes.pop(0)
        f_n = algorithm(curr)
        print("Expanding state with lowest f(n) = %s, g(n) = %s, h(n) = %s \n" % (f_n, curr[1], f_n - curr[1]))
        display_puzzle(curr[0])
        if curr[0] == goal:
            print("Goal State found!")
            return nodes
        else:
            num_nodes_expanded += 1
            depth += 1
            for i in range(0, 4):
                ## Find all possible child states 0 = Move Blank Up, 1 = Move Blank Down, 2 = Move Blank Left, 3 = Move Blank Right
                child_node = get_child(curr[0], i)
                ## Append to queue, ensuring that the g(n) is updated for each node given the previous node.
                if child_node != None:
                    nodes.append((child_node, curr[1] + 1))
            ## Sort Queue based on our Heuristic
            nodes = sorted(nodes, key=algorithm)
            if max_nodes_in_queue <= len(nodes):
                max_nodes_in_queue = len(nodes)


def get_child(state, dir):
    for i in range(0, len(state)):
        for j in range(0, len(state)):
            if state[i][j] == 0:
                child = copy.deepcopy(state)
                if dir == 0:  ## Move Blank Up
                    try:
                        temp_val = child[i - 1][j]
                        child[i - 1][j] = child[i][j]
                        child[i][j] = temp_val
                        return child
                    except IndexError:
                        return None
                elif dir == 1:  ## Move Blank Down
                    try:
                        temp_val = child[i + 1][j]
                        child[i + 1][j] = child[i][j]
                        child[i][j] = temp_val
                        return child
                    except IndexError:
                        return None
                elif dir == 2:  ## Move Blank Left
                    try:
                        temp_val = child[i][j - 1]
                        child[i][j - 1] = child[i][j]
                        child[i][j] = temp_val
                        return child
                    except IndexError:
                        return None
                elif dir == 3:
                    try:
                        temp_val = child[i][j + 1]
                        child[i][j + 1] = child[i][j]
                        child[i][j] = temp_val
                        return child
                    except IndexError:
                        return None
                else:
                    return None


def gen_puzzle(p_mode="N"):
    puzzle = []
    if p_mode == "Y":
        puzzle = [["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]]

        print("Please only enter numbers from 0-8, do not reuse numbers.")

        for i in range(0, 9):
            puzzle[int(i / 3)][i % 3] = int(input("%s\n%s\n%s\nNumber? " % (puzzle[0], puzzle[1], puzzle[2])))
    else:
        p_difficulty = int(input("Please enter your desired default puzzle difficulty level! \n 0 - Trivial \n 1 - Easy \n 2 - Medium \n 3 - Hard \n 4 - Impossible \n"))

        if p_difficulty == 0:
            puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        elif p_difficulty == 1:
            puzzle = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
        elif p_difficulty == 2:
            puzzle = [[1, 2, 3], [5, 0, 6], [4, 7, 8]]
        elif p_difficulty == 3:
            puzzle = [[5, 1, 2], [6, 7, 3], [4, 0, 8]]
        else:
            puzzle = [[5, 0, 2], [6, 1, 7], [4, 8, 3]]

    display_puzzle(puzzle)
    return puzzle


## Helper function for selecting algorithm
def select_algorithm(goal):
    algo = int(input("Select a search heuristic: 0 - Uniform Cost \n 1 - Misplaced Tile \n 2 - Manhattan Distance\n"))
    if algo == 0:
        return lambda i: i[1]
    elif algo == 1:
        return lambda i: i[1] + get_misplaced_tiles(i[0], goal)
    elif algo == 2:
        return lambda i: i[1] + get_manhattan(i[0], goal)


## Parameters: two matrices representing the current state and the goal state of the 8-puzzle matrix
## Output: The sum of Manhattan distances of all misplaced tiles
def get_manhattan(state, goal):
    distance = 0

    ## We know the goal state is when we have 1 - 3 in the first row, 4 - 6 in the second row, and 7-8, 0 in the third row.
    # That means the following correspondance to indices can be made
    # 1 = (0, 0), 2 = (0, 1), 3 = (0, 2), 4 = (1, 0), 5 = (1, 1), 6 = (1, 2), 7 = (2, 0), 8 = (2, 1), 0 = (2, 2)
    # The Manhattan Distance between any two indices is defined as |i_2 - i_1| + |j_2 - j_1|
    # We want to find the sum of the manhattan distances of all misplaced tiles.

    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] != goal[i][j]:
                goal_indices = index_mapper(state[i][j])
                distance += abs(i - goal_indices[0]) + abs(j - goal_indices[1])
    return distance


## Parameters: an integer
## Output: The indices of the position of the integer in the goal state of the 8-puzzle matrix.
def index_mapper(value):
    ## shift values over so 1 -> 0, 2 -> 1, ... 0 -> 8
    value = (value - 1) % 9
    ## use earlier algorithm to convert values of range(0, 9) to appropriate index in 2d list
    ## ex 8 / 3 = 2, 8 % 3 = 2 -> (2, 2)
    return (int(value / 3), value % 3)


## Parameters: two matrices representing the current state and the goal state of the 8-puzzle matrix
## Output: The number of tiles such that state[i][j] != goal[i][j]
def get_misplaced_tiles(state, goal):
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] != goal[i][j]:
                count += 1
    return count


def display_puzzle(puzzle):
    print("%s\n%s\n%s" % (puzzle[0], puzzle[1], puzzle[2]))


main()
