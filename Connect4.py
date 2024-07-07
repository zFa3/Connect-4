import tkinter as tk
import time

class Connect:
    def __init__(self) -> None:
        self.dimensions = (10, 10)
        self.board = [0 for i in range(self.dimensions[0]*self.dimensions[1])]
        self.CONNECT = 4 # how many in a row
        self.Player = 1 # represents player to move
        self.draw_grid = True # condition responsible for drawing the grid on screen
        
        self.SIDE_LEN = 500 # in pixels
        self.TILE_SIZE = self.SIDE_LEN//self.dimensions[0] # also in pixels
        self.LINE_WID = 1 # width of the lines on the grid in pixels

        self.dirs = [
                    # define all the directions that can cause a win
                    # left, right, up, down, diagonals
                     -1, 1,
                     -self.dimensions[0], self.dimensions[0],
                     -self.dimensions[0]-1, self.dimensions[0]-1,
                     -self.dimensions[0]+1, self.dimensions[0]+1
                    ]

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

        # bind the click to call a func
        self.root.bind("<Button-1>", self.click)

    def click(self, event):
        col = event.x//(self.SIDE_LEN//self.dimensions[0])
        row = event.y//(self.SIDE_LEN//self.dimensions[0])
        index = abs(((col + row * self.dimensions[0]) % self.dimensions[0]) - self.dimensions[0] + 1)
        # print(index)
        # ^^^ - for debugging purposes only
        #print(index % self.dimensions[0])
        #self.place_piece(index % self.dimensions[0])
        try:
            self.board[self.place_piece(index) * self.dimensions[0] + index] = 1 if self.Player else 2
        except:
            pass
        self.drawGUI(self.board[::-1])
        var = self.isGameOver()
        if var == 1:
            print("RED WON!")
        elif var == 2:
            print("YELLOW WON!")
        if var:
            self.GameOver(var)
            self.root.destroy()

    def GameOver(self, var):
        self.game_canvas.delete("all")
        for i in range(1, self.dimensions[0] * self.TILE_SIZE, 25):
            self.game_canvas.create_rectangle(0, i, self.dimensions[0] * self.TILE_SIZE, 0, fill=self.PlayerColors(var))
            time.sleep(0.05)
            self.game_canvas.update()

    def gameloop(self):
        self.drawGUI(self.board[::-1])
        '''
        while True:
            Column = abs(int(input()) - (self.dimensions[0] + 1)) - 1
            self.board[self.place_piece(Column) * self.dimensions[0] + Column] = 1 if self.Player else 2
            print(self.isGameOver())
        '''

    def place_piece(self, column):
        # some code snippets for placing a piece at designated square
        # check for empty column, if so, then find the lowest point that is available
        col = [item for index, item in enumerate(self.board) if index % (self.dimensions[0]) == column]
        if col.count(0) == 0:
            raise SystemError("invalid Move")
        # swap players after each **valid** move
        self.Player = not self.Player
        return col.index(0)

    def drawGUI(self, gameboard):
        self.game_canvas.delete("all")
        if self.draw_grid:
            for line in range(self.SIDE_LEN//self.TILE_SIZE):
                # iterates creating the vertical lines
                self.game_canvas.create_line(line * self.TILE_SIZE, 0, line*self.TILE_SIZE, self.SIDE_LEN, width = self.LINE_WID)
            for line in range(self.SIDE_LEN//self.TILE_SIZE):
                # create the horizontal lines
                self.game_canvas.create_line(0, line * self.TILE_SIZE, self.SIDE_LEN, line*self.TILE_SIZE, width = self.LINE_WID)
        for index, item in enumerate(gameboard):
            # find the row and column of the item based of the index in the array
            ind_col, ind_row = index // (self.SIDE_LEN//self.TILE_SIZE), index % (self.SIDE_LEN//self.TILE_SIZE)
            if item:
                # using ovals (circle) instead of rectangle since it makes sense
                self.game_canvas.create_oval((ind_row) * self.TILE_SIZE + 5, (ind_col) * self.TILE_SIZE + 5, (ind_row + 1) * self.TILE_SIZE - 5, (ind_col + 1) * self.TILE_SIZE - 5, fill = self.PlayerColors(item))

        self.game_canvas.update()
        self.game_canvas.pack()

    def isGameOver(self):
        # a "wrapper" function for checking if anyone won the game
        for i in range(len(self.board) + 1):
            for j in range(8):
                x, y = self.checkSpot(i, self.dirs[j], 1), self.checkSpot(i, self.dirs[j], 2)
                if x: return 1
                if y: return 2
        return 0

    def checkSpot(self, spot, direction, player):
        self.dirs = [
                    # define all the directions that can cause a win
                    # left, right, up, down, diagonals
                     -1, 1,
                     -self.dimensions[0], self.dimensions[0],
                     -self.dimensions[0]-1, self.dimensions[0]-1,
                     -self.dimensions[0]+1, self.dimensions[0]+1
                    ]
        try:
            # very quick and dirty way to implement bound checking
            # had already made most of the code so i couldnt switch
            # to changing the board with escape characters

            # just checking whether or not the index and the one before
            # have a 1 column distance from each other
            # print(self.board[spot + (i+1)*direction] == player and ((spot + (i + 1) * direction) % self.dimensions[0] == (spot + (i) * direction) % self.dimensions[0] or (spot + (i + 1) * direction) % self.dimensions[0] == (spot + (i) * direction) % self.dimensions[0] + 1 or (spot + (i + 1) * direction) % self.dimensions[0] == (spot + (i) * direction) % self.dimensions[0] - 1) for i in range(self.CONNECT))
            if all(self.board[spot + (i+1)*direction] == player and ((spot + (i + 1) * direction) % self.dimensions[0] == (spot + (i) * direction) % self.dimensions[0] or (spot + (i + 1) * direction) % self.dimensions[0] == (spot + (i) * direction) % self.dimensions[0] + 1 or (spot + (i + 1) * direction) % self.dimensions[0] == (spot + (i) * direction) % self.dimensions[0] - 1) for i in range(self.CONNECT)):
                return True
        # if indexError is thrown then it means we went out of bounds,
        # if we did then that means we tried searching below our array
        except IndexError: pass
        return False

    def PlayerColors(self, player):
        self.player_colors = {
            #1:"#FF5733",
            #2:"#E6D735",
            1:"#E61F00",
            2:"#E6AE00",
        }
        return self.player_colors[player]

connect = Connect()
connect.gameloop()
connect.root.mainloop()
