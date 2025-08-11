
from chess.creator.entity.builder.arena_builder import ArenaBuilder
from chess.geometry.coordinate.coordinate import Delta, Coordinate


def main():

     arena = ArenaBuilder.build()
     print(arena.chess_board)

     bp2 = arena.chess_board.find_square_by_name("B2").occupant
     bp2_origin = bp2.coordinate_stack.current_coordinate()
     bp2_dest = Coordinate(row=(bp2_origin.row + 2), column=bp2_origin.column)
     print(f"\nCOORDS[origin:{bp2_origin} dest:{bp2_dest}]")
     print(f"\n{bp2}")
     rank = bp2.rank
     print(f"Rank:{rank}")

     bp2_dest_square =  arena.chess_board.find_square_by_coordinate(bp2_dest)
     print(f"dest square:{bp2_dest_square}")
     if rank.walk.is_walkable(chess_piece=bp2, destination=bp2_dest):
          print(f"can walk to {bp2_dest}")
     #      print(f" {bp2} advancing to to {dest} from {coord}")
          arena.chess_board.capture_square(bp2, bp2_dest)
     else:
          print(f"cannot walk to {bp2_dest} from {bp2_origin}")
     print(arena.chess_board)

     wp3 = arena.chess_board.find_square_by_name("c7").occupant
     wp3_origin = wp3.coordinate_stack.current_coordinate()
     wp3_dest = Coordinate(row=(wp3_origin.row - 2), column=wp3_origin.column)
     print(f"\nCOORDS[origin:{wp3_origin} dest:{wp3_dest}]")
     print(f"\n{wp3}")
     rank = wp3.rank
     print(f"Rank:{rank}")
     if rank.walk.is_walkable(chess_piece=wp3, destination=wp3_dest):
          print(f"can walk to {wp3_dest}")
          arena.chess_board.capture_square(wp3, wp3_dest)
     else:
          print(f"cannot walk to {wp3_dest} from {wp3_origin}")
     print(arena.chess_board)


if __name__ == "__main__":
     main()


