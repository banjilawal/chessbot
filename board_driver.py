from common.generator import Generator
from strategy.horizontal_movement_strategy import HorizontalMovementStrategy

if __name__ == "__main__":
    board = Generator.board()
    movers = Generator.horizontal_movers(max_height=12, count=12)
    for mover in movers:
        board.add_horizontal_mover(mover)
    for cell in board.occupied_cells():
        print(cell)


    mover = board.random_mover()
    print(mover)

    movement_manager = HorizontalMovementStrategy