from curses.textpad import rectangle

import pygame
from pygame.examples.headless_no_windows_needed import screen
from pygame.examples.testsprite import screen_dims

from common.game_color import GameColor
from common.game_default import GameDefault
from model.board.board import Board
from model.cell.cell import Cell
from view.cell_view import CellView

#
# class BoardView:
#     def __init__(self, board: Board, cell_view: CellView, board_color: GameColor, cell_color: GameColor):
#         self.board = board
#         self.cell_view = cell_view
#         self.board_color = board_color
#         self.cell_color = cell_color
#
#     def screen_dimension(self):
#         y = self.board.dimension.height * self.cell_view.cell_px
#         x = self.board.dimension.length * self.cell_view.cell_px
#         return x, y
#
#     def draw_board(self, surface: pygame.Surface):
#         # Draw board background (this will show as grid lines between cells)
#         rect = pygame.Rect(0, 0,
#                            self.board.dimension.length * self.cell_view.cell_px,
#                            self.board.dimension.height * self.cell_view.cell_px)
#         pygame.draw.rect(surface, self.board_color.pygame_color, rect)
#
#         # Draw all cells (with inset borders so board color shows through)
#         for row in self.board.cells:
#             for cell in row:
#                 self.cell_view.draw_cell(surface=surface, cell=cell, color=self.cell_color)


class BoardView:
    board: Board
    cell_view: CellView
    board_color: GameColor
    cell_color: GameColor

    def __init__(self, board: Board, cell_view: CellView): #, board_color: GameColor, cell_color: GameColor):
        self.board = board
        self.cell_view = cell_view
        # self.board_color = board_color
        # self.cell_color = cell_color

    def screen_dimension(self):
        y = self.board.dimension.height * self.cell_view.cell_px + GameDefault.SCREEN_PADDING
        x = self.board.dimension.length * self.cell_view.cell_px + GameDefault.SCREEN_PADDING
        return x, y

    def draw_board(self, surface: pygame.Surface):
        rect = pygame.Rect(
            0,
            0,
            self.board.dimension.length * self.cell_view.cell_px,
            self.board.dimension.height * self.cell_view.cell_px
        )
        pygame.draw.rect(surface, pygame.Color("red"), rect)
        # for row in self.board.cells:
        #     for cell in row:
        #         self.cell_view.draw_cell(surface=surface, cell=cell, color=self.cell_color)

