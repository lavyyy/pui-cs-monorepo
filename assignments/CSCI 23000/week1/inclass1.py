"""
This prints a square shape!
"""

def printSquare(cols, rows, symbol):
    if cols == 0 | rows == 0:
        return

    print(f"{symbol}" * cols);
    for i in range(rows - 2):
        print(f"{symbol}{' ' * (cols - 2)}{symbol}");
    print(f"{symbol}" * cols);

printSquare(5, 4, '*');
