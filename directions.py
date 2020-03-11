import pygame

N   = 0
NE  = 1
E   = 2 
SE  = 3
S   = 4
SW  = 5
W   = 6
NW  = 7

def go_N(from_position):
    return (from_position[0],from_position[1]-1)

def go_NE(from_position):
    return (from_position[0]+1,from_position[1]-1)

def go_E(from_position):
    return (from_position[0]+1,from_position[1])

def go_SE(from_position):
    return (from_position[0]+1,from_position[1]+1)

def go_S(from_position):
    return (from_position[0],from_position[1]+1)

def go_SW(from_position):
    return (from_position[0]-1,from_position[1]+1)

def go_W(from_position):
    return (from_position[0]-1,from_position[1])

def go_NW(from_position):
    return (from_position[0]-1,from_position[1]-1)

go_map = (go_N,go_NE,go_E,go_SE,go_S,go_SW,go_W,go_NW)
key_map = {
    pygame.K_KP8:N,
    pygame.K_KP9:NE,
    pygame.K_KP6:E,
    pygame.K_KP3:SE,
    pygame.K_KP2:S,
    pygame.K_KP1:SW,
    pygame.K_KP4:W,
    pygame.K_KP7:NW
    }

def go(from_position, direction):
    return go_map[direction](from_position)
