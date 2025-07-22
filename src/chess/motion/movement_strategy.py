


class PawnMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement pawn-specific motion logic
        return False


class KnightMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement knight's L-shaped motion
        return False


class BishopMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement bishop's diagonal motion
        return False


class CastleMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement rook's straight-line motion
        return False


class QueenMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement queen's combined rook + bishop motion
        return False


class KingMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement king's single-step any direction, and castling
        return False