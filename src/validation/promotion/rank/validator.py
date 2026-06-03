# src/validation/promotion/rank/__init__.py

"""
Module: validation.promotion.rank.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err.validation.promotion import RankElevationValidationException
from model import King, Rank
from result import ValidationResult
from util import LoggingLevelRouter
from validation import RankValidator, Validator


class RankElevationValidator(Validator[Rank]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a RankTeamPromotion instance is certified safe, reliable and consistent
            before use.

    Attributes:

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : RankTeamPromotionToolkit,
            ) -> ValidationResult[RankTeamPromotion]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            rank_validator: RankValidator | None = None,
    ) -> ValidationResult[Rank]:
        """
        Verify the candidate is a safe RankTeamPromotion.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a RankTeamPromotion.
                    -   RankValidator flags the primary unsafe.
                    -   The satellite_table fails a check.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
            rank_validator: RankValidator
        Returns:
            ValidationResult[Rank]
        Raises:
            RankElevationValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if rank_validator is None:
            rank_validator = RankValidator()
            
        # Handle the case that, the candidate is flagged by the rank_validator.
        validation_result = rank_validator.validate(candidate)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankElevationValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankElevationValidationException.MSG,
                    err_code=RankElevationValidationException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        rank = cast(Rank, validation_result.payload)
        # Handle the case that, the higher rank is a King's.
        if isinstance(rank, King):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankElevationValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankElevationValidationException.MSG,
                    err_code=RankElevationValidationException.ERR_CODE,
                    ex=PromotionToKingException(
                        msg=PromotionToKingException.MSG,
                        err_code=PromotionToKingException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that, the new rank is still a Pawn's.
        if isinstance(rank, Pawn):
            # Send the exception chain on failure.
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankElevationValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankElevationValidationException.MSG,
                    err_code=RankElevationValidationException.ERR_CODE,
                    ex=PromoteToPawnException(
                        msg=PromoteToPawnException.MSG,
                        err_code=PromoteToPawnException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        return ValidationResult.success(rank)
