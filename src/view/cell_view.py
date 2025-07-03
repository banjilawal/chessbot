import pygame

from common.game_color import GameColor
from common.game_default import GameDefault
from model.cell.cell import Cell

#
# class CellView:
#     def __init__(self, cell_px: int):
#         self.cell_px = cell_px
#
#     def draw_cell(self, surface: pygame.Surface, cell: Cell, color: GameColor):
#         self.draw_cell_with_offset(surface, cell, color, 0, 0)
#
#     def draw_cell_with_offset(self, surface: pygame.Surface, cell: Cell, color: GameColor, offset_x: int,
#                               offset_y: int):
#         x = cell.coordinate.column * self.cell_px + offset_x
#         y = cell.coordinate.row * self.cell_px + offset_y
#
#         # Draw the cell with a 1-pixel border (inset)
#         rectangle = pygame.Rect(x + 1, y + 1, self.cell_px - 2, self.cell_px - 2)
#         pygame.draw.rect(surface, color.pygame_color, rectangle)

        # Alternative: Draw cell with border outline
        # rectangle = pygame.Rect(x, y, self.cell_px, self.cell_px)
        # pygame.draw.rect(surface, color.pygame_color, rectangle)
        # pygame.draw.rect(surface, (0, 0, 0), rectangle, 1)  # Black border

class CellView:
    def __init__(self, cell_px: int):
        self.cell_px = cell_px


    def draw_cell(self, surface: pygame.Surface, cell: Cell, color: GameColor):
        x = cell.coordinate.column * self.cell_px
        y = cell.coordinate.row * self.cell_px

        rectangle = pygame.Rect(x + 1, y + 1, self.cell_px -2, self.cell_px -2)
        pygame.draw.rect(surface, pygame.Color("blue"), rectangle)
