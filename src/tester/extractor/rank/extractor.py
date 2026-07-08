# src/tester/extractor/rank/extractor.py

"""
Module: tester.extractor.rank.extractor
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import TokenBlueprint
from err import BlueprintRankExtractorException
from microservice import RankService
from model import Rank
from result import BuildResult, ValidationResult
from schema import Persona
from toolkit import TokenToolkit
from util import LoggingLevelRouter


class BlueprintRankExtractor:
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
        toolkit: TokenToolkit

    Provides:
        -   execute(self, blueprint: TokenBlueprint) -> ValidationResult
        -   _build_rank(self, persona: Persona)-> BuildResult
        -   _validate_rank(self, rank: Rank) -> ValidationResult

    Super Class:
    """
    _toolkit: TokenToolkit
    
    def __init__(self, toolkit: TokenToolkit | None = TokenToolkit()):
        self._toolkit = toolkit
    
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
        
        # --- If the TokenBlueprint does not have its rank set find it. ---#
        if blueprint.rank is None:
            build_result = self._build_rank(
                persona=blueprint.formation.persona,
            )
            # Handle the case that the _build_rank raised an error.
            if build_result.is_failure:
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
        validation_result = self._validate_rank(rank=blueprint.rank,)
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
    

    @LoggingLevelRouter.monitor
    def _build_rank(self, persona: Persona)-> BuildResult:
        """
        Build the rank if it does not exist.

        Action:
            1.  Send an exception chain if the Build fails.
            2.  Otherwise, Send the success result.
        Args:
            persona: Persona
        Returns:
            BuildResult
        Raises:
            BlueprintRankExtractorException
        """
        method = f"{self.__class__.__name__}._build_rank"
        
        # --- Run the build ---#
        build_result = self._toolkit.rank_service.builder.build(persona=persona,)
        # Handle the case that, the build is aborted.
        if build_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                BlueprintRankExtractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BlueprintRankExtractorException.MSG,
                    err_code=BlueprintRankExtractorException.ERR_CODE,
                    ex=build_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return build_result
    
    @LoggingLevelRouter.monitor
    def _validate_rank(self, rank: Rank) -> ValidationResult:
        """
        Verify TokenBlueprint.rank when its set.

        Action:
            1.  If the rank gets flagged, send an exception chain, Otherwise, send the success result.
        Args:
            rank: Rank,
        Returns:
            ValidationResult
        Raises:
            BlueprintRankExtractorException
        """
        method = f"{self.__class__.__name__}._validate_rank"
        
        # Handle the case that, the rank is flagged.
        validation_result = self._toolkit.rank_service.validator.execute(rank)
        if validation_result.is_failure:
            # Send the exception chain on failure.
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
 