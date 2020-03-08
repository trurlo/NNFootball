from field import Field
import numpy as np

class State:
    def __init__(self, field: Field):
        self.current_position = (field.w//2,field.l//2)
        self.moves = np.zeros((field.w,field.l), dtype=np.uint8)

    def draw_possible_moves(self, window):
        

