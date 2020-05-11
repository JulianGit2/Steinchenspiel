# Bot for playing HUS

# Creates the board
row_1 = [2] * 8
row_2 = [2] * 4 + [0] * 4
row_3 = [0] * 4 + [2] * 4
row_4 = [2] * 8
outcome = {"row": 1, "state": "IB", "rem": 0}


def reset_board():
    global row_1
    global row_2
    global row_3
    global row_4
    row_1 = [2] * 8
    row_2 = [2] * 4 + [0] * 4
    row_3 = [0] * 4 + [2] * 4
    row_4 = [2] * 8


def show_board():
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)


def move_stone(row, col, start=True, plus=0, reverse=False):
    # Check if you are in row 2 or 3 - making stealing possible
    is_row2 = False
    is_row3 = False
    if id(row) == id(row_2):
        is_row2 = True
    elif id(row) == id(row_3):
        is_row3 = True
    # Reverse the list (if row 2 or row 4)
    if reverse:
        row.reverse()
    # Find how many stones are in the selected cell
    if start:
        if plus == 0:
            stones = row[col - 1]
        else:
            stones = plus
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

    # Check if you can steal opponents stones
    if is_row2:
        row_3_col = 9 - (col + stones)
        if row_3[row_3_col - 1] > 0:
            more_stones = (row[col - 1 + stones]
                           + row_3[row_3_col - 1]
                           + row_4[col - 1 + stones])
            row_3[row_3_col - 1] = 0
            row_4[row_3_col - 1] = 0
            rem = more_stones
        else:
            rem = row[col - 1 + stones]
    elif is_row3:
        if row_2[col + stones - 1] > 0:
            more_stones = (row[col - 1 + stones]
                           + row_2[col + stones - 1]
                           + row_1[col + stones - 1])
            row_2[col + stones - 1] = 0
            row_1[col + stones - 1] = 0
            rem = more_stones
        else:
            rem = row[col - 1 + stones]
    else:
        rem = row[col - 1 + stones]

    # Return the row as well as the amount of stones still remaining
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


def start_turn(row, col):
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
                                 plus=remaining,
                                 reverse=reverse)

    p1_points = sum(row_1) + sum(row_2)
    p2_points = sum(row_3) + sum(row_4)
    return{"p1": p1_points, "p2": p2_points}


def try_turns(player=1):
    state = {"row": [], "col": [], "points": [], "board": []}
    if player == 1:
        for i in range(1, 9):
            reset_board()
            if row_1[i - 1] > 1:
                state["row"].append("1")
                state["col"].append(str(i))
                state["points"].append(start_turn(row_1, i)["p1"])
                show_board()
        for i in range(1, 9):
            reset_board()
            if row_2[i - 1] > 1:
                state["row"].append("2")
                state["col"].append(str(i))
                state["points"].append(start_turn(row_2, i)["p1"])
                show_board()
    if player == 2:
        for i in range(1, 9):
            reset_board()
            if row_3[i - 1] > 1:
                state["row"].append("3")
                state["col"].append(str(i))
                state["points"].append(start_turn(row_3, i)["p2"])
                show_board()
        for i in range(1, 9):
            reset_board()
            if row_4[i - 1] > 1:
                state["row"].append("4")
                state["col"].append(str(i))
                state["points"].append(start_turn(row_4, i)["p2"])
                show_board()

    return state


def play_game("firstplayer"=1, turn):
    # Takes several turns




result = try_turns(1)
print(max(result["points"]))
print(min(result["points]"]))