import copy
import random
from shapes import *

class ObisTrisGameState:
    width: int
    height: int
    board: list[list[int]]
    score: int


    def __init__(self):
        self.score = 0
        self.width = 15
        self.height = 50
        self.board = [[0 for x in range(self.width)] for y in range(self.height)]
        self.is_game_over = False
        self.new_block()

    def advance(self):
        if self.current_block_landed():
            self.land_block()
            self.handle_lines()
            self.new_block()
            if self.current_block_intersects():
                self.game_over()
        else:
            self.current_block.y += 1
        
    def rotate(self):
        self.current_block.rotate()

    def right(self):
        return self.move_x(1)

    def left(self):
        return self.move_x(-1)

    def move_x(self, amount):
        new_x_min = self.current_block.x + amount
        new_x_max = new_x_min + self.current_block.width
        
        # check board bounds
        if new_x_min < 0 or new_x_max > self.width:
            return False
        
        # check if overlap with existing cells
        for vpos, shape_line in enumerate(self.current_block.shape):
            for hpos, h in enumerate(shape_line):
                if h and self.board[self.current_block.y + vpos][new_x_min + hpos]:
                    return False
                
        self.current_block.x += amount
        return True

    def down(self):
        self.advance()
    
    # return the current game board with the current block in place as a matrix
    def get_board_map(self):
        # first deep clone game state so we can render current block
        myboard = copy.deepcopy(self.board)

        for vpos, v in enumerate(self.current_block.shape):
            for hpos, h in enumerate(v):
                if h:
                    myboard[self.current_block.y + vpos][self.current_block.x + hpos] = h
        
        return myboard

    def current_block_landed(self):
        return self.current_block_touches_bottom() or self.current_block_intersects()

    def current_block_touches_bottom(self):
        # assumes shape always has at least one block in its lowest line, this is gonna be a fun bug later :P
        return (self.current_block.y + self.current_block.height) == self.height
    
    def current_block_intersects(self):      
        for vpos, shape_line in enumerate(self.current_block.shape):
            for hpos, h in enumerate(shape_line):
                if h and self.board[self.current_block.y + vpos + 1][self.current_block.x + hpos]:
                    return True
        return False

    # 'lands' the current block, as in, adds the occupied cells to the board
    def land_block(self):
        self.board = self.get_board_map()

    def new_block(self):
        # this is highly inefficient but it really doesnt matter right now
        options = [ObisTrisHero(), ObisTrisOrangeRicky(), ObisTrisBlueRicky(), ObisTrisSmashboy(), ObisTrisCleveland(), ObisTrisRhodeIsland(), ObisTrisTeeWee()]
        self.current_block = random.choice(options)
    
    def handle_lines(self):
        for i, line in enumerate(self.board):
            if all(line):
                self.score += 1
                del(self.board[i])
                self.board.insert(0, [0 for x in range(self.width)])

    # super simple implementation of levels
    def get_interval(self):
        return max(0.075, 0.5 - int(self.score/5)*0.05)
    

    def game_over(self):
        self.is_game_over = True


    # simple debugging method to show the board as ascii
    def print(self):
        # todo extract class

        # clear the screen
        print("\033[2J", end="")

        print("Score: ", self.score)
        for line in self.get_board_map():
            print("".join(["#" if x else "_" for x in line]))
