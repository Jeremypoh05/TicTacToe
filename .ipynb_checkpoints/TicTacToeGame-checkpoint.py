class TicTacToe:
    # Initializes the game board and current player.
    def __init__(self):
        # The game board is a dictionary where each key is a position on the board,
        # and each value is ' ' (indicating an empty space), 'X', or 'O'.
        self.board = {
            'top-l': ' ', 'top-c': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-c': ' ', 'mid-r': ' ',
            'bot-l': ' ', 'bot-c': ' ', 'bot-r': ' ',
        }
        # Current player is initially empty and will be set to 'X' or 'O' based on the player's choice.
        self.current_player = ''

    # Prints the game's instructions to the console.
    def print_instructions(self):
        print("Welcome to Tic Tac Toe!")
        print("Players take turns marking a space in a 3x3 grid.")
        print("The first player to get 3 of their marks in a row (up, down, across, or diagonally) wins the game.")
        print("Choose your position based on the following keys:")
        self.print_board_keys()
        print("\nLet's start the game!\n")

    # Prints the keys for each position on the board to help players choose their moves.
    def print_board_keys(self):
        print('top-l | top-c | top-r')
        print('-----+-------+-----')
        print('mid-l | mid-c | mid-r')
        print('-----+-------+-----')
        print('bot-l | bot-c | bot-r\n')

    # Prints the current state of the board, optionally highlighting the winning line if provided.
    def print_board(self, winning_line=None):
        board_to_print = self.board.copy()
        # If a winning line is provided, surround the winning marks with slashes for emphasis.
        if winning_line:
            for position in winning_line:
                board_to_print[position] = f"/{board_to_print[position]}/"
        
        # Helper function to format each cell for consistent width, ensuring tidy alignment.
        def format_cell(cell):
            # Formats each cell to ensure consistent width for alignment.
            # If cell is empty, it adds a space before and after it.
            # If cell contains a mark ('X' or 'O'), it centers the mark within a 3-character width.
            return f" {cell} " if cell == ' ' else f"{cell:^3}"
        
        # Print each row of the board, using the format_cell function for each cell.
        print(f"{format_cell(board_to_print['top-l'])}|{format_cell(board_to_print['top-c'])}|{format_cell(board_to_print['top-r'])}")
        print("---+---+---")
        print(f"{format_cell(board_to_print['mid-l'])}|{format_cell(board_to_print['mid-c'])}|{format_cell(board_to_print['mid-r'])}")
        print("---+---+---")
        print(f"{format_cell(board_to_print['bot-l'])}|{format_cell(board_to_print['bot-c'])}|{format_cell(board_to_print['bot-r'])}\n")

    # Allows the current player to choose their symbol ('X' or 'O').
    def choose_symbol(self):
        choice = input("Choose your symbol:\n 1 for X\n 2 for O\nYour choice: ")
        # Repeatedly prompt for input until a valid choice ('1' or '2') is made.
        while choice not in ['1', '2']:
            print("Please select an appropriate selection/number (1 for X, 2 for O).")
            choice = input("Your choice: ")
        # Set the current player based on the choice.
        self.current_player = 'X' if choice == '1' else 'O'

    # Attempts to make a move at the specified position. Returns True if successful, False otherwise.
    def make_move(self, position):
        # Check if the position is valid and empty before making the move.
        if position in self.board and self.board[position] == ' ':
            # Marks the position with the current player's symbol if it's empty.
            self.board[position] = self.current_player
            return True
        return False

    # Checks if the current board state results in a win for any player. Returns the winning line and description if so.
    def check_win(self):
        win_conditions = [
            # Defines all possible winning conditions.
            (['top-l', 'top-c', 'top-r'], "horizontal top line"),
            (['mid-l', 'mid-c', 'mid-r'], "horizontal middle line"),
            (['bot-l', 'bot-c', 'bot-r'], "horizontal bottom line"),
            (['top-l', 'mid-l', 'bot-l'], "vertical left line"),
            (['top-c', 'mid-c', 'bot-c'], "vertical center line"),
            (['top-r', 'mid-r', 'bot-r'], "vertical right line"),
            (['top-l', 'mid-c', 'bot-r'], "diagonal from top-left to bottom-right"),
            (['top-r', 'mid-c', 'bot-l'], "diagonal from top-right to bottom-left")
        ]
        for condition, description in win_conditions:
            # Check if any winning condition is met.
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                 # If a winning condition is met, returns the condition and its description.
                return condition, description  # Return the winning line and description.
        return None, None  #  Returns None if there's no win yet.

    # Switches the current player from 'X' to 'O', or vice versa.
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    # Checks if all positions on the board are filled, indicating a full board.
    def is_board_full(self):
        return all(self.board[key] != ' ' for key in self.board)