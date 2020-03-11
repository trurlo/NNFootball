import pygame
import colors
from field import Field
from state import State
import directions

fld = Field(width=9, length=11, fieldgrid=30, goalsize=3)

pygame.init()
win = pygame.display.set_mode(fld.get_pixel_field_size())
FPS = 60
clock = pygame.time.Clock()
state = State(fld,win)

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in directions.key_map.keys():
                state.move(directions.key_map[event.key])
            if event.key == pygame.K_q: # quit
                running = False
            if event.key == pygame.K_r: # reset state
                state = State(fld,win)
            if event.key in (pygame.K_u, pygame.K_KP5): # undo last move
                state.undo()
            if event.key == pygame.K_d: # dump state to "state.txt"
                state.dump()
    win.fill(colors.BLACK)
    state.draw_all_possible_moves()
    fld.draw(win)
    state.draw_moves()
    state.draw_ball()
    state.draw_whose_turn()
    pygame.display.flip()

pygame.quit()