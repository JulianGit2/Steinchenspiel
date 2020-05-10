# First draft

row_1 = [2] * 4 + [0] * 4
row_2 = [0] * 4 + [2] * 4
row_3 = [2] * 4 + [0] * 4
row_4 = [2] * 8
outcome = {"row": 1, "state": "IB", "rem": 0}


def show_board():
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)


def move_stone(row, col, start=True, plus=0, reverse=False):
    # Reverse the list (if row 2 or row 4)
    if reverse:
        row.reverse()
    # Find how many stones are in the selected cell
    stones = row[col - 1]
    # Remove all stones from first cell if first turn
    if start:
        row[col - 1] = 0
    for stone in range(1, stones + 1):
        # Check if cell after the current cell is at the end of the row
        if col - 1 + stone > 7:
            # Return the amount of stones still remaining
            if reverse:
                row.reverse()
            return{"row": row,
                   "state": "OOB",
                   "rem": stones + 1 - stone}
        else:
            # Increase next cell by 1
            row[col - 1 + stone] += 1

    # Return the row as well as the amount of stones still remaining
    if reverse:
        row.reverse()
    return{"row": row,
           "state": "IB",
           "rem": row[col - 1 + stones]}


def sim_start(row, col):
    outcome = move_stone(row, col,
                         start=True,
                         plus=0,
                         reverse=False)
    while outcome["rem"] > 0:
        if outcome["state"] == "OOB":
        outcome = move_stone(row, col + outcome["rem"],
                             start=False,
                             plus=0,
                             reverse=False)
        show_board()

sim_start(row_1, 1)




