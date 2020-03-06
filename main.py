import pygame
import colors
from field import Field
from state import State

fld = Field(width=9, length=11, fieldgrid=50, goalsize=3)

pygame.init()
win = pygame.display.set_mode(fld.get_pixel_field_size())
FPS = 60
clock = pygame.time.Clock()
state = State(fld)

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.fill(colors.BLACK)
    fld.draw(win)
    pygame.display.flip()

pygame.quit()