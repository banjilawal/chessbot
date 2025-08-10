from xml.sax.handler import feature_string_interning

from chess.creator.entity.builder.arena_builder import ArenaBuilder
from chess.geometry.coordinate.coordinate import Delta, Coordinate


def main():

     arena = ArenaBuilder.build()
     print(arena.chess_board)

     chess_piece = arena.chess_board.find_square_by_name("B2").occupant
     coord = chess_piece.current_coordinate
     dest = Coordinate(coord.row + 1, coord.column +1)
     print(coord, dest)
     print(chess_piece)
     rank = chess_piece.rank
     print(rank)
     print(rank.walk.is_walkable(chess_piece=chess_piece, destination=dest))





if __name__ == "__main__":
    main()
