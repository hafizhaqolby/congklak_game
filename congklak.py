# Simple 2-Player Congklak

board = [7] * 7 + [0] + [7] * 7 + [0]

def print_board():
    print("\n--- CONGKLAK BOARD ---")
    print("P2: {}".format(board[14:7:-1]))
    print("    [{}]              [{}]".format(board[15], board[7]))
    print("P1: {}".format(board[0:7]))
    print("-----------------------\n")

def get_player_input(p_num):
    while True:
        prompt = "Player {} - Pick a hole (0-6): ".format(p_num)
        # The variable name has been changed here
        player_input = input(prompt)
        
        is_a_valid_number = True
        if player_input == "":
            is_a_valid_number = False
        else:
            for char in player_input:
                if char not in "0123456789":
                    is_a_valid_number = False
                    break
        
        if not is_a_valid_number:
            print("Invalid input. Please enter a number.")
            continue

        choice = int(player_input)
        if not (0 <= choice <= 6):
            print("Invalid choice. Pick between 0 and 6.")
            continue
        
        hole_idx = choice if p_num == 1 else 8 + choice
        if board[hole_idx] == 0:
            print("That hole is empty. Pick another one.")
            continue
        
        return choice

def move(player, hole):
    idx = hole if player == 1 else 8 + hole
    stones = board[idx]
    board[idx] = 0
    while stones > 0:
        idx = (idx + 1) % 16
        if (player == 1 and idx == 15) or (player == 2 and idx == 7):
            continue
        board[idx] += 1
        stones -= 1

# --- Main Game Loop ---
turn = 1
while sum(board[0:7]) > 0 and sum(board[8:14]) > 0:
    print_board()
    user_choice = get_player_input(turn)
    move(turn, user_choice)
    turn = 3 - turn

# --- Game Over ---
board[7] += sum(board[0:7])
board[15] += sum(board[8:14])
winner_msg = "It's a draw!"
if board[7] > board[15]:
    winner_msg = "Player 1 wins!"
elif board[15] > board[7]:
    winner_msg = "Player 2 wins!"

print("\n🏁 Game Over!")
print_board()
print(winner_msg)
print("Final Score -> P1: {} | P2: {}".format(board[7],board[15]))
