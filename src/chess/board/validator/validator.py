# src/chess/board/validator/__init__.py

"""
Module: chess.board.validator.__init__
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""


from chess.board import Board
from chess.system import LoggingLevelRouter, Validator, ValidationResult


class BoardValidator(Validator[Board]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a Board instance is certified safe, reliable and consistent before use.
    2.  Provide the verification customer an exception detailing the contract violation if integrity assurance fails.

    # PARENT:
        *   Validator

    # PROVIDES:
        * BoardValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls, candidate: Any,
            id_validator: type[IdValidator] = IdValidator,
            square_validator: type[SquareValidator] = SquareValidator
    ) -> ValidationResult[Board]:
        """
        # Action:
        Use chained PieceValidator and SquareValidator to ensure a candidate is a valid DomainOrigin before
        the client can use it.

        # Parameters:
          * candidate (Any): Object to verify is a Domain.
          * piece_validator (type[PieceValidator]): Injected into number_bounds_validator.
          * number_bounds_validator (type[SquareValidator]): verifies the relationship between the
                Domain's owning Piece and Square.

        # Returns:
          ValidationResult[DomainOrigin] containing either:
                - On success: DomainOrigin in the payload.
                - On failure: Exception.

        # Raises:
            * TypeError
            * InvalidDomainOriginException
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
                    NumberOfBoardSquaresOutOfBoundsException(
                        f"{method}: {NumberOfBoardSquaresOutOfBoundsException.DEFAULT_MESSAGE}"
                    )
                )
            
            for square in board.squares:
                square_validation = square_validator.validate(square)
                if not square_validation.is_failure():
                    return ValidationResult.failure(square_validation.exception)
            
            return ValidationResult(payload=board)
        
        except Exception as e:
            return ValidationResult.failure(
                InvalidBoardException(f"{method}: {InvalidBoardException.DEFAULT_MESSAGE}", e)
            )
        
       
    @classmethod
    @LoggingLevelRouter.monitor
    def validate_piece_board_binding(
            cls,
            board_candidate: Any,
            piece_candidate: Any,
            board_search_context: BoardSearchContext=BoardSearchContext,
            piece_validator: type[PieceValidator] = PieceValidator,
            square_validator: type[SquareValidator] = SquareValidator,
            board_square_search: type[BoardSquareSearch] = BoardSquareSearch
    ) -> ValidationResult[(Board, Piece, Square)]:
        """
        # Action:
        """
        method = "BoardValidator.verify_piece_relates_to_board"
        
        try:
            piece_validation = piece_validator.validate_piece_is_actionable(piece_candidate)
            if piece_validation.is_failure():
                return ValidationResult.failure(piece_validation.exception)
            
            piece = cast(Piece, piece_validation.payload)
            
            board_validation = cls.validate(board_candidate)
            if board_validation.is_failure():
                return ValidationResult.failure(board_validation.exception)
            
            board = cast(Board, board_validation.payload)
            
            if piece not in board.pieces:
                return ValidationResult.failure(
                    PieceNotOnBoardException(
                        f"{method}: {PieceNotOnBoardException.DEFAULT_MESSAGE}"
                    )
                )
            
            square_search_result = board_square_search.find(board=board, piece)
            
            
            
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
#   person = PlayerAgentBuilder.builder(commander_id=id_emitter.person_id, visitor_name=RandomName.person())
#   team_name = TeamBuilder.builder()
