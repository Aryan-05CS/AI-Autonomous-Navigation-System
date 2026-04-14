import pygame

class Agent:
    def __init__(self, pos):
        self.pos = pos  # (row, col)

    def move(self, new_pos):
        self.pos = new_pos

    def draw(self, win, cell_size):
        x = self.pos[1] * cell_size
        y = self.pos[0] * cell_size
        pygame.draw.rect(win, (255, 165, 0), (x, y, cell_size, cell_size))