import pygame

from src.common.dimension import Dimension
from src.common.grid_entity_generator import GridEntityGenerator
from model.board import Board
from model.crate import Crate

if __name__ == "__main__":
    board = Board(dimension=Dimension(length=11, height=11))


    max_length = board.dimension.length % 2 + 1
    max_height = board.dimension.height % 2 + 1
    board.add_boulders(GridEntityGenerator().generate_boulders(max_length=2, max_height=3, count=9))
    board.place_boulders_randomly()

    board.add_ladders(GridEntityGenerator().generate_ladders(max_height=max_height, count=9))
    board.place_ladders_randomly()
    print(board.print())

    for boulder in board.vaults:
        boulder.print_cells()
    pygame.init()

    cell_px = 80  # Or use GameDefault.CELL_PX if you prefer
    width = board.dimension.length * cell_px
    height = board.dimension.height * cell_px

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Podscape!!")
    clock = pygame.time.Clock()

    color1 = (220, 220, 220)  # Light
    color2 = (60, 60, 60)     # Dark
    boulder_color = (0, 200, 0)  # Green
    padding_color = (100, 100, 100)  # Gray
    cream = (255, 253, 208)
    khaki = (240, 230, 140)
    light_gray =  (192, 192, 192)
    dark_gray = (64, 64, 64)
    very_light_gray = (211, 211, 211)
    slate_gray = (112, 128, 144)
    blue = (0, 0, 255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ladder_line_width = 2

        # 1. Draw base grid
        for row_idx, row in enumerate(board.cells):
            for col_idx, cell in enumerate(row):
                x = col_idx * cell_px
                y = row_idx * cell_px
                color = cream if (row_idx + col_idx) % 2 == 0 else khaki
                pygame.draw.rect(screen, color, (x, y, cell_px, cell_px))

        # 2. Draw vaults (gray square + inner border)
        for boulder in board.vaults:
            if boulder.cells:
                for row in boulder.cells:
                    for cell in row:
                        x = cell.coordinate.column * cell_px
                        y = cell.coordinate.row * cell_px
                        pygame.draw.rect(screen, light_gray, (x, y, cell_px, cell_px))  # main fill
                        pygame.draw.rect(screen, padding_color, (x + 1, y + 1, cell_px - 2, cell_px - 2),
                                         width=2)  # border

        # 3. Draw crates on top (only blue lines)
        for ladder in board.crates:
            if isinstance(ladder, Crate) and ladder.cells:
                for row in ladder.cells:
                    for cell in row:
                        x = cell.coordinate.column * cell_px
                        y = cell.coordinate.row * cell_px

                        # Left vertical border (side rail)
                        pygame.draw.line(
                            screen,
                            blue,
                            (x + 3, y),
                            (x + 3, y + cell_px),
                            2
                        )

                        # Right vertical border (side rail)
                        pygame.draw.line(
                            screen,
                            blue,
                            (x + cell_px - 4, y),
                            (x + cell_px - 4, y + cell_px),
                            2
                        )

                        # Draw ladder rungs as horizontal blue lines with gaps
                        rung_y = y
                        while rung_y < y + cell_px - 4:
                            pygame.draw.line(
                                screen,
                                blue,
                                (x + 4, rung_y),  # start 4 px in from the left
                                (x + cell_px - 4, rung_y),  # end 4 px before the right
                                2  # line thickness
                            )
                            rung_y += 30


        pygame.display.flip()
        clock.tick(60)
    pygame.quit()