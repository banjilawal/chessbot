import pygame

from model.board.board import Board
from model.cell.cell import Cell


class BoardView:
    board: Board
    cell_px: int

    def __init__(self, board: Board, cell_px: int):
        self.board = board
        self.cell_px = cell_px
    #

    def draw_board(self, surface: pygame.Surface):
        """Draw the board on the given surface."""
        for row_index in range(self.board.row_count):
            for column_index in range(self.board.column_count):
                cell = self.board.cells[row_index][column_index]
                self.draw_cell(surface, cell)
    #

    def draw_cell(self, surface: pygame.Surface, cell: Cell):
        x = cell.column * self.cell_px
        y = cell.row * self.cell_px
        rectangle = pygame.Rect(x, y, self.cell_px, self.cell_px)
        pygame.draw.rect(surface, cell.color.pygame_color, rectangle)
    #
