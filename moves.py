table = [['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']]
table.insert(len(table), ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'])
for i in range(2, 6):
    table.insert(len(table), [0, 0, 0, 0, 0, 0, 0, 0])
table.insert(len(table), ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'])
table.insert(len(table), ['r', 'h', 'b', 'k', 'q', 'b', 'h', 'r'])
position_king_opponent = [0, 4]
position_king_player = [7, 3]
win = -1


def game_setup(player, opponent):
    if player == 'B':
        temp = table[0][4]
        table[0][4] = table[0][3]
        table[0][3] = temp
        temp = table[7][4]
        table[7][4] = table[7][3]
        table[7][3] = temp
        position_king_player = [0, 3]
        position_king_opponent = [7, 4]
    # for j in range(8):
    # table[0][j] += color_opponent
    # table[1][j] += color_opponent
    # table[6][j] += color_player
    # table[7][j] += color_player
    print_table()


def same_color(x, y):
    if type(table[x][y]) != type(0):
        if table[x][y][len(table[x][y]) - 1] == color_player:
            return True
    return False


def enemy_attacked(x, y):
    if type(table[x][y]) != type(0):
        if table[x][y][len(table[x][y]) - 1] == color_opponent:
            return True
    return False


def is_in_border_or_outside(x, y):
    if x < 1 or x > 6 or y < 1 or y > 6:
        return True
    return False


def is_in_border(x, y):
    if x == 0 or x == 7 or y == 0 or y == 7:
        return True
    return False


def is_outside(x, y):
    if x < 0 or x > 7 or y < 0 or y > 7:
        return True
    return False


def move(x1, y1, x2, y2):
    if (same_color(x2, y2) or available_cells(table[x1][y1], x1, y1, x2, y2) == False):
        print("NOT A LEGAL MOVE")
        print_table()
        return
    table[x2][y2] = table[x1][y1]
    table[x1][y1] = 0
    if position_king_opponent[0] == x1 and position_king_opponent[1] == y1:
        position_king_opponent[0] = x2
        position_king_opponent[1] = y2
    if position_king_player[0] == x1 and position_king_player[1] == y1:
        position_king_player[0] = x2
        position_king_player[1] = y2
    if position_king_opponent[0] == x2 and position_king_opponent[1] == y2:
        print("Ganaste")
        win = 1
    if position_king_player[0] == x2 and position_king_player[1] == y2:
        print("Perdiste")
        win = 0
    print_table()


def print_table():
    for j in range(8):
        for k in range(8):
            print(table[j][k], sep=",", end="")
        print("")


def find_key(piece):
    pieces = ['r', 'h', 'b', 'q', 'k', 'p']
    piece_num = 0
    while (piece[0] != pieces[piece_num]):
        piece_num = piece_num + 1
    return piece_num


def available_cells(piece, x, y, x_destination, y_destination):
    # Rook = r, Knight = h, Bishop = b, Queen = q, King = k, Pawn = p
    piece_num = find_key(piece)
    if piece_num == 0:
        available_cells = available_cells_rook(x, y)
    if piece_num == 1:
        available_cells = available_cells_knight(x, y)
    if piece_num == 2:
        available_cells = available_cells_bishop(x, y)
    if piece_num == 3:
        available_cells = available_cells_queen(x, y)
    if piece_num == 4:
        available_cells = available_cells_king(x, y)
    if piece_num == 5:
        available_cells = available_cells_pawn(x, y)
    available = False
    for j in range(len(available_cells)):
        if available_cells[j][0] == x_destination and available_cells[j][1] == y_destination:
            available = True
    return available


def available_cells_rook(x, y):
    available_cells_rook = []
    # ahead
    y_temp = y + 1
    intact = True
    if y_temp > -1 and y_temp < 8:
        while ((not same_color(x, y_temp)) and intact and (not is_in_border_or_outside(x, y_temp))):
            available_cells_rook.insert(len(available_cells_rook), [x, y_temp])
            if enemy_attacked(x, y_temp):
                intact = False
            y_temp = y_temp + 1
        if (not same_color(x, y_temp)) and intact and is_in_border(x, y_temp):
            available_cells_rook.insert(len(available_cells_rook), [x, y_temp])

    # behind
    y_temp = y - 1
    intact = True
    if y_temp > -1 and y_temp < 8:
        while ((not same_color(x, y_temp)) and intact and (not is_in_border_or_outside(x, y_temp))):
            available_cells_rook.insert(len(available_cells_rook), [x, y_temp])
            if enemy_attacked(x, y_temp):
                intact = False
            y_temp = y_temp - 1
        if (not same_color(x, y_temp)) and intact and is_in_border(x, y_temp):
            available_cells_rook.insert(len(available_cells_rook), [x, y_temp])

    # left
    x_temp = x - 1
    intact = True
    if x_temp > -1 and x_temp < 8:
        while ((not same_color(x_temp, y)) and intact and (not is_in_border_or_outside(x_temp, y))):
            available_cells_rook.insert(len(available_cells_rook), [x_temp, y])
            if enemy_attacked(x_temp, y):
                intact = False
            x_temp = x_temp - 1
        if (not same_color(x_temp, y)) and intact and is_in_border(x_temp, y):
            available_cells_rook.insert(len(available_cells_rook), [x_temp, y])

    # right
    x_temp = x + 1
    intact = True
    if x_temp > -1 and x_temp < 8:
        while ((not same_color(x_temp, y)) and intact and (not is_in_border_or_outside(x_temp, y))):
            available_cells_rook.insert(len(available_cells_rook), [x_temp, y])
            if enemy_attacked(x_temp, y):
                intact = False
            x_temp = x_temp + 1
        if (not same_color(x_temp, y)) and intact and is_in_border(x_temp, y):
            available_cells_rook.insert(len(available_cells_rook), [x_temp, y])
    return available_cells_rook


def available_cells_knight(x, y):
    available_cells_knight = []
    temp_cells = []
    if x - 1 > -1 and x - 1 < 8:
        if y - 2 > -1 and y - 2 < 8:
            temp_cells.insert(len(temp_cells), [x - 1, y - 2])
        if y + 2 > -1 and y + 2 < 8:
            temp_cells.insert(len(temp_cells), [x - 1, y + 2])
    if x + 1 > -1 and x + 1 < 8:
        if y - 2 > -1 and y - 2 < 8:
            temp_cells.insert(len(temp_cells), [x + 1, y - 2])
        if y + 2 > -1 and y - 2 < 8:
            temp_cells.insert(len(temp_cells), [x + 1, y + 2])
    if x - 2 > -1 and x - 2 < 8:
        if y - 1 > -1 and y - 1 < 8:
            temp_cells.insert(len(temp_cells), [x - 2, y - 1])
        if y + 1 > -1 and y + 1 < 8:
            temp_cells.insert(len(temp_cells), [x - 2, y + 1])
    if x + 2 > -1 and x + 2 < 8:
        if y - 1 > -1 and y - 1 < 8:
            temp_cells.insert(len(temp_cells), [x + 2, y - 1])
        if y + 1 > -1 and y + 1 < 8:
            temp_cells.insert(len(temp_cells), [x + 2, y + 1])
    for j in range(len(temp_cells)):
        if (not (is_outside(temp_cells[j][0], temp_cells[j][1]))) \
                and not (same_color(temp_cells[j][0], temp_cells[j][1])):
            available_cells_knight.insert(len(available_cells_knight), temp_cells[j])
    return available_cells_knight


def available_cells_bishop(x, y):
    available_cells_bishop = []
    # ahead_left
    x_temp = x - 1
    y_temp = y + 1
    intact = True
    if x_temp > -1 and x_temp < 8 and y_temp > -1 and y_temp < 8:
        while ((not same_color(x_temp, y_temp)) and intact and (not is_in_border_or_outside(x_temp, y_temp))):
            available_cells_bishop.insert(len(available_cells_bishop), [x_temp, y_temp])
            if enemy_attacked(x_temp, y_temp):
                intact = False
            x_temp = x_temp - 1
            y_temp = y_temp + 1
        if (not same_color(x_temp, y_temp)) and intact and is_in_border(x_temp, y_temp):
            available_cells_bishop.insert(len(available_cells_bishop), [x_temp, y_temp])

    # ahead_right
    x_temp = x + 1
    y_temp = y + 1
    intact = True
    if x_temp > -1 and x_temp < 8 and y_temp > -1 and y_temp < 8:
        while ((not same_color(x_temp, y_temp)) and intact and (not is_in_border_or_outside(x_temp, y_temp))):
            available_cells_bishop.insert(len(available_cells_bishop), [x_temp, y_temp])
            if enemy_attacked(x_temp, y_temp):
                intact = False
            x_temp = x_temp + 1
            y_temp = y_temp + 1
        if (not same_color(x_temp, y_temp)) and intact and is_in_border(x_temp, y_temp):
            available_cells_bishop.insert(len(available_cells_bishop), [x_temp, y_temp])

    # behind_left
    x_temp = x - 1
    y_temp = y - 1
    intact = True
    if x_temp > -1 and x_temp < 8 and y_temp > -1 and y_temp < 8:
        while ((not same_color(x_temp, y_temp)) and intact and (not is_in_border_or_outside(x_temp, y_temp))):
            available_cells_bishop.insert(len(available_cells_bishop), [x_temp, y_temp])
            if enemy_attacked(x_temp, y_temp):
                intact = False
            x_temp = x_temp - 1
            y_temp = y_temp - 1
        if (not same_color(x_temp, y_temp)) and intact and is_in_border(x_temp, y_temp):
            available_cells_bishop.insert(len(available_cells_bishop), [x_temp, y_temp])

    # behind_right
    x_temp = x + 1
    y_temp = y - 1
    intact = True
    if x_temp > -1 and x_temp < 8 and y_temp > -1 and y_temp < 8:
        while ((not same_color(x_temp, y_temp)) and intact and (not is_in_border_or_outside(x_temp, y_temp))):
            available_cells_bishop.insert(len(available_cells_bishop), [x_temp, y_temp])
            if enemy_attacked(x_temp, y_temp):
                intact = False
            x_temp = x_temp + 1
            y_temp = y_temp - 1
        if (not same_color(x_temp, y_temp)) and intact and is_in_border(x_temp, y_temp):
            available_cells_bishop.insert(len(available_cells_bishop), [x_temp, y_temp])
    return available_cells_bishop


def available_cells_queen(x, y):
    available_cells_queen = available_cells_knight(x, y)
    available_cells_queen_2 = available_cells_bishop(x, y)
    for i in range(len(available_cells_queen_2)):
        available_cells_queen.insert(len(available_cells_queen), available_cells_queen_2[i])
    return available_cells_queen


def available_cells_king(x, y):
    available_cells_king = []
    temp_cells = []
    if x - 1 > -1 and x - 1 < 8:
        if y - 1 > -1 and y - 1 < 8:
            temp_cells.insert(len(temp_cells), [x - 1, y - 1])
        if y > -1 and y < 8:
            temp_cells.insert(len(temp_cells), [x - 1, y])
        if y + 1 > -1 and y + 1 < 8:
            temp_cells.insert(len(temp_cells), [x - 1, y + 1])
    if x > -1 and x < 8:
        if y - 1 > -1 and y - 1 < 8:
            temp_cells.insert(len(temp_cells), [x, y - 1])
        if y + 1 > -1 and y + 1 < 8:
            temp_cells.insert(len(temp_cells), [x, y + 1])
    if x + 1 > -1 and x + 1 < 8:
        if y - 1 > -1 and y - 1 < 8:
            temp_cells.insert(len(temp_cells), [x + 1, y - 1])
        if y > -1 and y < 8:
            temp_cells.insert(len(temp_cells), [x + 1, y])
        if y + 1 > -1 and y + 1 < 8:
            temp_cells.insert(len(temp_cells), [x + 1, y + 1])
    for j in range(8):
        if not (is_outside(temp_cells[j][0], temp_cells[j][1])) \
                and not (same_color(temp_cells[j][0]), temp_cells[j][1]):
            available_cells_king.insert(len(available_cells_king), temp_cells[j])
    return available_cells_king


def available_cells_pawn(x, y):
    available_cells_pawn = []
    if x - 1 > -1 and x - 1 < 8:
        if y - 1 > -1 and y - 1 < 8:
            if enemy_attacked(x - 1, y - 1):
                available_cells_pawn.insert(len(available_cells_pawn), [x - 1, y - 1])
        if y + 1 > -1 and y + 1 < 8:
            if enemy_attacked(x - 1, y + 1):
                available_cells_pawn.insert(len(available_cells_pawn), [x - 1, y + 1])
        if y > -1 and y < 8:
            if (not enemy_attacked(x - 1, y)) and not (same_color(x - 1, y)):
                available_cells_pawn.insert(len(available_cells_pawn), [x - 1, y])
        if x == 6:
            if x - 2 > -1 and x - 2 < 8:
                if (not same_color(x - 2, y)) and not (enemy_attacked(x - 2, y)):
                    available_cells_pawn.insert(len(available_cells_pawn), [x - 2, y])
    return available_cells_pawn


# white = True
white = bool(input("Are you playing whites?"))
color_player = 'W'
color_opponent = 'B'
if not white:
    color_player = 'B'
    color_opponent = 'W'
game_setup(color_player, color_opponent)
while win == -1:
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))
    move(x1, y1, x2, y2)
