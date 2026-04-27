# src/operation/validation/square/operation.py

"""
Module: operation.validation.square.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import SquareNullException, SquareValidationException
from model import Square
from operation import Validator
from result import ValidationResult
from system import LoggingLevelRouter
from toolkit import SquareToolkit


class SquareValidator(Validator[Square]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Square instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(candidate: Any, toolkit: SquareToolkit) -> ValidationResult[Square]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "square_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: SquareToolkit,
    ) -> ValidationResult[Square]:
        """
        Verify the object is a Square that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate either null or not a Square
                    _   Coord check fails
                    -   A Board check fails
                    -   Identity check fails
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            toolkit: SquareToolkit
        Returns:
            ValidationResult[Square]
        Raises:
             SquareValidationException
        """
        method = f"{cls.__name__}.validate"
        
        if toolkit is None:
            toolkit = SquareToolkit()
        
        # Handle the case that, the candidate does not exist.
        validation_bootstrap_result = toolkit.validation_bootstrapper.validate(
            candidate=candidate,
            target_model=Square,
            null_exception=SquareNullException(),
        )
        if validation_bootstrap_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    ex=validation_bootstrap_result.exception,
                )
            )
        # --- Cast candidate to a Square for additional tests. ---#
        square = cast(Square, candidate)
        
        # Handle the case that, square.id or square.schema does not pass a validation check.
        identity_validation_result = toolkit.identity_service.validate_identity(
            id_candidate=square.id,
            name_candidate=square.name
        )
        if identity_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    ex=identity_validation_result.exception,
                )
            )
        # Handle the case that, square.coordis not safe.
        coord_validation_result = toolkit.coord_validator.validate(square.coord)
        if coord_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    ex=identity_validation_result.exception,
                )
            )
        # Handle the case that, square.board does not pass a validation check.
        board_validation_result = toolkit.board_validator.validate(square.board)
        if board_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    ex=board_validation_result.exception,
                )
            )
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
        board_validation_result = board_service.microservice.validator.validat(
            candidate=square.board
        )
        if board_validation_result.is_faiure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    mthd_rslt=SquareValidationException.MTHD_RSLT,
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
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    mthd_rslt=SquareValidationException.MTHD_RSLT,
                    ex=board_square_relation.exception
                )
            )
        # Handle the case that, the square belongs to a different board.
        if board_square_relation.does_not_exist:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    mthd_rslt=SquareValidationException.MTHD_RSLT,
                    ex=SquareOnDifferentBoardException(
                        msg=SquareOnDifferentBoardException.MSG,
                        err_code=SquareOnDifferentBoardException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the board has an expire link to the square.
        if board_square_relation.stale_link_exists:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    mthd_rslt=SquareValidationException.MTHD_RSLT,
                    ex=BoardOrphanSquareLinkException(
                        msg=BoardOrphanSquareLinkException.MSG,
                        err_code=BoardOrphanSquareLinkException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the square has not been added to the board's squares.
        if board_square_relation.registration_does_not_exist:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    mthd_rslt=SquareValidationException.MTHD_RSLT,
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
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    mthd_rslt=SquareValidationException.MTHD_RSLT,
                    ex=NullSquareException(
                        msg=NullSquareException.MSG,
                        err_code=NullSquareException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, SquareState):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationException(
                    cls_mthd=method,
                    op=SquareValidationException.OP,
                    msg=SquareValidationException.MSG,
                    err_code=SquareValidationException.ERR_CODE,
                    mthd_rslt=SquareValidationException.MTHD_RSLT,
                    ex=TypeError(
                        f"Expected type{SquareState.__name__}, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(cast(SquareState, candidate))
