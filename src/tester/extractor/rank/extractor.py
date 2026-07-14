# src/tester/extractor/rank/extractor.py

"""
Module: tester.extractor.rank.extractor
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Type

from blueprint import TokenBlueprint
from bootstrapper import PrimingValidator
from err import BlueprintRankExtractorException, TokenBlueprintNullException
from microservice import RankService
from result import ValidationResult
from tester import Extractor
from util import LoggingLevelRouter


class BlueprintRankExtractor(Extractor):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Validate a TokenBlueprint's rank if it exists. Otherwise, find it using
            the formation and formation.

    Attributes:
        priming_validator: PrimingValidator
        rank_service: RankService

    Provides:
        -   execute(self, blueprint: TokenBlueprint) -> ValidationResult

    Super Class:
    """
    _priming_validator: PrimingValidator
    _rank_service: RankService
    
    def __init__(
            self, 
            priming_validator: PrimingValidator | None = PrimingValidator(),
            rank_service: RankService | None = RankService(),
    ):
        self._priming_validator = priming_validator
        self._rank_service = rank_service
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TokenBlueprint) -> ValidationResult:
        """
        Process a TokenBlueprint's rank validator.

        Action:
            1.  If the blueprint's rank is null, create it using the formation.
            2.  If the blueprint's rank exists, validate it.
            3.  Send an exception chain in the ValidationResult if either route fails.
            4.  Send the success result from either route taken.
        Args:
            blueprint: TokenBlueprint
        Returns:
            ValidationResult[Rank]
        Raises:
            BlueprintRankExtractorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        priming_result = self._priming_validator.execute(
            candidate=blueprint,
            target_model=Type[TokenBlueprint],
            null_exception=TokenBlueprintNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain in the validation result.
            return ValidationResult.failure(
                BlueprintRankExtractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BlueprintRankExtractorException.MSG,
                    err_code=BlueprintRankExtractorException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- If the TokenBlueprint does not have its rank set find it. ---#
        if blueprint.rank is None:
            # Handle the case that the _build_rank raised an error.
            build_result = self._rank_service.builder.execute(blueprint.formation.persona)
            if build_result.is_failure:
                # Send the exception chain in the validation result.
                return ValidationResult.failure(
                    BlueprintRankExtractorException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BlueprintRankExtractorException.MSG,
                        err_code=BlueprintRankExtractorException.ERR_CODE,
                        ex=build_result.exception,
                    )
                )
            # --- Forward the work product to the caller. ---#
            return ValidationResult.success(build_result.payload)
        
        # --- For the default case, validate the rank which already exists in the TokenBlueprint. ---#
        validation_result = self._rank_service.validator.execute(rank=blueprint.rank,)
        if validation_result.is_failure:
            # Handle the case that the _validate_rank raised an error.
            return ValidationResult.failure(
                BlueprintRankExtractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BlueprintRankExtractorException.MSG,
                    err_code=BlueprintRankExtractorException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return validation_result

 