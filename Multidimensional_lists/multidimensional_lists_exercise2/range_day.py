def is_in_range(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def get_direction(command, row, col, step):
    if command == "up":
        return row - step, col
    if command == "down":
        return row + step, col
    if command == "left":
        return row, col - step
    return row, col + step

shooted_rows, shooted_cols=0,0
total_targets,kills = 0,0
size = 5
matrix = []
hitted_target = []
player_rows, player_cols = 0, 0

for _ in range(size):
    matrix.append([el for el in input().split()])

for rows in range(size):
    for cols in range(size):
        if matrix[rows][cols] == "x":
            total_targets += 1
        if matrix[rows][cols] == "A":

            player_rows, player_cols = rows, cols

n = int(input())

for _ in range(n):
    commands = input().split()
    task = commands[0]
    direction = commands[1]
    if task == "move":
        step = int(commands[2])

        next_player_row, next_player_col = get_direction(direction, player_rows, player_cols, step)

        if not is_in_range(next_player_row, next_player_col, size):
            continue

        if matrix[next_player_row][next_player_col] != ".":
            continue

        matrix[player_rows][player_cols] = "."
        matrix[next_player_row][next_player_col] = "A"
        player_rows, player_cols=next_player_row, next_player_col

    else:
        step = 1
        shooted_rows, shooted_cols = get_direction(direction, player_rows, player_cols, 1)
        while True:
            if not is_in_range(shooted_rows, shooted_cols, size):
                break

            if matrix[shooted_rows][shooted_cols] == "x":
                hitted_target.append([shooted_rows,shooted_cols])
                matrix[shooted_rows][shooted_cols] = "."
                kills += 1

                break
            shooted_rows, shooted_cols = get_direction(direction, shooted_rows, shooted_cols, 1)
        if len(hitted_target)==total_targets:
            break


if len(hitted_target) == total_targets:
    print(f"Training completed! All {kills} targets hit.")
else:
    print(f"Training not completed! {total_targets-(len(hitted_target))} targets left.")
if hitted_target:
    [print(el) for el in hitted_target]
