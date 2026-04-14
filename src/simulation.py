import pygame
import numpy as np
from planner import astar
from agent import Agent

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Simulation:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Autonomous Navigation")

        self.grid = np.zeros((ROWS, COLS))

        # obstacles
        self.grid[10:20, 15] = 1

        self.start = (0, 0)
        self.goal = (29, 29)

        self.path = astar(self.grid, self.start, self.goal)
        self.agent = Agent(self.start)
        self.goal_reached = False
        
        if not self.path:
            print("WARNING: No path found from start to goal!")

    def draw_grid():
     for row in range(ROWS):
        for col in range(ROWS):
            color = WHITE

            if grid[row][col] == 1:
                color = BLACK

            pygame.draw.rect(win, color,
                             (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            pygame.draw.rect(win, (200, 200, 200),
                             (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

            if self.grid[row][col] == 1:
                    color = BLACK
            if (row, col) in self.path:
                    color = BLUE
            if (row, col) == self.goal:
                    color = GREEN

            pygame.draw.rect(self.win, color, rect)
            pygame.draw.rect(self.win, (200,200,200), rect, 1)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        step = 0

        while running:
            clock.tick(5)
            self.win.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_grid()

            if step < len(self.path):
                self.agent.move(self.path[step])
                step += 1
            elif not self.goal_reached and len(self.path) > 0:
                self.goal_reached = True
                print("Goal reached!")

            self.agent.draw(self.win, CELL_SIZE)

            pygame.display.update()

        pygame.quit()