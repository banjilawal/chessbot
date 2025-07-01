from model.board.board import Board
from view.board_view import BoardView

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Construct your game board model
board = Board(...)  # Initialize as per your logic
view = BoardView(board)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # Clear screen
    view.draw(screen)         # Draw the board and pieces
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
