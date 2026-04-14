import pygame
import numpy as np
from planner import astar
from agent_v2 import Agent

# Setup
WIDTH = 600
ROWS = 20
CELL_SIZE = WIDTH // ROWS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Autonomous Navigation")

# Grid
grid = np.zeros((ROWS, ROWS))

# Obstacles
grid[5][5] = 1
grid[5][6] = 1
grid[5][7] = 1

start = (0, 0)
goal = (15, 15)

path = astar(grid, start, goal)
agent = Agent(start)
step = 0

# Draw grid
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

# Draw path
def draw_path(path):
    for (row, col) in path:
        pygame.draw.rect(win, BLUE,
                         (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def get_cell_pos(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col

# Main loop
running = True

while running:
    pygame.time.delay(200)
    win.fill(WHITE)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        row = pos[1] // CELL_SIZE
        col = pos[0] // CELL_SIZE

        if event.button == 1:  # LEFT CLICK
            if (row, col) != start and (row, col) != goal:
                grid[row][col] = 1

        elif event.button == 3:  # RIGHT CLICK
            grid[row][col] = 0

        # Recalculate path
        path = astar(grid, start, goal)
        step = 0

    draw_grid()
    draw_path(path)

    # Draw start
    pygame.draw.rect(win, (0, 255, 0),
                     (start[1]*CELL_SIZE, start[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw goal
    pygame.draw.rect(win, (255, 0, 0),
                     (goal[1]*CELL_SIZE, goal[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Move agent step-by-step
    if step < len(path):
        agent.move(path[step])
        step += 1

    agent.draw(win, CELL_SIZE)

    pygame.display.update()

pygame.quit()