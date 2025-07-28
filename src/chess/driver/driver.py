from chess.factory.grid_builder import GridBuilder
from chess.factory.rank_factory import RankFactory
from chess.geometry.board import Board

def main():

    board = Board(grid=GridBuilder.build())
    ranks = RankFactory.run_factory()






if __name__ == "__main__":
    main()
