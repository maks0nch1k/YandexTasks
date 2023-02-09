import pygame
import random


class Board:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        possible_bombs = list(range(0, number_of_cells[0] * number_of_cells[1]))
        self.board = [[-1 for i in range(number_of_cells[0])] for j in range(number_of_cells[1])]
        for i in range(number_of_mines):
            ind = random.choice(possible_bombs)
            del possible_bombs[possible_bombs.index(ind)]
            self.board[ind // number_of_cells[1]][ind % number_of_cells[0]] = 10
        self.left = 25
        self.top = 25
        self.cell_size = 50
        self.step = 0
        self.arr = [[] for i in range(8)]

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        color = "white"
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[j][i] == 10:
                    pygame.draw.rect(screen, "red", (self.left + self.cell_size * i,
                                                     self.top + self.cell_size * j,
                                                     self.cell_size, self.cell_size))
                elif self.board[j][i] > -1:
                    f2 = pygame.font.SysFont('serif', 48)
                    text2 = f2.render(str(self.board[j][i]), True, "green")
                    screen.blit(text2, (self.left + self.cell_size * i, self.top + self.cell_size * j))
                pygame.draw.rect(screen, color, (self.left + self.cell_size * i,
                                                 self.top + self.cell_size * j,
                                                 self.cell_size, self.cell_size), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.arr = [[] for i in range(8)]
        self.on_click(cell)

    def on_click(self, cell):
        if cell is not None and self.board[cell[1]][cell[0]] != 10:
            self.board[cell[1]][cell[0]] = 0
            self.open_cell(cell)

    def open_cell(self, cell):
        if cell[1] < self.rows - 1 and self.board[cell[1] + 1][cell[0]] == 10:
            self.board[cell[1]][cell[0]] += 1
        if cell[1] > 0 and self.board[cell[1] - 1][cell[0]] == 10:
            self.board[cell[1]][cell[0]] += 1
        if cell[0] < self.cols - 1 and cell[1] < self.rows - 1 and self.board[cell[1] + 1][cell[0] + 1] == 10:
            self.board[cell[1]][cell[0]] += 1
        if cell[0] > 0 and cell[1] < self.rows - 1 and self.board[cell[1] + 1][cell[0] - 1] == 10:
            self.board[cell[1]][cell[0]] += 1
        if cell[0] < self.cols - 1 and cell[1] > 0 and self.board[cell[1] - 1][cell[0] + 1] == 10:
            self.board[cell[1]][cell[0]] += 1
        if cell[0] > 0 and cell[1] > 0 and self.board[cell[1] - 1][cell[0] - 1] == 10:
            self.board[cell[1]][cell[0]] += 1
        if cell[0] > 0 and self.board[cell[1]][cell[0] - 1] == 10:
            self.board[cell[1]][cell[0]] += 1
        if cell[0] < self.cols - 1 and self.board[cell[1]][cell[0] + 1] == 10:
            self.board[cell[1]][cell[0]] += 1

        if cell[1] < self.rows - 1 and self.board[cell[1]][cell[0]] == 0 and (cell[0], cell[1]) not in self.arr[0]:
            self.arr[0].append((cell[0], cell[1]))
            self.on_click((cell[0], cell[1] + 1))
        if cell[1] > 0 and self.board[cell[1]][cell[0]] == 0 and (cell[0], cell[1]) not in self.arr[1]:
            self.arr[1].append((cell[0], cell[1]))
            self.on_click((cell[0], cell[1] - 1))
        if cell[0] < self.cols - 1 and cell[1] < self.rows - 1 and self.board[cell[1]][cell[0]] == 0 and (cell[0], cell[1]) not in self.arr[2]:
            self.arr[2].append((cell[0], cell[1]))
            self.on_click((cell[0] + 1, cell[1] + 1))
        if cell[0] > 0 and cell[1] < self.rows - 1 and self.board[cell[1]][cell[0]] == 0 and (cell[0], cell[1]) not in self.arr[3]:
            self.arr[3].append((cell[0], cell[1]))
            self.on_click((cell[0] - 1, cell[1] + 1))
        if cell[0] < self.cols - 1 and cell[1] > 0 and self.board[cell[1]][cell[0]] == 0 and (cell[0], cell[1]) not in self.arr[4]:
            self.arr[4].append((cell[0], cell[1]))
            self.on_click((cell[0] + 1, cell[1] - 1))
        if cell[0] > 0 and cell[1] > 0 and self.board[cell[1]][cell[0]] == 0 and (cell[0], cell[1]) not in self.arr[5]:
            self.arr[5].append((cell[0], cell[1]))
            self.on_click((cell[0] - 1, cell[1] - 1))
        if cell[0] > 0 and self.board[cell[1]][cell[0]] == 0 and (cell[0], cell[1]) not in self.arr[6]:
            self.arr[6].append((cell[0], cell[1]))
            self.on_click((cell[0] - 1, cell[1]))
        if cell[0] < self.cols - 1 and self.board[cell[1]][cell[0]] == 0 and (cell[0], cell[1]) not in self.arr[7]:
            self.arr[7].append((cell[0], cell[1]))
            self.on_click((cell[0] + 1, cell[1]))

    def get_cell(self, mouse_pos):
        pos = mouse_pos
        if 0 <= (pos[0] - self.left) // self.cell_size <= self.cols - 1 and \
                0 <= (pos[1] - self.top) // self.cell_size <= self.rows - 1:
            return (pos[0] - self.left) // self.cell_size, (pos[1] - self.top) // self.cell_size
        else:
            return None


if __name__ == "__main__":
    pygame.init()
    number_of_cells = tuple(map(int, input().split()))
    number_of_mines = int(input())
    size = width, height = 50 + number_of_cells[0] * 50, 50 + number_of_cells[1] * 50
    screen = pygame.display.set_mode(size)

    board = Board(number_of_cells[0], number_of_cells[1])
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render()
        pygame.display.flip()
    pygame.quit()
