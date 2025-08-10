from xml.sax.handler import feature_string_interning

from chess.creator.entity.builder.arena_builder import ArenaBuilder
from chess.geometry.coordinate.coordinate import Delta, Coordinate


def main():

     arena = ArenaBuilder.build()
     print(arena.chess_board)

     chess_piece = arena.chess_board.find_square_by_name("B2").occupant
     coord = chess_piece.coordinate_stack.current_coordinate()
     dest = Coordinate(row=(coord.row + 1), column=coord.column)
     print(f"\nCOORDS[origin:{coord} dest:{dest}]")
     print(f"\n{chess_piece}")
     rank = chess_piece.rank
     print(f"Rank:{rank}")

     dest_square =  arena.chess_board.find_square_by_coordinate(dest)
     print(f"dest square:{dest_square}")
     # if rank.walk.is_walkable(chess_piece=chess_piece, destination=dest):
     #      print("can walk")
     #      print(f" {chess_piece} advancing to to {dest} from {coord}")
     #      arena.chess_board.capture_square(chess_piece, dest)
     # else:
     #      print("cannot walk")
     # print(arena.chess_board)





if __name__ == "__main__":
    main()
