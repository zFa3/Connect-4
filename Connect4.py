import tkinter as tk

class Connect:
    def __init__(self) -> None:
        self.dimensions = (5, 10)
        self.board = [0 for _ in range(self.dimensions[0]*self.dimensions[1])]
        self.SIDE_LEN = 750 # in pixels
        self.CONNECT = 4 # how many in a row
        self.Player = True # boolean variable; represents player to move

        # Create a new window in tkinter
        self.root = tk.Tk()
        # Change the geometry of the window
        self.root.geometry(f"{self.SIDE_LEN}x{self.SIDE_LEN}")
        self.game_canvas = tk.Canvas(self.root)
        # background color
        self.game_canvas.config(background="#ACACAC")
        self.game_canvas.config(width=self.SIDE_LEN, height=self.SIDE_LEN)
        # title of the window
        self.root.title("Connect 4")

    def place_piece(self, column, player):
        # some code snippets for placing a piece at designated square
        column%=self.dimensions[1]
        # check for empty column, if so, then find the lowest point that is available
        for row in range(1, self.dimensions[0]+1):
            if self.board[(row-1)*self.dimensions[1] + column]!=0:
                if not row: raise SystemError("invalid move")
                else: self.board[(row-1)*self.dimensions[1] + column]=player;break
            if row == self.dimensions[0]:
                self.board[(row-1)*self.dimensions[1] + column]=player
        return self.board

connect = Connect()
