import pygame

from common.game_color import GameColor
from common.game_default import GameDefault
from model.board.board import Board
from model.cell.cell import Cell


class BoardView:
    board: Board
    cell_px: int
    color: GameColor

    def __init__(self, board: Board, cell_px: int = GameDefault.CELL_PX, color: GameColor = GameDefault.BOARD_COLOR):
        self.board = board
        self.cell_px = cell_px

    def screen_dimension(self):
        y = self.board.dimension.height * self.cell_px
        x = self.board.dimension.length * self.cell_px
        return x, y

    def draw_board(self, surface: pygame.Surface):
        for row_index in range(self.board.row_count()):
            for column_index in range(self.board.column_count()):
                cell = self.board.cells[row_index][column_index]
                self.draw_cell(surface, cell)

    def draw_cell(self, surface: pygame.Surface, cell: Cell):
        x = cell.coordinate.column * self.cell_px
        y = cell.coordinate.row * self.cell_px
        rectangle = pygame.Rect(x, y, self.cell_px, self.cell_px)
        pygame.draw.rect(surface, cell.color.pygame_color, rectangle)
