import tkinter as tk

class Connect:
    def __init__(self) -> None:
        self.dimensions = (10, 10)
        self.board = [0 for _ in range(self.dimensions[0]*self.dimensions[1])]
        self.CONNECT = 4 # how many in a row
        self.Player = True # boolean variable; represents player to move
        self.draw_grid = True # condition responsible for drawing the grid on screen
        
        self.SIDE_LEN = 500 # in pixels
        self.TILE_SIZE = self.SIDE_LEN//self.dimensions # also in pixels
        self.LINE_WID = 1 # width of the lines on the grid in pixels

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
    
    def drawGUI(self):
        self.game_canvas.delete("all")
        if self.draw_grid:
            for line in range(self.SIDE_LEN//self.TILE_SIZE):
                # iterates creating the vertical lines
                self.game_canvas.create_line(line * self.TILE_SIZE, 0, line*self.TILE_SIZE, self.SIDE_LEN, width = self.LINE_WID)
            for line in range(self.SIDE_LEN//self.TILE_SIZE):
                # create the horizontal lines
                self.game_canvas.create_line(0, line * self.TILE_SIZE, self.SIDE_LEN, line*self.TILE_SIZE, width = self.LINE_WID)
        for index, item in enumerate(self.pad_board(self.board)):
            ind_col, ind_row = index // (self.SIDE_LEN//self.TILE_SIZE), index % (self.SIDE_LEN//self.TILE_SIZE)
            if item:
                self.game_canvas.create_rectangle((ind_row) * self.TILE_SIZE, (ind_col) * self.TILE_SIZE, (ind_row + 1) * self.TILE_SIZE, (ind_col + 1) * self.TILE_SIZE, fill = self.PlayerColors(item))

        self.game_canvas.update()
        self.game_canvas.pack()

    def PlayerColors(player):
        pass

connect = Connect()
