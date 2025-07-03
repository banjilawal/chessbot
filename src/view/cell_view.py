import pygame

from common.game_color import GameColor
from model.cell.cell import Cell

class CellView:
    def __init__(self, cell_px: int):
        self.cell_px = cell_px


    def draw_cell(self, surface: pygame.Surface, cell: Cell, color: GameColor):
        x = cell.coordinate.column * self.cell_px
        y = cell.coordinate.row * self.cell_px

        rectangle = pygame.Rect(x, y, self.cell_px, self.cell_px)
        pygame.draw.rect(surface, color.pygame_color, rectangle)