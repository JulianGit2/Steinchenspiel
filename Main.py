# Bot for playing HUS

# Creates the board
row_1 = [2] * 8
row_2 = [2] * 4 + [0] * 4
row_3 = [0] * 4 + [2] * 4
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
    if start:
        stones = row[col - 1]
    else:
        stones = plus
    # Remove all stones from first cell if first turn
    if start:
        row[col - 1] = 0
    for stone in range(1, stones + 1):
        # Check if cell after the current cell is at the end of the row
        if col - 1 + stone > 7:
            # Return the amount of stones still remaining
            rem = stones + 1 - stone
            if reverse:
                row.reverse()
            return{"row": row,
                   "pos": 0,
                   "rem": rem}
        else:
            # Increase next cell by 1
            row[col - 1 + stone] += 1

    # Return the row as well as the amount of stones still remaining
    rem = row[col - 1 + stones]
    if reverse:
        row.reverse()
    return{"row": row,
           "pos": col + stones,
           "rem": rem}


def is_reverse(row):
    if id(row) == id(row_1):
        return False
    elif id(row) == id(row_2):
        return True
    elif id(row) == id(row_3):
        return False
    elif id(row) == id(row_4):
        return True
    else:
        print("No known row specified")


def switch_row(row):
    if id(row) == id(row_1):
        return{"row": row_2, "reverse": True}
    elif id(row) == id(row_2):
        return{"row": row_1, "reverse": False}
    elif id(row) == id(row_3):
        return{"row": row_4, "reverse": True}
    elif id(row) == id(row_4):
        return{"row": row_3, "reverse": False}
    else:
        print("No known row specified")


def start_sim(row, col):
    reverse = is_reverse(row)
    # if reverse, switch column
    if reverse:
        col = 9 - col
    outcome = move_stone(row, col,
                         start=True,
                         plus=0,
                         reverse=reverse)
    # While any stones are remaining or jumping to next row
    while outcome["rem"] > 1 or outcome["pos"] == 0:
        # if next row
        if outcome["pos"] == 0:
            reverse = switch_row(row)["reverse"]
            remaining = outcome["rem"]
            pos = outcome["pos"]
            row = switch_row(row)["row"]
            outcome = move_stone(row, pos,
                                 start=False,
                                 plus=remaining,
                                 reverse=reverse)
        # if same row
        else:
            reverse = is_reverse(row)
            remaining = outcome["rem"]
            pos = outcome["pos"]
            outcome = move_stone(row, pos,
                                 start=True,
                                 plus=0,
                                 reverse=reverse)

    print("---")
    print(sum(row_1) + sum(row_2))
    print(outcome["rem"])
    print(outcome["pos"])
    show_board()

start_sim(row_3, 5)




