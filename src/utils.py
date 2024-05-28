import os

def clear_terminal():
    if os.name == 'posix':
       os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def print_grid(grid):
    num_cols = len(grid[0])
    header = "   " + "".join(str(col).rjust(2) for col in range(num_cols))
    print(header)
    print("  +" + "--" * num_cols + "-+")
    
    for row_idx, row in enumerate(grid):
        row_str = " ".join(row)
        print(f"{row_idx:2}| {row_str} |")
    
    print("  +" + "--" * num_cols + "-+")