import os
import time
import random

# cd c:\Users\anton\Coding\python playground>
# python sudokusolver.py
def print_progress_graph(puzzle):
    empty = sum(row.count('0') for row in puzzle)
    filled = 81 - empty

    bar_width = 30
    filled_width = int((filled / 81) * bar_width)
    empty_width = bar_width - filled_width

    bar = 'X' * filled_width + '-' * empty_width
    percent = (filled / 81) * 100
    return f"[{bar}] {percent:.1f}%"


def print_sudoku_with_graph(puzzle):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    elapsed_time = time.time() - start_time
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(puzzle[i][j].replace("0", " "), end=" ")
        print()

    print("\nSEED:         " + seed)
    print("ITERATION:    " + str(iteration))
    print("ELAPSED TIME: " + str(round(elapsed_time, 2)) + " seconds")
    print("\n" + print_progress_graph(puzzle))

def print_sudoku(puzzle):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    elapsed_time = time.time() - start_time
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(puzzle[i][j].replace("0", " "), end=" ")
        print()

    print("SEED:         " + seed)
    print("ITERATION:    " + str(iteration))
    print("ELAPSED TIME: " + str(round(elapsed_time, 2)) + " seconds")

def is_valid(puzzle, row, col, num):
    for i in range(9):
        if puzzle[row][i] == num:
            return False
        if puzzle[i][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if puzzle[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(puzzle):
    global iteration
    iteration += 1
    print_sudoku_with_graph(puzzle)
    empty = find_empty(puzzle)
    if not empty:
        return True
    row, col = empty
    for i in seed:
        if is_valid(puzzle, row, col, str(i)):
            puzzle[row] = puzzle[row][:col] + str(i) + puzzle[row][col+1:]
            if solve_sudoku(puzzle):
                return True
            puzzle[row] = puzzle[row][:col] + "0" + puzzle[row][col+1:]
    return False

def find_empty(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == "0":
                return (i, j)
    return None

def select_file():
    files = [f for f in os.listdir('.') if f.endswith('.txt')]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print("Select a file by entering its number, or 'q' to quit:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")

        choice = input("Enter your choice: ").lower()
        if choice == 'q':
            return None
        try:
            index = int(choice) - 1
            if 0 <= index < len(files):
                return files[index]
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")

def generate_seed():
    return ''.join(random.sample('123456789', 9))

file = open(select_file(), "r")
sudoku = [line.strip() for line in file.readlines()]
file.close()

seed = generate_seed()
start_time = time.time()
iteration = 0

solve_sudoku(sudoku)