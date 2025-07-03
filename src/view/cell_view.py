import pygame

from model.cell.cell import Cell

class CellView:
    def __init__(self, cell_px: int):
        self.cell_px = cell_px

    def draw_cell(self, surface: pygame.Surface, cell: Cell):
        global color
        x = cell.coordinate.column * self.cell_px
        y = cell.coordinate.row * self.cell_px

        rectangle = pygame.Rect(x, y, self.cell_px, self.cell_px)


        if cell.color and hasattr(cell.color, "pygame_color"):
            color = cell.color.pygame_color
        pygame.draw.rect(surface, color, rectangle)