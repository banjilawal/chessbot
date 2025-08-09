from chess.creator.service.board_controller_builder import BoardControllerBuilder
from chess.field import board_controller
from chess.geometry.coordinate.coordinate import Coordinate


def main():

     board = BoardControllerBuilder.build()
     square = board.square_service.find_square_by_id(58)
     print("searched by id", square)

     square = board.square_service.find_square_by_coordinate(Coordinate(1, 1))
     print("searched by coordinate", square)

     square = board.square_service.find_square_by_name("b2")
     print("searched by name:", square)

     for s in board.square_service.occupied_squares():
         print(s.__str__())

     print(board.square_service.squares_to_string())


     chess_piece = board.team_service.find_chess_piece_by_id(23)
     print("\nFound by id", chess_piece)
     chess_piece = board.team_service.find_chess_piece_by_name("bp6")
     print("Found by name", chess_piece)

     square = board.square_service.find_square_by_name("a2")
     print("Found by name", square)
     chess_piece = square.occupant
     print("a2 occupant", chess_piece)
     print("a2 occupant", chess_piece.name)

     new_square = board.square_service.find_square_by_name("a3")
     print(chess_piece.name, "requesting move to", new_square)
     chess_piece.forward_move_request(destination=new_square.coordinate)
     # for s in board_controller.map_service.squares():
     #     print(board.__str__(), "\n")




if __name__ == "__main__":
    main()
