# src/validator/blueprint/token/rank/validator.py

"""
Module: validator.blueprint.token.rank.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from blueprint import TokenBlueprint
from err import RankProcessorException
from microservice import RankService
from model import Persona, Rank
from result import BuildResult, ValidationResult
from toolkit import TokenToolkit
from util import LoggingLevelRouter


class BlueprintRankProcessor:
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

    Provides:
        -   def execute(
                    blueprint: TokenBlueprint,
                    toolkit: TokenToolkit,
            ) -> ValidationResult[Rank]:

    Super Class:
        BlueprintValidator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            blueprint: TokenBlueprint,
            toolkit: TokenToolkit | None = None
    ) -> ValidationResult[Rank]:
        """
        Process a TokenBlueprint's rank validator.

        Action:
            1.  If the blueprint's rank is null, create it using the formation.
            2.  If the blueprint's rank exists, validate it.
            3.  Send an exception chain in the ValidationResult if either route fails.
            4.  Send the success result from either route taken.
        Args:
            blueprint: TokenBlueprint
            toolkit: TokenToolkit
        Returns:
            ValidationResult[Rank]
        Raises:
            RankProcessorException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TokenToolkit()
        
        # --- If the TokenBlueprint does not have its rank set find it. ---#
        if blueprint.rank is None:
            build_result = cls._build_rank(
                persona=blueprint.formation.persona,
                rank_service=toolkit.rank_service,
            )
            # Handle the case that the _build_rank raised an error.
            if build_result.is_failure:
                return ValidationResult.failure(
                    RankProcessorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=RankProcessorException.MSG,
                        err_code=RankProcessorException.ERR_CODE,
                        ex=build_result.exception,
                    )
                )
            # --- Forward the work product to the caller. ---#
            return ValidationResult.success(build_result.payload)
        
        # --- For the default case, validate the rank which already exists in the TokenBlueprint. ---#
        validation_result = cls._validate_rank(
            rank=blueprint.rank,
            rank_validator=toolkit.rank_service.validator,
        )
        if validation_result.is_failure:
            # Handle the case that the _validate_rank raised an error.
            return ValidationResult.failure(
                RankProcessorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RankProcessorException.MSG,
                    err_code=RankProcessorException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return validation_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_rank(
            cls,
            persona: Persona,
            rank_service: RankService,
    ) -> BuildResult[Rank]:
        """
        Build the rank if it does not exist.

        Action:
            1.  Send an exception chain if the Build fails.
            2.  Otherwise, Send the success result.
        Args:
            persona: Persona
            rank_service: RankService
        Returns:
            BuildResult[Rank]
        Raises:
            RankProcessorException
        """
        method = f"{cls.__name__}._build_rank"
        
        # --- Run the build ---#
        build_result = rank_service.builder.build(persona=persona,)
        # Handle the case that, the build is aborted.
        if build_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                RankProcessorException(
                    msg=RankProcessorException.MSG,
                    err_code=RankProcessorException.ERR_CODE,
                    ex=build_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return build_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_rank(
            cls,
            rank: Rank,
            rank_service: RankService,
    ) -> ValidationResult[Rank]:
        """
        Verify TokenBlueprint.rank when its set.

        Action:
            1.  If the rank gets flagged, send an exception chain, Otherwise, send the success result.
        Args:
            rank: Rank,
            rank_service: RankService
        Returns:
            ValidationResult[Rank]
        Raises:
            RankProcessorException
        """
        method = f"{cls.__name__}._validate_rank"
        
        # Handle the case that, the rank is flagged.
        validation_result = rank_service.validator.run(rank)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankProcessorException(
                    msg=RankProcessorException.MSG,
                    err_code=RankProcessorException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return validation_result
 