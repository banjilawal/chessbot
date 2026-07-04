# src/validation/blueprint/token/validator.py

"""
Module: validation.blueprint.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from blueprint import TokenBlueprint
from database.team.database import failure
from err import FormationNullException, TokenBlueprintNullException, TokenBlueprintValidatorException
from model import Formation, SquareContext
from result import ValidationResult
from toolkit import TokenToolkit
from util import LoggingLevelRouter
from validation import Validator


class TokenBlueprintValidator(Validator[TokenBlueprint]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Ensure a TokenBlueprint instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    toolkit: TokenBlueprintToolkit,
            ) -> ValidationResult:

    Super Class:
        BlueprintValidator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: TokenToolkit | None = None
    ) -> ValidationResult[TokenBlueprint]:
        """
        Verify a TokenBlueprint and fill before its used.

        Action:
            1.  Send an exception chain in the ValidationResult if any following occurs:
                    -   A blueprint attribute gets flagged by a validator.
                    -   The opening square is not found.
                    -   The Rank is not built successfully.
                    -   Any blueprint values have already been used in the team.
            2.  Otherwise ,create a new Blueprint including the Rank and OpeningSquare.
            2.  Send the success result.
        Args:
            candidate: Any
            toolkit: TokenToolkit
        Returns:
            ValidationResult[Blueprint]
        Raises:
            PrimingTokenAssemblyException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if toolkit is None:
            toolkit = TokenToolkit()
        
        # Handle the case that, the candidate fails an initial check.
        priming_validation_result = toolkit.priming_validator.validate(
            candidate=candidate,
            target_model=TokenBlueprint,
            null_exception=TokenBlueprintNullException(),
        )
        if priming_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=priming_validation_result.exception,
                )
            )
        # --- Cast the candidate into a TokenBlueprint for additional tests. ---#
        blueprint = cast(TokenBlueprint, candidate)
        
        # Handle the case that, any id in the blueprint is flagged.
        id_validation_result = toolkit.blueprint_id_validator.validate(
            candidate=blueprint.id,
            identity_service=toolkit.identity_service,
        )
        if id_validation_result.is_failure:
        # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the team does not pass a validation check.
        team_validation = toolkit.team_validator.validate(
            candidate=blueprint.team
        )
        if team_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that, the formation does not pass a validation check.
        formation_validation = toolkit.priming_validator.validate(
            candidate=blueprint.formation,
            target_model=Formation,
            null_exception=FormationNullException(),
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # --- Search for the token's home square if its null. ---#
        if blueprint.opening_square is None:
        home_square_result = blueprint.team.board.squares.search(
            context=SquareContext(name=blueprint.formation.home_square_name)
        )
        if home_square_result.is-failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=home_square_result.exception,
                )
            )
        
        # Handle the case that, the the token's home square is not found.
        # Handle the case that, a blueprint value is
        blueprint_validation_result = cls._run_validations(
            blueprint=blueprint,
            toolkit=toolkit,
        )
        if blueprint_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        # Handle the case that, a blueprint value has already been used.
        collision_analysis_result = cls._run_collision_analysis(
            blueprint=blueprint
        )
        if collision_analysis_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )

        # Handle the case that, the search is not completed.
        if square_search_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=square_search_result.exception,
                )
            )
        # Handle the case that, the opening square is not found.
        if square_search_result.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=SquareNotFoundException(
                        msg=SquareNotFoundException.MSG,
                        err_code=SquareNotFoundException.ERR_CODE,
                    ),
                )
            )
        opening_square_discovery_result = cls._opening_square_discovery(
            blueprint=blueprint
        )
        if opening_square_discovery_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        # Handle the case that its Rank instance request is not satisfied.
        rank_assembly_result = toolkit.rank_service.assembly.assembly(
            persona=blueprint.formation.persona
        )
        if rank_assembly_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=rank_assembly_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            TokenBlueprint(
                team=blueprint.team,
                formation=blueprint.formation,
                rank=rank_assembly_result.payload,
                id=blueprint_validation_result.payload.id,
                opening_square=opening_square_discovery_result.payload[0],
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_validations(
            cls,
            blueprint: TokenBlueprint,
            toolkit: TokenToolkit,
    ) -> ValidationResult[TokenBlueprint]:
        """
        Verify a TokenBlueprint and fill before its used.

        Action:
            1.  Send an exception chain in the ValidationResult if any following occurs:
                    -   A blueprint attribute gets flagged by a validator.
                    -   The included id is not certified as safe.
                    -   Any blueprint values have already been used in the team.
            2.  Otherwise ,create a new Blueprint including the certified id.
            2.  Send the success result.
        Args:
            blueprint: TokenBlueprint
            toolkit: TokenToolkit
        Returns:
            ValidationResult[Blueprint]
        Raises:
            PrimingTokenAssemblyException
        """
        method = f"{cls.__name__}._run_validations"
        


        # --- Create a new TokenBlueprint with the id, then send the success result. ---#
        return ValidationResult.success(
            TokenBlueprint(
                team=blueprint.team,
                formation=blueprint.formation,
                id=id_validation_result.payload,
            )
        )
        
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _run_collision_analysis(cls, blueprint: TokenBlueprint,) -> AnalysisResult[CollisionReport]:
        """
        Verify none of the blueprint values have already been used.

        Action:
            1.  Send an exception chain in the AnalysisResult if any following occurs:
                    -   The analysis is not completed.
                    -   A collision occurred.
            2.  Otherwise, forward the success result.
        Args:
            blueprint: TokenBlueprint
        Returns:
            ValidationResult[Blueprint]
        Raises:
            PrimingTokenAssemblyException
        """
        method = f"{cls.__name__}._run_collision_analysis"
        
        # Handle the case that a blueprint value has already been used.
        collision_analysis_result = blueprint.team.roster.run_collision_analysis(
            blueprint=blueprint
        )
        if collision_analysis_result.is_failure:
            # Send the exception chain on failure.
            return AnalysisResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=collision_analysis_result.exception,
                )
            )
        if collision_analysis_result.payload.collision_exists:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=collision_analysis_result.payload.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return collision_analysis_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _opening_square_discovery(
            cls,
            blueprint: TokenBlueprint,
    ) -> SearchResult[List[OpeningSquare]]:
        """
        Find the token's opening square.

        Action:
            1.  Send an exception chain in the AnalysisResult if any following occurs:
                    -   The search is not completed.
                    -   The opening_square is not found.
            2.  Otherwise, forward the success result.
        Args:
            blueprint: TokenBlueprint
            toolkit: TokenToolkit
        Returns:
            SearchResult[List[OpeningSquare]]
        Raises:
            PrimingTokenAssemblyException
        """
        method = f"{cls.__name__}._opening_square_discovery"
        
        square_search_result = blueprint.team.roster.search(
            context=SquareContext(formation=blueprint.formation)
        )
        # Handle the case that, the search is not completed.
        if square_search_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=square_search_result.exception,
                )
            )
        # Handle the case that, the opening square is not found.
        if square_search_result.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBlueprintValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBlueprintValidatorException.MSG,
                    err_code=TokenBlueprintValidatorException.ERR_CODE,
                    ex=SquareNotFoundException(
                        msg=SquareNotFoundException.MSG,
                        err_code=SquareNotFoundException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return square_search_result


# Register the operation.
WorkerRegistryController.register_worker(worker=TokenBlueprintValidator)