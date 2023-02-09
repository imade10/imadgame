class TicTacToe:
    def __init__(self):
        self.board = [" " for x in range(9)]
        self.player = "X"

    def display_board(self):
        row1 = "| {} | {} | {} |".format(self.board[0], self.board[1], self.board[2])
        row2 = "| {} | {} | {} |".format(self.board[3], self.board[4], self.board[5])
        row3 = "| {} | {} | {} |".format(self.board[6], self.board[7], self.board[8])

        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def play(self):
        while True:
            self.display_board()
            move = int(input("{}'s turn. Move to which place? (1-9): ".format(self.player)))
            if self.board[move-1] == " ":
                self.board[move-1] = self.player
                if self.player == "X":
                    self.player = "O"
                else:
                    self.player = "X"
            else:
                print("This place is already filled. Try another place.")
                continue
            if self.check_win():
                self.display_board()
                print("Player {} wins! Congrats!".format(self.player))
                break
            if not any(" " in row for row in self.board):
                self.display_board()
                print("It's a draw! No one wins.")
                break

    def check_win(self):
        for combination in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != " ":
                return True
        return False

game = TicTacToe()
game.play()
