from typing import cast, Any

from chess.piece import NullPieceException
from chess.system import (
    COLUMN_SIZE, ChessException, IdValidator, ROW_SIZE, Validator, ValidationResult,
    LoggingLevelRouter
)
from chess.board import (
    Board, NullBoardException, BoardNullPieceListException, BoardNullSquareListException,
    InvalidBoardException
)


class BoardValidator(Validator[Board]):
    """
    # ROLE: Validation
  
    # RESPONSIBILITIES:
    1. Verify a candidate is a Board instance that can be used safely in the system.
  
    # PROVIDES:
      ValidationResult[Board] containing either:
            - On success: Board in payload.
            - On failure: Exception.
  
    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls, candidate: Any,
            id_validator: type[IdValidator] = IdValidator,
    ) -> ValidationResult[Board]:
        """
        # Action:
        Run checks verifying a candidate is a valid Board object meeting the minimum requirements
        for use in the system.
    
        # Parameters:
          * candidate (Any): Object to verify is a Board.
          * id_validator (type[IdValidator]): IdValidator runs sanity checks on the board's id
    
        # Returns:
          ValidationResult[Board] containing either:
                - On success: Board in payload.
                - On failure: Exception.
    
        # Raises:
            * TypeError
            * NullBoardException
            * BoardNullSquaresListException
            * BoardNullEnemiesDictException
            * BoardNullFriendsDictException
            * InvalidBoardException
        """
        method = "BoardValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullBoardException(f"{method} {NullBoardException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, Board):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected Board, got {type(candidate).__name__} instead")
                )
            
            board = cast(Board, candidate)
            
            id_validation = id_validator.validate(board.id)
            if not id_validation.is_failure():
                return ValidationResult.failure(id_validation.exception)
            
            if board.pieces is None:
                return ValidationResult.failure(
                    BoardNullPieceListException(
                        f"{method}: {BoardNullPieceListException.DEFAULT_MESSAGE}"
                    )
                )
            
            if board.squares is None:
                return ValidationResult.failure(
                    BoardNullSquareListException(
                        f"{method}: {BoardNullSquareListException.DEFAULT_MESSAGE}"
                    )
                )
            
            if len(board.squares) == ROW_SIZE * COLUMN_SIZE:
                return ValidationResult.failure(
                    NumberOfBoardSquaresOutBoundsException(
                        f"{method}: {NumberOfBoardSquaresOutBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult(payload=board)
        
        except Exception as e:
            return ValidationResult.failure(
                InvalidBoardException(f"{method}: {InvalidBoardException.DEFAULT_MESSAGE}", e)
            )
        
       
    @classmethod
    @LoggingLevelRouter.monitor
    def verify_piece_relates_to_board(
            cls,
            board_candidate: Any,
            piece_candidate: Any,
            piece_validator: type[PieceValidator] = PieceValidator,
    ) -> ValidationResult[(Board, Piece, Square)]:
        """
        # Action:
        """
        method = "BoardValidator.verify_piece_relates_to_board"
        
        try:
            piece_validation = piece_validator.
            if piece_validation.is_failure():
                return ValidationResult.failure(piece_validation.exception)
            
            piece = cast(Piece, piece_validation.payload)
            
            board_validation = cls.validate(board_candidate)
            if board_validation.is_failure():
                return ValidationResult.failure(board_validation.exception)
            
            board = cast(Board, board_validation.payload)
            
            if piece not in board.pieces:
                return ValidationResult.failure(
                    return ChessException
                )
            
            if board_candidate is None:
            
            if piece is None:
                return ValidationResult.failure(
                    NullPieceException(f"{method} {NullPieceException.DEFAULT_MESSAGE}")
                )
        except Exception as e:
            return ValidationResult.failure(
                InvalidBoardException(
                    f"{method}: {InvalidBoardException.DEFAULT_MESSAGE}", e
                )
            )

#
#
# def main():
#   person = CommanderBuilder.build(commander_id=id_emitter.person_id, visitor_name=RandomName.person())
#   team_name = TeamBuilder.build()
