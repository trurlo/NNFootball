from field import Field
import numpy as np
import directions
import pygame

class State:
    def __init__(self, field: Field, window):
        self.starting_position = field.center_point
        self.current_position = field.center_point
        self.tracks = np.zeros((field.w,field.l), dtype=np.uint8) # array to keep blocked (already used) tracks
        self.moves = [] # list to hold subsequent moves
        self.field = field
        self.window = window
        self.whose_turn = 0
        # clear outside
        for i in range(field.w):
            self.tracks[i,0] = self.tracks[i,0] | (1<<directions.N|1<<directions.NE|1<<directions.NW|1<<directions.E|1<<directions.W)
            self.tracks[i,field.l-1] = self.tracks[i,field.l-1] | (1<<directions.S|1<<directions.SE|1<<directions.SW|1<<directions.E|1<<directions.W)
        for i in range(field.l):
            self.tracks[0,i] = self.tracks[0,i] | (1<<directions.N|1<<directions.NW|1<<directions.W|1<<directions.SW|1<<directions.S)
            self.tracks[field.w-1,i] = self.tracks[field.w-1,i] | (1<<directions.N|1<<directions.NE|1<<directions.E|1<<directions.SE|1<<directions.S)

    def switch_player(self):
        if self.whose_turn:
            self.whose_turn = 0
        else:
            self.whose_turn = 1

    def draw_possible_moves(self, position):
        for i in range(8):
            if not (self.tracks[position] & 1<<i):
                self.field.draw_move(self.window,position,i,self.field.possible_move_color)

    def draw_all_possible_moves(self):
        for c in range(self.field.w):
            for r in range(self.field.l):
                self.draw_possible_moves((c,r))

    def draw_ball(self):
        pygame.draw.circle(self.window, self.field.ball_color, self.field.get_point_coords(self.current_position),8,1)                

    def draw_whose_turn(self):
        if not self.whose_turn :
            pygame.draw.circle(self.window, self.field.field_color, (self.field.left_margin+10,self.field.top_margin+10),8)
        else:
            pygame.draw.circle(self.window, self.field.field_color, (self.field.left_margin+10,self.field.get_pixel_field_size()[1]-self.field.bottom_margin-10),8)

    def draw_moves(self):
        pos = self.starting_position
        for move in self.moves:
            self.field.draw_move(self.window,pos,move&7,(255*(move&128)>>7,0,255)) # strip bits 3-7 from move
            pos = directions.go(pos,move&7)         

    def can_move(self, from_position, direction):
        return not (self.tracks[from_position]&1<<direction)

    def move(self, direction):
        if self.can_move(self.current_position, direction):
            self.moves.append(direction|(128*self.whose_turn)) # pack whose_turn into 7th bit
            self.tracks[self.current_position] = self.tracks[self.current_position] | 1<<direction # block track from starting position in this direction
            self.current_position = directions.go(self.current_position,direction)
            if not self.tracks[self.current_position]: # if new field was empty (not jumpable)
                self.switch_player()
            self.tracks[self.current_position] = self.tracks[self.current_position] | 1<<((direction+4)%8) # block reversed direction from new position

    def undo(self):
        if self.moves: # if there are any moves to undo, ie. if the list is not empty
            dir = self.moves.pop() # get and remove last move from stack
            self.whose_turn = (dir & 128)>>7 # restore whose_turn from 7th bit
            dir = dir&7 # and strip bits 3-7
            self.tracks[self.current_position] = self.tracks[self.current_position] &~(1<<(dir+4)%8)  # release backward track
            self.current_position = directions.go(self.current_position,(dir+4)%8) # backtrack one move
            self.tracks[self.current_position] = self.tracks[self.current_position] &~(1<<dir) # release forward track

    def dump(self):
        fn = open("state.txt","w")
        fn.write("current_position: "+str(self.current_position))
        fn.write("\n\n")
        fn.write("whose turn: "+str(self.whose_turn))
        fn.write("\n\n")
        for move in self.moves: 
            fn.write(str(move)+' ')
        fn.write("\n\n")
        for r in range(self.field.l):
            for c in range(self.field.w):
                fn.write(str(self.tracks[c,r]).zfill(3)+' ')
            fn.write("\n")
        fn.close()
            
