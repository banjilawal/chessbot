from chess.creator.service.board_controller_builder import BoardControllerBuilder


def main():
     board_controller = BoardControllerBuilder.build()
     board_controller.square_service.squares_to_string()


if __name__ == "__main__":
    main()
