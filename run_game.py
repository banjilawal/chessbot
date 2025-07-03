import pygame

from common.game_color import GameColor
from common.game_default import GameDefault
from model.board.board import Board
from view.board_view import BoardView

if __name__ == "__main__":
    board = Board(id=1)
    print(board.print())
    pygame.init()
    board_view = BoardView(board=board, cell_px=GameDefault.CELL_PX)

    # Sets the screen to be 800x600 pixels
    screen = pygame.display.set_mode(board_view.screen_dimension())

    # Clock to help control frame rate. We need this for drawing the screen and handle input
    clock = pygame.time.Clock()
    #
    # board = Board(id=1)
    # view = BoardView(board)
    #
    running = True
    while running:

    #     If any event from an input device sends a quit, ie mouse or kepybaard saying quit then stop running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    # Fills the screen with a color. This is the background color
        screen.fill(GameColor.GREEN.pygame_color)
        board_view.draw_board(screen)
    #     view.draw_board(screen)         # Draw the board and pieces

    # when itesms are drawn they are in a hidden surface stored in memory. We need to call flip to draw the
    # items on the screen. Thy are flipped from hidden screen to visible screen
        pygame.display.flip()
    # clock.tick() controls the frame rate. Its saying goe as fast as 60 FPS
        clock.tick(60)
    #
    pygame.quit()
