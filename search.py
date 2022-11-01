from logging import warn
import queue


def main():
    p_mode = input("Welcome to my 8-Puzzle Solver! Would you like to solve your own puzzle? (Y / N) ")
    gen_puzzle(p_mode)


def gen_puzzle(p_mode="N"):
    puzzle = []
    if p_mode == "Y":
        puzzle = [["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]]

        print("Please only enter numbers from 0-8, do not reuse numbers.")

        for i in range(0, 9):
            puzzle[int(i / 3)][i % 3] = int(input("%s\n%s\n%s\nNumber? " % (puzzle[0], puzzle[1], puzzle[2])))

        display_puzzle(puzzle)
    else:
        p_difficulty = input("Please enter your desired default puzzle difficulty level! \n 0 - Trivial \n 1 - Easy \n 2 - Medium \n 3 - Hard \n 4 - Impossible \n")

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


def solve_puzzle(puzzle):
    input("Select a search heuristic: 0 - Uniform Cost \n 1 - Misplaced Tile \n 2 - Manhattan Distance")


def display_puzzle(puzzle):
    print("%s\n%s\n%s" % (puzzle[0], puzzle[1], puzzle[2]))


main()
