class SquareComparator:
    def __init__(self, piece):
        self.piece = piece
    def compare(self, square1, square2):
        if self.piece.color == 'white':
            return square1.y - square2.y
        else:
            return square2.y - square1.y