import pprint

import pygame


class Board:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.board = [[0 for i in range(cols)] for _ in range(rows)]
        self.left = 25
        self.top = 25
        self.cell_size = 50
        self.step = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        color = "white"
        for i in range(self.cols):
            for j in range(self.rows):
                pygame.draw.rect(screen, color, (self.left + self.cell_size * i,
                                                 self.top + self.cell_size * j,
                                                 self.cell_size, self.cell_size), 1)
                if self.board[j][i] == -2:
                    pygame.draw.circle(screen, "red",
                                       (self.left + self.cell_size * i + self.cell_size // 2,
                                        self.top + self.cell_size * j + self.cell_size // 2),
                                       self.cell_size // 2 - 1)
                if self.board[j][i] == -1:
                    pygame.draw.circle(screen, "blue",
                                       (self.left + self.cell_size * i + self.cell_size // 2,
                                        self.top + self.cell_size * j + self.cell_size // 2),
                                       self.cell_size // 2 - 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell):
        pass

    def get_cell(self, mouse_pos):
        pos = mouse_pos
        if 0 <= (pos[0] - self.left) // self.cell_size <= self.cols - 1 and \
                0 <= (pos[1] - self.top) // self.cell_size <= self.rows - 1:
            return (pos[0] - self.left) // self.cell_size, (pos[1] - self.top) // self.cell_size
        else:
            return None


class Lines(Board):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.red = None

    def on_click(self, cell):
        if self.red is None:
            if self.board[cell[1]][cell[0]] == 0:
                self.board[cell[1]][cell[0]] = -1
            elif self.board[cell[1]][cell[0]] == -1:
                self.board[cell[1]][cell[0]] = -2
                self.red = cell
            elif self.board[cell[1]][cell[0]] == -2:
                self.board[cell[1]][cell[0]] = 0
                self.red = None

        elif self.board[cell[1]][cell[0]] == 0:
            if self.has_path(cell[1], cell[0], self.red[1], self.red[0]):
                self.board[cell[1]][cell[0]] = -1
                self.board[self.red[1]][self.red[0]] = 0
                self.red = None

        elif self.board[cell[1]][cell[0]] == -2:
            self.board[cell[1]][cell[0]] = -1
            self.red = None
            pprint.pprint(self.board)

    def has_path(self, x1, y1, x2, y2):
        board_local = [elem.copy() for elem in self.board]
        for i in range(10):
            for j in range(10):
                if board_local[i][j] == -2:
                    board_local[i][j] = 0
        board_local = self.voln(x1, y1, 1, board_local)
        if board_local[x2][y2] > 0:
            return True
        else:
            return False

    def voln(self, x, y, cur, board):
        board[x][y] = cur
        if y + 1 < 10:
            if board[x][y + 1] == 0 or (board[x][y + 1] != -1 and board[x][y + 1] > cur):
                self.voln(x, y + 1, cur + 1, board)
        if x + 1 < 10:
            if board[x + 1][y] == 0 or (board[x + 1][y] != -1 and board[x + 1][y] > cur):
                self.voln(x + 1, y, cur + 1, board)
        if x - 1 >= 0:
            if board[x - 1][y] == 0 or (board[x - 1][y] != -1 and board[x - 1][y] > cur):
                self.voln(x - 1, y, cur + 1, board)
        if y - 1 >= 0:
            if board[x][y - 1] == 0 or (board[x][y - 1] != -1 and board[x][y - 1] > cur):
                self.voln(x, y - 1, cur + 1, board)
        return board


if __name__ == "__main__":
    pygame.init()
    number_of_cells = 10
    size = width, height = 50 + number_of_cells * 50, 50 + number_of_cells * 50
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Линеечки")

    board = Lines(number_of_cells, number_of_cells)
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
