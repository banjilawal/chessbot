# src/tool/rank__init__.py

"""
Module: tool.rank.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from microservice import PersonaService
from model import Rank
from result import ValidationResult
from system import LoggingLevelRouter

# =========== RANK PACKAGE ===========#

# Packages

# Modules

from __future__ import annotations


class RankPersonaValidator(Validator[Rank]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a Rank has the correct persona.

    Attributes:

    Provides:
        -   def validate(
                    cls,
                    rank: Any,
                    persona_service: PersonaService,
            ) -> ValidationResult[Rank]:

    Super Class:
        Validator
        
    Notes:
        -   Assumes the rank param has already been validated. Should only
            be called inside RankValidator.
            
        IntegrityWorker Responsibilities:
            -   IntegrityWorkers are validators and external services and validators.
            -   IntegrityWorkers simplify and modularize dependency management.
            -   They decrease the number of imports.
            -   Simplify Builder/Validator entry point signatures.
            -   This is too large for a simple RankIntegrityWorker.
            -   Single files
            
        RankPersonaValidator is Not an IntegrityWorker:
            -   RankPersonaValidator lives inside the *.rank.validator package.
            -   Highly cohesive with RankValidator.
            -   Don't want any cyclic dependencies with RankTool.persona_service.
            -   Requires its package.
        
        Contractors:
            -   If I need to writer other validators for ranks I'put them all in a contractors
                package.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            rank: Rank,
            persona_service: PersonaService,
    ) -> ValidationResult[Rank]:
        """
        Verify the candidate is a Rank that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult
                    -   the candidate does not exist.
                    -   the candidate is not a Rank.
                    -   Any integrity worker raises a failed test.
            2.  Otherwise, after the candidate is cast to a Rank, send the success result.
        Args:
            rank: Any
            persona_service: PersonaService
        Returns:
            ValidationResult[Rank]
        Raises:
            TypeError
            NullRankException
            RankPersonaValidatorException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Handle the case that, a King has the wrong Persona. ---#
        if isinstance(rank, King):
            if rank.persona != persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankPersonaValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=RankPersonaValidatorException.OP,
                        msg=RankPersonaValidatorException.MSG,
                        err_code=RankPersonaValidatorException.ERR_CODE,
                        mthd_rslt_type=RankPersonaValidatorException.MTHD_RSLT,
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
            if rank.persona != persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankPersonaValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=RankPersonaValidatorException.OP,
                        msg=RankPersonaValidatorException.MSG,
                        err_code=RankPersonaValidatorException.ERR_CODE,
                        mthd_rslt_type=RankPersonaValidatorException.MTHD_RSLT,
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
            if rank.persona != persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankPersonaValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=RankPersonaValidatorException.OP,
                        msg=RankPersonaValidatorException.MSG,
                        err_code=RankPersonaValidatorException.ERR_CODE,
                        mthd_rslt_type=RankPersonaValidatorException.MTHD_RSLT,
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
            if rank.persona != persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankPersonaValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=RankPersonaValidatorException.OP,
                        msg=RankPersonaValidatorException.MSG,
                        err_code=RankPersonaValidatorException.ERR_CODE,
                        mthd_rslt_type=RankPersonaValidatorException.MTHD_RSLT,
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
            if rank.persona != persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankPersonaValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=RankPersonaValidatorException.OP,
                        msg=RankPersonaValidatorException.MSG,
                        err_code=RankPersonaValidatorException.ERR_CODE,
                        mthd_rslt_type=RankPersonaValidatorException.MTHD_RSLT,
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
            if rank.persona != persona_service.persona:
                # Return the exception on failure.
                return ValidationResult.failure(
                    RankPersonaValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        op=RankPersonaValidatorException.OP,
                        msg=RankPersonaValidatorException.MSG,
                        err_code=RankPersonaValidatorException.ERR_CODE,
                        mthd_rslt_type=RankPersonaValidatorException.MTHD_RSLT,
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
            RankPersonaValidatorException(
                cls_mthd=method,
                cls_name=cls.__name__,
                op=RankPersonaValidatorException.OP,
                msg=RankPersonaValidatorException.MSG,
                err_code=RankPersonaValidatorException.ERR_CODE,
                mthd_rslt_type=RankPersonaValidatorException.MTHD_RSLT,
                ex=RankValidationRouteException(
                    val=rank,
                    var=rank.persona.name,
                    msg=RankPersonaValidatorException.MSG,
                    err_code=RankPersonaValidatorException.ERR_CODE,
                )
            )
        )
 

