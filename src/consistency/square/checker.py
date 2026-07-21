# src/consistency/square/consistency.py

"""
Module: consistency.square.checker
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from controller import WorkerRegistryController
from err import SquareConsistencyCheckerException
from model import Square
from chooser import SquareCarrier
from err.root import SquareRootCertifier
from result import ValidationResult
from util import LoggingLevelRouter
from consistency import  ConsistencyChecker


class SquareConsistencyChecker(ConsistencyChecker[Square]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Square instance is certified safe, reliable and consistent before use.

    Attributes:
        root_certifier: SquareRootCertifier
    Provides:
        -   def validate(candidate: Any, toolkit: SquareToolkit) -> ValidationResult[Square]:

    Super Class:
        ConsistencyChecker
    """
    
    
    def __init__(
            self,
            root_certifier: SquareRootCertifier = SquareRootCertifier(),
    ):
        """
        Args:
            root_certifier: SquareRootCertifier
        """
        super().__init__(root_certifier=root_certifier)
        
    @property
    def root_certifier(self) -> SquareRootCertifier:
        return cast(SquareRootCertifier, self.root_certifier)

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
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
        Returns:
            ValidationResult[Square]
        Raises:
             SquareConsistencyCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        bootstrap = self.root_certifier.toolkit.priming_consistency.execute(
            target_model=self.root_certifier.toolkit.model,
            model_null_exception=self.root_certifier.toolkit.null_exception,
        )
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareConsistencyCheckerException.MSG,
                    err_code=SquareConsistencyCheckerException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        root_certification = self.root_certifier.execute(
            candidate=SquareCarrier(model=bootstrap.payload)
        )
        if root_certification.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareConsistencyCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareConsistencyCheckerException.MSG,
                    err_code=SquareConsistencyCheckerException.ERR_CODE,
                    ex=root_certification.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return root_certification
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_board_tests(
            cls,
            square: Square,
            board_service: BoardService = BoardService()
    ) -> ValidationResult[Square]:
        """
        Tests that the Square belongs to a secure board.
        
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
            SquareConsistencyCheckerException
            SquareOnDifferentBoardException
            SquareBoardRegisteredException
        """
        method = f"{self.__class__.__name__}._run_board_tests"
        
        # Handle the case that, the square's board is nnt certified as safe.
        board_consistency_result = board_service.microservice.run.validat(
            candidate=square.board
        )
        if board_consistency_result.is_faiure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareConsistencyCheckerException(
                    cls_mthd=method,
                    op=SquareConsistencyCheckerException.OP,
                    msg=SquareConsistencyCheckerException.MSG,
                    err_code=SquareConsistencyCheckerException.ERR_CODE,
                    mthd_rslt_type=SquareConsistencyCheckerException.MTHD_RSLT,
                    ex=board_consistency_result.exception
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
                SquareConsistencyCheckerException(
                    cls_mthd=method,
                    op=SquareConsistencyCheckerException.OP,
                    msg=SquareConsistencyCheckerException.MSG,
                    err_code=SquareConsistencyCheckerException.ERR_CODE,
                    mthd_rslt_type=SquareConsistencyCheckerException.MTHD_RSLT,
                    ex=board_square_relation.exception
                )
            )
        # Handle the case that, the square belongs to a different board.
        if board_square_relation.does_not_exist:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareConsistencyCheckerException(
                    cls_mthd=method,
                    op=SquareConsistencyCheckerException.OP,
                    msg=SquareConsistencyCheckerException.MSG,
                    err_code=SquareConsistencyCheckerException.ERR_CODE,
                    mthd_rslt_type=SquareConsistencyCheckerException.MTHD_RSLT,
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
                SquareConsistencyCheckerException(
                    cls_mthd=method,
                    op=SquareConsistencyCheckerException.OP,
                    msg=SquareConsistencyCheckerException.MSG,
                    err_code=SquareConsistencyCheckerException.ERR_CODE,
                    mthd_rslt_type=SquareConsistencyCheckerException.MTHD_RSLT,
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
                SquareConsistencyCheckerException(
                    cls_mthd=method,
                    op=SquareConsistencyCheckerException.OP,
                    msg=SquareConsistencyCheckerException.MSG,
                    err_code=SquareConsistencyCheckerException.ERR_CODE,
                    mthd_rslt_type=SquareConsistencyCheckerException.MTHD_RSLT,
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
            SquareConsistencyCheckerException
        """
        method = f"{self.__class__.__name__}.execute_square_state"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareConsistencyCheckerException(
                    cls_mthd=method,
                    op=SquareConsistencyCheckerException.OP,
                    msg=SquareConsistencyCheckerException.MSG,
                    err_code=SquareConsistencyCheckerException.ERR_CODE,
                    mthd_rslt_type=SquareConsistencyCheckerException.MTHD_RSLT,
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
                SquareConsistencyCheckerException(
                    cls_mthd=method,
                    op=SquareConsistencyCheckerException.OP,
                    msg=SquareConsistencyCheckerException.MSG,
                    err_code=SquareConsistencyCheckerException.ERR_CODE,
                    mthd_rslt_type=SquareConsistencyCheckerException.MTHD_RSLT,
                    ex=TypeError(
                        f"Expected type{SquareState.__name__}, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(cast(SquareState, candidate))

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=SquareConsistency)