# src/logic/rank/validation/validator.py

"""
Module: logic.rank.validation.validator
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from __future__ import annotations
from typing import cast, Any

from logic.coord import Coord, NullRankException
from logic.coord.service.operation.validation.exception.transaction import RankValidationException
from logic.rank import (
    Bishop, BishopPersonaMismatchException, King, KingPersonaMismatchException, Knight, KnightPersonaMismatchException,
    Pawn, PawnPersonaMismatchException, Queen,
    QueenPersonaMismatchException,
    Rank, RankValidationRouteException, Rook, RookPersonaMismatchException
)
from logic.system import (
    NUMBER_OF_ROWS, Validator, ValidationResult, LoggingLevelRouter, NumberValidator
)


class RankValidator(Validator[Coord]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Coord instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    cls,
                    rank: Any,
                    workers: RankIntegrityWorkers,
            ) -> ValidationResult[Rank]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            workers: RankIntegrityWorkers = RankIntegrityWorkers(),
    ) -> ValidationResult[Rank]:
        """
        Verify the rank is a Rank that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult
                    -   the rank does not exist.
                    -   the rank is not a Rank.
                    -   Any integrity worker raises a failed test.
            2.  Otherwise, after the rank is cast to a Rank, send the success result.
        Args:
            candidate: Any
            workers: RankIntegrityWorkers
        Returns:
            ValidationResult[Rank]
        Raises:
            TypeError
            NullRankException
            RankValidationException
        """
        method = f"{cls.__name__}.build"
        
        # Handle the case that, the rank does not exist.
        if candidate is None:
            # Return the exception on failure.
            return ValidationResult.failure(
                RankValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=RankValidationException.OP,
                    msg=RankValidationException.MSG,
                    err_code=RankValidationException.ERR_CODE,
                    rslt_type=RankValidationException.RSLT_TYPE,
                    ex=NullRankException(
                        msg=NullRankException.MSG,
                        err_code=NullRankException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the rank is the wrong type.
        if not isinstance(candidate, Rank):
            # Return the exception on failure.
            return ValidationResult.failure(
                RankValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=RankValidationException.OP,
                    msg=RankValidationException.MSG,
                    err_code=RankValidationException.ERR_CODE,
                    rslt_type=RankValidationException.RSLT_TYPE,
                    ex=TypeError(
                        f"Expected a Rank, got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast rank to a Coord for additional tests ---#
        rank = cast(Rank, candidate)
        
        # Handle the case that, the rank's id is not safe.
        id_validation_result = workers.identity_service.validate_id(rank.id)
        if id_validation_result.is_failure:
            # Return the exception on failure.
            return ValidationResult.failure(
                RankValidationException(
                    mthd=method,
                    title=cls.__name__,
                    op=RankValidationException.OP,
                    msg=RankValidationException.MSG,
                    err_code=RankValidationException.ERR_CODE,
                    rslt_type=RankValidationException.RSLT_TYPE,
                    ex=id_validation_result.exception,
                )
            )

        # --- Handle the case that, a King has the wrong Persona. ---#
        if isinstance(rank, King):
            if rank.persona != workers.persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=RankValidationException.OP,
                        msg=RankValidationException.MSG,
                        err_code=RankValidationException.ERR_CODE,
                        rslt_type=RankValidationException.RSLT_TYPE,
                        ex=KingPersonaMismatchException(
                            val=rank.persona,
                            var="rank.persona",
                            msg=KingPersonaMismatchException.MSG,
                            err_code=KingPersonaMismatchException.ERR_CODE,
                        ),
                    )
                )
            # --- Otherwise return the work product. ---#
            return ValidationResult.success(rank)
        
        # --- Handle the case that, a Pawn has the wrong Persona. ---#
        if isinstance(rank, Pawn):
            if rank.persona != workers.persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=RankValidationException.OP,
                        msg=RankValidationException.MSG,
                        err_code=RankValidationException.ERR_CODE,
                        rslt_type=RankValidationException.RSLT_TYPE,
                        ex=PawnPersonaMismatchException(
                            val=rank.persona,
                            var="rank.persona",
                            msg=PawnPersonaMismatchException.MSG,
                            err_code=PawnPersonaMismatchException.ERR_CODE,
                        ),
                    )
                )
            # --- Otherwise return the work product. ---#
            return ValidationResult.success(rank)
        
        # --- Handle the case that, a Knight has the wrong Persona. ---#
        if isinstance(rank, Knight):
            if rank.persona != workers.persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=RankValidationException.OP,
                        msg=RankValidationException.MSG,
                        err_code=RankValidationException.ERR_CODE,
                        rslt_type=RankValidationException.RSLT_TYPE,
                        ex=KnightPersonaMismatchException(
                            val=rank.persona,
                            var="rank.persona",
                            msg=KnightPersonaMismatchException.MSG,
                            err_code=KnightPersonaMismatchException.ERR_CODE,
                        ),
                    )
                )
            # --- Otherwise return the work product. ---#
            return ValidationResult.success(rank)
        
        # --- Handle the case that, a Bishop has the wrong Persona. ---#
        if isinstance(rank, Bishop):
            if rank.persona != workers.persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=RankValidationException.OP,
                        msg=RankValidationException.MSG,
                        err_code=RankValidationException.ERR_CODE,
                        rslt_type=RankValidationException.RSLT_TYPE,
                        ex=BishopPersonaMismatchException(
                            val=rank.persona,
                            var="rank.persona",
                            msg=BishopPersonaMismatchException.MSG,
                            err_code=BishopPersonaMismatchException.ERR_CODE,
                        ),
                    )
                )
            # --- Otherwise return the work product. ---#
            return ValidationResult.success(rank)
        
        # --- Handle the case that, a Bishop has the wrong Persona. ---#
        if isinstance(rank, Rook):
            if rank.persona != workers.persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=RankValidationException.OP,
                        msg=RankValidationException.MSG,
                        err_code=RankValidationException.ERR_CODE,
                        rslt_type=RankValidationException.RSLT_TYPE,
                        ex=RookPersonaMismatchException(
                            val=rank.persona,
                            var="rank.persona",
                            msg=RookPersonaMismatchException.MSG,
                            err_code=RookPersonaMismatchException.ERR_CODE,
                        ),
                    )
                )
            # --- Otherwise return the work product. ---#
            return ValidationResult.success(rank)
        
        # --- Handle the case that, a Bishop has the wrong Persona. ---#
        if isinstance(rank, Queen):
            if rank.persona != workers.persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankValidationException(
                        mthd=method,
                        title=cls.__name__,
                        op=RankValidationException.OP,
                        msg=RankValidationException.MSG,
                        err_code=RankValidationException.ERR_CODE,
                        rslt_type=RankValidationException.RSLT_TYPE,
                        ex=QueenPersonaMismatchException(
                            val=rank.persona,
                            var="rank.persona",
                            msg=QueenPersonaMismatchException.MSG,
                            err_code=QueenPersonaMismatchException.ERR_CODE,
                        ),
                    )
                )
            # --- Otherwise return the work product. ---#
            return ValidationResult.success(rank)
        
        # Handle the case that, the there is no persona validator logic for the rank.
        return ValidationResult.failure(
            RankValidationException(
                mthd=method,
                title=cls.__name__,
                op=RankValidationException.OP,
                msg=RankValidationException.MSG,
                err_code=RankValidationException.ERR_CODE,
                rslt_type=RankValidationException.RSLT_TYPE,
                ex=RankValidationRouteException(
                    val=rank,
                    var=rank.persona.name,
                    msg=RankValidationException.MSG,
                    err_code=RankValidationException.ERR_CODE,
                )
            )
        )
 

