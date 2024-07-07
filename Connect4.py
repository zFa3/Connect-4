import tkinter as tk

class TextColors:
    def __init__(self) -> None:
        self.RED = '\033[91m'
        self.ORANGE = '\033[93m'
        self.GREEN = '\033[92m'
        self.BLUE = '\033[94m'
        self.CYAN = '\033[96m'

        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

        self.COLORS = ['\033[92m', '\033[94m', '\033[91m', '\033[94m', '\033[96m', '\033[1m', '\033[4m']

    def PrintColors(self, colorIndex: int, *args):
        print(f"{self.COLORS[colorIndex]}", *args, sep="", end="")

class Connect:
    def __init__(self) -> None:
        self.dimensions = (5, 10)
        self.board = [0 for _ in range(self.dimensions[0]*self.dimensions[1])]
        self.dimensions

        self.root = tk.Tk()
        self.root.geometry(f"{self.SIDE_LEN}x{self.SIDE_LEN}")
        self.game_canvas = tk.Canvas(self.root)
        self.game_canvas.config(background="#ACACAC")
        self.game_canvas.config(width=self.SIDE_LEN, height=self.SIDE_LEN)
        self.root.title("Connect 4")

    def place_piece(self, column, player):
        column%=self.dimensions[1]
        for row in range(1, self.dimensions[0]+1):
            if self.board[(row-1)*self.dimensions[1] + column]!=0:
                if not row: raise SystemError("invalid move")
                else: self.board[(row-1)*self.dimensions[1] + column]=player;break
            if row==self.dimensions[0]:
                self.board[(row-1)*self.dimensions[1] + column]=player
        return self.board
    

connect = Connect()
printer = TextColors()