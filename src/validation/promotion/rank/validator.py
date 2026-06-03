# src/validation/promotion/rank/__init__.py

"""
Module: validation.promotion.rank.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, cast

from err import RankTeamPromotionNullException, RankElevationValidationException
from model import Rank
from operation import Validator
from result import ValidationResult
from util import LoggingLevelRouter
from toolkit import RankTeamPromotionToolkit
from validation import RankValidator


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
        validation_result = rank_validator.validate(candidate),
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
        promotion = validation_priming_result.payload
        rank_validation_result =toolkit.rank_service.validator.validate(promotion.primary)
        
        if rank_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankElevationValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankElevationValidationException.MSG,
                    err_code=RankElevationValidationException.ERR_CODE,
                    ex=rank_validation_result.exception,
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(promotion)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_satellite_table_checks(
            cls,
            promotion: Rank,
            toolkit: RankTeamPromotionToolkit
    ) -> ValidationResult[Dict[Schema, Team]]:
        method = f"{cls.__name__}.run_satellite_table_checks"
        
        # Handle the case that, the satellite is not a dictionary or null.
        table_validation_result = PromotionTableValidationPrimer.validate(promotion)
        if table_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankElevationValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankElevationValidationException.MSG,
                    err_code=RankElevationValidationException.ERR_CODE,
                    ex=table_validation_result.exception
                )
            )
        # --- Cast to Dict for additional tests. ---#
        table = cast(Dict[Schema, Any], table_validation_result.payload)
        
        # handle the case that, the keys are not safe schemas.
        for key in table.keys():
            schema_validation_result = toolkit.schema_service.validator.validate(table[key])
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankElevationValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankElevationValidationException.MSG,
                    err_code=RankElevationValidationException.ERR_CODE,
                    ex=schema_validation_result.exception
                )
            )
        # Handle the case that, the values are not safe teams.
        for key in table.keys():
            team_validation_result = toolkit.schema_service.validator.validate(table[key])
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankElevationValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankElevationValidationException.MSG,
                    err_code=RankElevationValidationException.ERR_CODE,
                    ex=team_validation_result.exception
                )
            )
        # --- Return the work product to the caller. ---#
        return ValidationResult.success(table)