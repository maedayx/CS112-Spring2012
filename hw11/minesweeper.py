#! /usr/bin/env python

import pygame, random
from pygame.locals import *
from pygame import draw

# Classes
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_mine = False
        self.nearby = 0
        self.is_revealed = False # Change to false!
        self.cell_rect = pygame.Rect(self.x*(CELL_WIDTH+2), self.y*(CELL_HEIGHT+2), CELL_WIDTH, CELL_HEIGHT)
        self.color = CELL_COLOR
    
    @property
    def adjacent_cells(self):
        adjacent_cells = []
        if self.x+1 < GAME_SIZE:
            adjacent_cells.append((self.x+1,self.y))
        if self.x-1 >= 0:
            adjacent_cells.append((self.x-1,self.y))
        if self.y+1 < GAME_SIZE:
            adjacent_cells.append((self.x,self.y+1))
        if self.y-1 >= 0:
            adjacent_cells.append((self.x,self.y-1))
        if self.y-1 >= 0 and self.x-1 >= 0:
            adjacent_cells.append((self.x-1,self.y-1))
        if self.y+1 < GAME_SIZE and self.x+1 < GAME_SIZE:
            adjacent_cells.append((self.x+1,self.y+1))
        if self.y-1 >= 0 and self.x+1 < GAME_SIZE:
            adjacent_cells.append((self.x+1,self.y-1))
        if self.y+1 < GAME_SIZE and self.x-1 >= 0:
            adjacent_cells.append((self.x-1,self.y+1))
        return adjacent_cells
    
    def draw_hidden(self):
        draw.rect(screen, self.color, self.cell_rect)
     
    def draw_revealed(self):
        if self.is_mine:
            self.color = MINE_COLOR
            nearby_text = nearby_font.render("M", True, (0,0,0))
        else:
            nearby_text = nearby_font.render(str(self.nearby), True, (0,0,0))
        loc = nearby_text.get_rect()
        loc.center = self.cell_rect.center
        draw.rect(screen, self.color, self.cell_rect)
        screen.blit(nearby_text, loc)
        
    def draw(self):
        if self.is_revealed:
            self.draw_revealed()
        else:
            self.draw_hidden()
    

# Set up constants
GAME_SIZE = 10
GAME_MINES = 10 # Small size & mines for test games
CELL_SIZE = CELL_WIDTH, CELL_HEIGHT = 50, 50
CELL_COLOR = 255,255,255
MINE_COLOR = 255,0,0
FLAGGED_COLOR = 0,255,0
REVEALED_COLOR = 170,170,170
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (CELL_WIDTH+2)*GAME_SIZE-1, (CELL_HEIGHT+2)*GAME_SIZE-1
FPS = 30

# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill((0,0,0))

nearby_font = pygame.font.Font(None, 50)

def start_game():
    # Set up board
    mines = []
    found_mines = 0
    board = [ [Cell(x,y) for x in range(GAME_SIZE)] for y in range(GAME_SIZE) ] # Build the board

    # Fill the board with mines
    x = random.randint(0,GAME_SIZE-1)
    y = random.randint(0,GAME_SIZE-1)
    for i in range(GAME_MINES):
        while board[y][x].is_mine == True: # Make sure there's not aleady a mine there, if there is pick a new random spot
            x = random.randint(0,GAME_SIZE-1)
            y = random.randint(0,GAME_SIZE-1)
        board[y][x].is_mine = True # Place the mine!
        mines.append((x,y))
    
    # Calculate the numbers of nearby mines
    for row in board:
        for cell in row:
            if cell.is_mine == False:
                for adj_cell in cell.adjacent_cells:
                    if adj_cell in mines:
                        cell.nearby += 1

clock = pygame.time.Clock()

# Set up board
mines = []
found_mines = 0
board = [ [Cell(x,y) for x in range(GAME_SIZE)] for y in range(GAME_SIZE) ] # Build the board

# Fill the board with mines
x = random.randint(0,GAME_SIZE-1)
y = random.randint(0,GAME_SIZE-1)
for i in range(GAME_MINES):
    while board[y][x].is_mine == True: # Make sure there's not aleady a mine there, if there is pick a new random spot
        x = random.randint(0,GAME_SIZE-1)
        y = random.randint(0,GAME_SIZE-1)
    board[y][x].is_mine = True # Place the mine!
    mines.append((x,y))

# Calculate the numbers of nearby mines
for row in board:
    for cell in row:
        if cell.is_mine == False:
            for adj_cell in cell.adjacent_cells:
                if adj_cell in mines:
                    cell.nearby += 1

# Set up game loop
done = False
game_over = False
won = False

# Game loop
while not done:
    # Events
    for event in pygame.event.get():
        # Game Loop control
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_SPACE and game_over == True:
            # Set up board
            mines = []
            found_mines = 0
            board = [ [Cell(x,y) for x in range(GAME_SIZE)] for y in range(GAME_SIZE) ] # Build the board

            # Fill the board with mines
            x = random.randint(0,GAME_SIZE-1)
            y = random.randint(0,GAME_SIZE-1)
            for i in range(GAME_MINES):
                while board[y][x].is_mine == True: # Make sure there's not aleady a mine there, if there is pick a new random spot
                    x = random.randint(0,GAME_SIZE-1)
                    y = random.randint(0,GAME_SIZE-1)
                board[y][x].is_mine = True # Place the mine!
                mines.append((x,y))

            # Calculate the numbers of nearby mines
            for row in board:
                for cell in row:
                    if cell.is_mine == False:
                        for adj_cell in cell.adjacent_cells:
                            if adj_cell in mines:
                                cell.nearby += 1
            # Set up game loop
            done = False
            game_over = False
            won = False
        # Revealing spots
        elif event.type == MOUSEBUTTONDOWN and not game_over:
            if event.button == 1:
                for row in board:
                    for cell in row:
                        if cell.cell_rect.collidepoint(pygame.mouse.get_pos()):
                            cell.is_revealed = True
                            cell.color = REVEALED_COLOR
                            if cell.is_mine:
                                game_over = True # If player clicked on a mine, it's game over!
                            else:
                                # Reveal adjacent cells that aren't mines
                                for adj_cell in cell.adjacent_cells:
                                    if not adj_cell in mines:
                                        x = adj_cell[0]
                                        y = adj_cell[1]
                                        board[y][x].is_revealed = True
                                        board[y][x].color = REVEALED_COLOR
                                        for next_cell in board[y][x].adjacent_cells:
                                            if not next_cell in mines:
                                                x = next_cell[0]
                                                y = next_cell[1]
                                                board[y][x].is_revealed = True
                                                board[y][x].color = REVEALED_COLOR
            elif event.button == 3:
                for row in board:
                    for cell in row:
                        if cell.cell_rect.collidepoint(pygame.mouse.get_pos()) and cell.color != FLAGGED_COLOR:
                            cell.color = FLAGGED_COLOR
                            if cell.is_mine:
                                found_mines += 1
                        elif cell.cell_rect.collidepoint(pygame.mouse.get_pos()) and cell.color == FLAGGED_COLOR:
                            cell.color = CELL_COLOR
                            if cell.is_mine:
                                found_mines -= 1
    
    # Draw Board
    for row in board:
        for cell in row:
            cell.draw()
    
    if found_mines == GAME_MINES:
        won = True
        game_over = True
    
    if game_over and not won:
        for mine in mines:
            if board[mine[1]][mine[0]].color != FLAGGED_COLOR:    
                board[mine[1]][mine[0]].is_revealed = True
                
    if game_over and won:
        for row in board:
            for cell in row:
                cell.color = FLAGGED_COLOR
    
    # Refresh
    pygame.display.flip()
    clock.tick(FPS)    