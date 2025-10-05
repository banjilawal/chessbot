import pygame.time

from chess.creator.entity.builder.arena_builder import ArenaBuilder
from chess.screen import GameDisplay
from config.logging_setup import init_logging



def main():
  """Your exact requested structure"""
  logger = init_logging() # Explicit logging start

  try:
    logger.info("Starting arena initialization")
    arena = ArenaBuilder.build()
    print(arena.chess_board)
    visualizer = GameDisplay(
      chess_board=arena.chess_board,
      cell_px=CELL_PX,
      border_px=BORDER_PX
    )

    clock = pygame.time.Clock()
    frame_count = 0

    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          visualizer.handle_mouse_down(event)
        elif event.type == pygame.MOUSEBUTTONUP:
          visualizer.handle_mouse_up(event)
        elif event.type == pygame.MOUSEMOTION:
          visualizer.handle_mouse_motion(event)
      visualizer.update_display()
      clock.tick(60)
    # launch_game(arena)

  except Exception as e:
    logger.critical(f"Game failed: {e}", exc_info=True)
    raise
  finally:
    logger.info("Game session ended")



if __name__ == "__main__":
  main() # Clean entry point