import pygame

from model.board.board import Board


class BoardView:
    board: Board
    cell_px: int

    def __init__(self, board: Board, cell_px: int):
        self.board = board
        self.cell_px = cell_px

    def draw(self, surface: pygame.Surface):
        """Draw the board on the given surface."""
        for row in range(self.board.height):
            for col in range(self.board.width):
                cell = self.board.get_cell(row, col)
                rect = pygame.Rect(col * self.cell_px, row * self.cell_px, self.cell_px, self.cell_px)
                if cell.is_occupied():
                    color = cell.occupant.color
                else:
                    color = (255, 255, 255)