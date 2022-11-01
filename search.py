from logging import warn
import queue


def main():
    p_mode = input("Welcome to my 8-Puzzle Solver! Would you like to solve your own puzzle? (Y / N) ")
    solve_puzzle(p_mode)


def display_puzzle(puzzle):
    print("%s\n%s\n%s" % (puzzle[0], puzzle[1], puzzle[2]))


def solve_puzzle(p_mode="N"):
    if p_mode == "Y":
        puzzle = [["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]]

        print("Please only enter numbers from 0-8, do not reuse numbers.")

        for i in range(0, 9):
            puzzle[int(i / 3)][i % 3] = int(input("%s\n%s\n%s\nNumber? " % (puzzle[0], puzzle[1], puzzle[2])))

        display_puzzle(puzzle)
    else:
        p_difficulty = input("Please enter your desired default puzzle difficulty level! \n 0 - Trivial \n 1 - Easy \n 2 - Normal \n 3 - Hard \n 4 - Difficult \n 5 - Impossible \n")


main()
