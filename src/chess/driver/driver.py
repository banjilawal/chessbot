from chess.factory.grid_builder import GridBuilder


def main():
    from chess.geometry.board import Board
    board = Board(grid=GridBuilder.build())
    print(board.grid)




if __name__ == "__main__":
    main()
