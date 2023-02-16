import pprint

import pygame
from copy import deepcopy


class Board:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.board = [[0 for i in range(cols)] for _ in range(rows)]
        self.left = 25
        self.top = 25
        self.cell_size = 30
        self.is_game = False

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        color = "white"
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[j][i] == 1:
                    pygame.draw.rect(screen, "green", (self.left + self.cell_size * i,
                                                     self.top + self.cell_size * j,
                                                     self.cell_size, self.cell_size))

                pygame.draw.rect(screen, color, (self.left + self.cell_size * i,
                                                 self.top + self.cell_size * j,
                                                 self.cell_size, self.cell_size), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell):
        if cell is None:
            return None
        self.board[cell[1]][cell[0]] = 1

    def get_cell(self, mouse_pos):
        pos = mouse_pos
        if 0 <= (pos[0] - self.left) // self.cell_size <= self.cols - 1 and \
                0 <= (pos[1] - self.top) // self.cell_size <= self.rows - 1:
            return (pos[0] - self.left) // self.cell_size, (pos[1] - self.top) // self.cell_size
        else:
            return None


class Life(Board):
    def __init__(self, cols, rows):
        super().__init__(cols, rows)

    def next_move(self):
        board = deepcopy(self.board)

        for i in range(self.cols):
            for j in range(self.rows):
                cnt = 0
                if j < self.rows - 1 and self.board[j + 1][i] == 1:
                    cnt += 1
                if j > 0 and self.board[j - 1][i] == 1:
                    cnt += 1
                if i < self.cols - 1 and j < self.rows - 1 and self.board[j + 1][i + 1] == 1:
                    cnt += 1
                if i > 0 and j < self.rows - 1 and self.board[j + 1][i - 1] == 1:
                    cnt += 1
                if i < self.cols - 1 and j > 0 and self.board[j - 1][i + 1] == 1:
                    cnt += 1
                if i > 0 and j > 0 and self.board[j - 1][i - 1] == 1:
                    cnt += 1
                if i > 0 and self.board[j][i - 1] == 1:
                    cnt += 1
                if i < self.cols - 1 and self.board[j][i + 1] == 1:
                    cnt += 1

                if self.board[j][i] == 0 and cnt == 3:
                    board[j][i] = 1
                if self.board[j][i] == 1 and cnt != 2 and cnt != 3:
                    board[j][i] = 0

        self.board = deepcopy(board)


if __name__ == "__main__":
    pygame.init()
    number_of_cells = 30
    size = width, height = 50 + number_of_cells * 30, 50 + number_of_cells * 30
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Игра «Жизнь»")

    board = Life(number_of_cells, number_of_cells)
    running = True
    FPS = 10
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if board.is_game:
                        board.is_game = False
                    else:
                        board.is_game = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not board.is_game:
                    board.get_click(event.pos)
                elif event.button == 3:
                    if board.is_game:
                        board.is_game = False
                    else:
                        board.is_game = True
                elif event.button == 4:
                    FPS += 10
                elif event.button == 5:
                    FPS -= 10

        if board.is_game:
            board.next_move()

        screen.fill((0, 0, 0))
        board.render()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
