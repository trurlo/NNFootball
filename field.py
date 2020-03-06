import pygame
import colors

class Field:
    def __init__(self, width: int, length: int, fieldgrid: int, goalsize: int):
        if width%2 == 0:
            raise ValueError("Field width must be an odd number.")
        if length%2 == 0:
            raise ValueError("Field length must be an odd number.")
        if goalsize%2 == 0:
            raise ValueError("Goal size must be an odd number.")
        if goalsize > width - 2:
            raise ValueError("Goal too big.")
        self.w = width
        self.l = length
        self.f = fieldgrid
        self.g = goalsize
        self.left_margin = fieldgrid
        self.top_margin = fieldgrid
        self.bottom_margin = fieldgrid
        self.right_margin = fieldgrid
        self.perimeter_points = (
            (self.left_margin,self.top_margin+self.f), # 1
            (self.left_margin+((self.w-self.g)//2)*self.f,self.top_margin+self.f), # 2
            (self.left_margin+((self.w-self.g)//2)*self.f,self.top_margin), # 3
            (self.left_margin+((self.w-self.g)//2+self.g-1)*self.f,self.top_margin), # 4
            (self.left_margin+((self.w-self.g)//2+self.g-1)*self.f,self.top_margin+self.f), # 5
            ((self.w-1)*self.f+self.left_margin,self.top_margin+self.f), # 6
            ((self.w-1)*self.f+self.left_margin,self.l*self.f+self.top_margin), # 7
            (self.left_margin+((self.w-self.g)//2+self.g-1)*self.f,self.l*self.f+self.top_margin), # 8
            (self.left_margin+((self.w-self.g)//2+self.g-1)*self.f,(self.l+1)*self.f+self.top_margin), # 9
            (self.left_margin+((self.w-self.g)//2)*self.f,(self.l+1)*self.f+self.top_margin), # 10
            (self.left_margin+((self.w-self.g)//2)*self.f,self.l*self.f+self.top_margin), # 11
            (self.left_margin,self.l*self.f+self.top_margin) # 12
        )
        self.line_width = 2
        self.center_point = ((self.w-1)//2,(self.l+1)//2)
        self.field_color = colors.WHITE
        self.center_color = colors.BLUE
        self.perimeter_color = colors.WHITE
        self.perimeter_width = 2
        self.point_size = 3
       
        
    def get_pixel_field_size(self):
        return ((self.w-1)*self.f+self.left_margin+self.right_margin,(self.l+1)*self.f+self.top_margin+self.bottom_margin)

    def draw_move(self, window: pygame.Surface, from_position, direction: int)
        


    def draw(self, window: pygame.Surface):
        pygame.draw.polygon(window, self.perimeter_color, self.perimeter_points, self.perimeter_width) # perimeter lines
        # actual field:
        for c in range(self.w):
            for r in range(self.l):
                pygame.draw.circle(window, self.field_color, (self.left_margin+c*self.f,self.top_margin+(r+1)*self.f),2)
        pygame.draw.circle(window, colors.BLUE, (self.left_margin+self.center_point[0]*self.f, self.top_margin+self.center_point[1]*self.f), self.point_size) # center point
        # goal
        for c in range(self.g):
            pygame.draw.circle(window, self.field_color, (self.left_margin+self.f*(c+(self.w-self.g)//2),self.top_margin), self.point_size)
            pygame.draw.circle(window, self.field_color, (self.left_margin+self.f*(c+(self.w-self.g)//2),self.top_margin+(self.f+1)*self.l), self.point_size)
        
