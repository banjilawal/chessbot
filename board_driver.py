from common.generator import Generator

if __name__ == "__main__":
    generator = Generator()
    board = generator.board()
    for cell in board.cells:
        if cell.occupnat is not None:
            print("cell_id:", cell.id, " ")