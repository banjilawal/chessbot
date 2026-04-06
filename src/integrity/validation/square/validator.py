# src/integrity/validation/square/validator.py

"""
Module: integrity.validation.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class SquareValidator(Validator[Square]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a Square instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    Super Class:
        *   Validator

    Provides:


    # INHERITED ATTRIBUTES:
    None

    Attributes:
    None

    # LOCAL METHODS:
        *   validate(
                rank: Any,
                board_service: BoardService = BoardService(),
                coord_service: CoordService = CoordService(),
                identity_service: IdentityService = IdentityService()
            ) -> ValidationResult[Square]
            
        *   validate_square_state(rank: Any) -> ValidationResult[SquareState]
        *   verify_is_square_dataset(rank: Any) -> ValidationResult[List[Square]]

    # INHERITED METHODS:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            board_service: BoardService = BoardService(),
            coord_service: CoordService = CoordService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Square]:
        """
        # ACTION:
            1.  Send an exception chain in the ValidationResult if:
                    -   The rank is null
                    -   The rank is not a Square
                    -   The id and schema are not certified as safe.
                    -   The coord does not pass a validation check.
                    -   The board does not pass a validation check.
                    -   There is no bidirectional relationship between the board and square.
            2.  Otherwise, send the succes result.
        Args:
            candidate: Any
            board_service: BoardService
            coord_service: CoordService
            identity_service: IdentityService
        Returns:
            ValidationResult[Square]
        Raises:
            TypeError
            NullSquareException
            SquareValidationException
        """
        method = "SquareValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=NullSquareException(
                        msg=NullSquareException.MSG,
                        err_code=NullSquareException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, Square):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected Square, but, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast rank to a Square for additional tests. ---#
        square = cast(Square, candidate)
        
        # Handle the case that, square.id or square.schema does not pass a validation check.
        identity_validation_result = identity_service.validate_identity(
            id_candidate=square.id,
            name_candidate=square.name
        )
        if identity_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=identity_validation_result.exception
                )
            )
        # Handle the case that, square.coordis not safe.
        coord_validation_result = coord_service.validator.validate(square.coord)
        if coord_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=coord_validation_result.exception
                )
            )
        # Handle the case that, square.board safety and relation validation fails.
        board_test_results = cls._run_board_tests(square=square, board_service=board_service)
        if board_test_results.is_failure:
            return board_test_results
        
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(square)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_board_tests(
            cls,
            square: Square,
            board_service: BoardService = BoardService()
    ) -> ValidationResult[Square]:
        """
        Tests that the token belongs to a secure board.
        
        Action:
            1.  Send an exception chain in the ValidationResult If:
                    -   The board is not safe.
                    -   The square and the board do not have bidirectional relationship.
            2.  Otherwise, send the success result.
        Args:
            square: Square
            board_service: BoardService
        Returns:
            ValidationResult[int]
        Raises:
            SquareValidationException
            SquareOnDifferentBoardException
            SquareBoardRegisteredException
        """
        method = f"{cls.__name__}._run_board_tests"
        
        # Handle the case that, the square's board is nnt certified as safe.
        board_validation_result = board_service.service.validator.validat(
            candidate=square.board
        )
        if board_validation_result.is_faiure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=board_validation_result.exception
                )
            )
        
        # --- ServiceRequest an analysis of the relation between the board and square. ---#
        board_square_relation = board_service.board_square_relation_analyzer.search_service(
            candidate_primary=square.board,
            candidate_satellite=square,
        )

        # Handle the case that, the analyzer did not complete the request.
        if board_square_relation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=board_square_relation.exception
                )
            )
        # Handle the case that, the square belongs to a different board.
        if board_square_relation.does_not_exist:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=SquareOnDifferentBoardException(
                        msg=SquareOnDifferentBoardException.MSG,
                        err_code=SquareOnDifferentBoardException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the board has an expire link to the square.
        if board_square_relation.stale_link_exists:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=BoardOrphanSquareLinkException(
                        msg=BoardOrphanSquareLinkException.MSG,
                        err_code=BoardOrphanSquareLinkException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the square has not been added to the board's squares.
        if board_square_relation.registration_does_not_exist:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=SquareBoardRegisteredException(
                        msg=SquareBoardRegisteredException.MSG,
                        err_code=SquareBoardRegisteredException.ERR_CODE,
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(square)
    
    @classmethod
    def validate_square_state(cls, candidate: Any) -> ValidationResult[SquareState]:
        """
        Tests if the rank is a SquareState instance.
        
        Action:
            1.  Send an exception chain in the ValidationResult if:
                    -   The rank is null.
                    -   The rank has the wrong type.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[SquareState]
        Raises:
            TypeError
            NullSquareStateException
            SquareValidationException
        """
        method = f"{cls.__name__}.validate_square_state"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=NullSquareException(
                        msg=NullSquareException.MSG,
                        err_code=NullSquareException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SquareState):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    rslt_type=SquareValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected type{SquareState.__name__}, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(cast(SquareState, candidate))
