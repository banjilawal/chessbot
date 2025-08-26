import traceback

from chess.creator.entity.builder.arena_builder import ArenaBuilder
from chess.geometry.coordinate.coord import Offset, Coordinate


def main():

     arena = ArenaBuilder.build()
     print(arena.chess_board)

     bp2 = arena.chess_board.find_square_by_name("B2").occupant
     bp2_origin = bp2.positions.current_coordinate()
     bp2_dest = Coordinate(row=(bp2_origin.row + 1), column=bp2_origin.column)
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
     wp3_origin = wp3.positions.current_coordinate()
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
     # print(arena.chess_board)

     origin = bp2.positions.current_coordinate()
     print(f"bp2.coord {origin}\n ")
     bp2_dest = Coordinate(row=(origin.row + 1), column=origin.column)
     print(f"dest square:{bp2_dest_square}")
     if rank.walk.is_walkable(chess_piece=bp2, destination=bp2_dest):
          print(f"can walk to {bp2_dest}")
          #      print(f" {bp2} advancing to to {dest} from {coord}")
          arena.chess_board.capture_square(bp2, bp2_dest)
     else:
          print(f"cannot walk to {bp2_dest} from {bp2_origin}")

     wp3_origin = wp3.positions.current_coordinate()
     wp3_dest = Coordinate(row= wp3_origin.row - 1, column=wp3_origin.column + 1)
     if rank.walk.is_walkable(chess_piece=wp3, destination=wp3_dest):
          print(f"can walk to {wp3_dest}")
          arena.chess_board.capture_square(wp3, wp3_dest)
     else:
          print(f"cannot walk to {wp3_dest} from {wp3_origin}")
     print(arena.chess_board)
     print(f"bp")

     bp3 = arena.chess_board.find_square_by_name("C2").occupant
     bp3_current = bp3.positions.current_coordinate()
     bp3_dest = Coordinate(row=bp3_current.row +1, column=bp3_current.column)
     arena.chess_board.capture_square(bp3, bp3_dest)

     wp3_origin = wp3.positions.current_coordinate()
     wp3_dest = Coordinate(row= wp3_origin.row - 1, column=wp3_origin.column + 1)
     if rank.walk.is_walkable(chess_piece=wp3, destination=wp3_dest):
          print(f"can walk to {wp3_dest}")
          arena.chess_board.capture_square(wp3, wp3_dest)
     else:
          print(f"cannot walk to {wp3_dest} from {wp3_origin}")
     print(f"\n{arena.chess_board}")

     print(f"\nwp3={wp3}")
     print(f"\nbp3={bp3}")



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n🔴 Exception caught in main:")
        traceback.print_exc()
        if e.__cause__:
            print(f"\n🔍 Original cause: {type(e.__cause__).__name__} - {e.__cause__}")



