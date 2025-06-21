from itertools import count
from typing import List

import pygame

from game.common.game_constant import GameConstant
from game.exception.exception import InvalidIdError, InvalidNumberOfRowsError, InvalidNumberOfColumnsError
from game.board.board_square import GameBoardSquare

from dataclasses import dataclass
from typing import Optional

from game.figure.game_figure import GameFigure

@dataclass
class GameBoard:
    MINIMUM_NUMBER_OF_ROWS = 2
    MINIMUM_NUMBER_OF_COLUMNS = 2
    id: int
    number_of_rows: int
    number_of_columns: int
    figures: Optional[List[GameFigure]] = None

    # Drawing constants as class attributes
    SQUARE_SIZE_IN_PIXELS = 40

    # Pygame colors (defined as RGB tuples)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY_LIGHT = (200, 200, 200)
    GRAY_DARK = (150, 150, 150)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    def __post_init__(self):
        if self.id < GameConstant.MINIMUM_ID:
            raise InvalidIdError("GameBoard id below minimum value.")
        if self.number_of_rows < GameBoard.MINIMUM_NUMBER_OF_ROWS:
            raise InvalidNumberOfRowsError("GameBoard number_of_rows below minimum value.")
        if self.number_of_columns < GameBoard.MINIMUM_NUMBER_OF_COLUMNS:
            raise InvalidNumberOfColumnsError("GameBoard number_of_columns below minimum value.")

        index = count(1)
        self._squares = [
            [
                GameBoardSquare(_id=next(index), _row=row, _column=column)
                for column in range(self.number_of_columns)
            ]
            for row in range(self.number_of_rows)
        ]

    @property
    def columns(self):
        return self.number_of_columns

    @property
    def squares(self):
        return self._squares

    def area(self):
        return self.number_of_rows * self.number_of_columns

    def draw(self, screen):
        square_size = GameBoard.SQUARE_SIZE_IN_PIXELS
        light_color = GameBoard.GRAY_LIGHT
        dark_color = GameBoard.GRAY_DARK
        border_color = GameBoard.BLACK

        for row_index in range(self.number_of_rows):
            for col_index in range(self.number_of_columns):
                left = col_index * square_size
                top = row_index * square_size

                if (row_index + col_index) % 2 == 0:
                    color = light_color
                else:
                    color = dark_color

                pygame.draw.rect(screen, color, (left, top, square_size, square_size))
                pygame.draw.rect(screen, border_color, (left, top, square_size, square_size), 1)

    def print_grid(self): # Keeping your original method for text-based printing
        for row in self._squares:
            print("".join("+---" for _ in row) + "+")
            print("".join("|   " for _ in row) + "|")
        print("".join("+---" for _ in self._squares[0]) + "+")

# def main(num_rows: int = 8, num_columns:int = 8, square_width_pixels:int = 400):



# --- Main game logic wrapped in if __name__ == "__main__": ---
if __name__ == "__main__":
    pygame.init()


    BOARD_ROWS = 11
    BOARD_COLS = 8

    SQUARE_SIZE = GameBoard.SQUARE_SIZE_IN_PIXELS

    SCREEN_WIDTH = BOARD_COLS * SQUARE_SIZE
    SCREEN_HEIGHT = BOARD_ROWS * SQUARE_SIZE


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # pygame.display.set_caption("My Pygame Game Board") # Set the window title

    my_board = GameBoard(id=1, number_of_rows=BOARD_ROWS, number_of_columns=BOARD_COLS)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(GameBoard.WHITE)
        my_board.draw(screen)
        pygame.display.flip()
    pygame.quit()