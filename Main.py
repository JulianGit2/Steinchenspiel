# First draft

row_1 = [2] * 8
row_2 = [0] * 4 + [2] * 4
row_3 = [2] * 4 + [0] * 4
row_4 = [2] * 8


def show_board():
    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)


def move_stone(row, col, plus):
    if row == 1:
        stones = row_1[col - 1] + plus
        if stones < 2:
            print("Finish")
        row_1[col - 1] = 0
        for stone in range(1, stones + 1):
            # If at the end of the row
            if col - 1 + stone > 7:
                return {"row": 2,
                        "column": 8,
                        "stone": stone - 1,
                        "next": True}
            # If not at the end of the row
            else:
                row_1[col - 1 + stone] += 1
                if stone == stones:
                    return {"row": 1,
                            "column": col + stones,
                            "stone": 0,
                            "next": True}

    if row == 2:
        stones = row_2[col - 1] + plus
        if stones < 2:
            print("Finish")
        row_2[col - 1] = 0
        for stone in range(1, stones + 1):
            # If at the end of the row
            if col - 1 - stone < 1:
                row_2[col - 1 - stone] += 1
                return {"row": 1,
                        "column": 1 + stone,
                        "stone": stone,
                        "next": True}
            # If not at the end of the row
            else:
                row_2[col - 1 - stone] += 1
                if stone == stones:
                    return {"row": 2,
                            "column": col - stones,
                            "stone": row_1[col - stones],
                            "next": True}

    if row == 3:
        row_3[col - 1]
    if row == 4:
        row_3[col - 1]






print("Start")
show_board()
print("First Run")
outcome = move_stone(2, 8, 0)
print(outcome)
show_board()
print("Second Run")
print(outcome)
outcome = move_stone(outcome["row"], outcome["column"], outcome["stone"])
show_board()
print("Third Run")
print(outcome)
outcome = move_stone(outcome["row"], outcome["column"], outcome["stone"])
show_board()
# show_board()
# print(outcome)
# outcome = move_stone(outcome["row"], outcome["column"], outcome["stone"])
# show_board()
# print(outcome)

# for i in range(1):
#     print(outcome)
#     outcome = move_stone(outcome["row"], outcome["column"], outcome["stone"])
#     print(i)
#     show_board()

# for i in range(2):
#     if outcome["next"] == False:
#         print("skip")
#         print(outcome)
#         move_stone(outcome["row"], outcome["column"], outcome["stone"])
#     else:
#         move_stone(outcome["row"], outcome["column"], outcome["stone"])

