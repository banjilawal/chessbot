# src/bootstrap/assembly/token/operation.py

"""
Module: bootstrap.assembly.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from blueprint import TokenBlueprint
from controller import WorkerRegistryController
from report import CollisionReport
from toolkit import TokenToolkit
from search import SquareNotFoundException
from operation import AssemblyPrimer
from err import TokenAssemblyPrimerException
from result import AnalysisResult, SearchResult, ValidationResult
from model import HomeSquare, SquareContext, Token
from util import IdFactory, LoggingLevelRouter


class TokenAssemblyPrimer(AssemblyPrimer[Token]):
    NAME = "token_assembly_primer"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            blueprint: TokenBlueprint,
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
            blueprint: TokenBlueprint
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
            
        # Handle the case that, a blueprint value is
        blueprint_validation_result = cls._run_validations(
            blueprint=blueprint,
            toolkit=toolkit,
        )
        if blueprint_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenAssemblyPrimerException.MSG,
                    err_code=TokenAssemblyPrimerException.ERR_CODE,
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
                TokenAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenAssemblyPrimerException.MSG,
                    err_code=TokenAssemblyPrimerException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        # Handle the case that, the opening square discovery failed.
        home_square_discovery_result = cls._home_square_discovery(
            blueprint=blueprint
        )
        if home_square_discovery_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenAssemblyPrimerException.MSG,
                    err_code=TokenAssemblyPrimerException.ERR_CODE,
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
                TokenAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenAssemblyPrimerException.MSG,
                    err_code=TokenAssemblyPrimerException.ERR_CODE,
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
                home_square=home_square_discovery_result.payload[0],
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
        
        # Handle the case that, the id is not certified as safe.
        id_validation_result = cls._verify_id(
            blueprint=blueprint,
            toolkit=toolkit
        )
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenAssemblyPrimerException.MSG,
                    err_code=TokenAssemblyPrimerException.ERR_CODE,
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
                TokenAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenAssemblyPrimerException.MSG,
                    err_code=TokenAssemblyPrimerException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that, the formation does not pass a validation check.
        formation_validation = toolkit.formation_service.execute.build(
            candidate=blueprint.formation
        )
        if formation_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenAssemblyPrimerException.MSG,
                    err_code=TokenAssemblyPrimerException.ERR_CODE,
                    ex=formation_validation.exception,
                )
            )
        # --- Create a new TokenBlueprint with the id, then send the success result. ---#
        return ValidationResult.success(
            TokenBlueprint(
                team=blueprint.team,
                formation=blueprint.formation,
                id=id_validation_result.payload,
            )
        )
        
    @classmethod
    def _verify_id(
            cls,
            blueprint: TokenBlueprint,
            toolkit: TokenToolkit
    ) -> ValidationResult[int]:
        """
        Verify the id if it already exists or create a new one.

        Action:
            1.  Send an exception chain in the ValidationResult if an existing id
                is not certified as safe.
            2.  Otherwise, send the success result.
        Args:
            blueprint: TokenBlueprint
            toolkit: TokenToolkit
        Returns:
            ValidationResult[int]
        Raises:
            PrimingTokenAssemblyException
        """
        method = f"{cls.__name__}._verify_id"
        
        if blueprint.id is None:
            return ValidationResult.success(IdFactory.next_id(class_name="Token"))
        
        if blueprint.id is not None:
            id_validation = toolkit.identity_service.validate_id(blueprint.id)
            if id_validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    TokenAssemblyPrimerException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenAssemblyPrimerException.MSG,
                        err_code=TokenAssemblyPrimerException.ERR_CODE,
                        ex=id_validation.exception,
                    )
                )
            # --- Return the work product. ---#
            return ValidationResult.success(blueprint.id)
        
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
                TokenAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenAssemblyPrimerException.MSG,
                    err_code=TokenAssemblyPrimerException.ERR_CODE,
                    ex=collision_analysis_result.exception,
                )
            )
        if collision_analysis_result.payload.collision_exists:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenAssemblyPrimerException.MSG,
                    err_code=TokenAssemblyPrimerException.ERR_CODE,
                    ex=collision_analysis_result.payload.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return collision_analysis_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _home_square_discovery(
            cls,
            blueprint: TokenBlueprint,
    ) -> SearchResult[List[HomeSquare]]:
        """
        Find the token's opening square.

        Action:
            1.  Send an exception chain in the AnalysisResult if any following occurs:
                    -   The search is not completed.
                    -   The home_square is not found.
            2.  Otherwise, forward the success result.
        Args:
            blueprint: TokenBlueprint
            toolkit: TokenToolkit
        Returns:
            SearchResult[List[OpeningSquare]]
        Raises:
            PrimingTokenAssemblyException
        """
        method = f"{cls.__name__}._home_square_discovery"
        
        square_search_result = blueprint.team.roster.search(
            context=SquareContext(formation=blueprint.formation)
        )
        # Handle the case that, the search is not completed.
        if square_search_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenAssemblyPrimerException.MSG,
                    err_code=TokenAssemblyPrimerException.ERR_CODE,
                    ex=square_search_result.exception,
                )
            )
        # Handle the case that, the opening square is not found.
        if square_search_result.is_empty:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenAssemblyPrimerException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenAssemblyPrimerException.MSG,
                    err_code=TokenAssemblyPrimerException.ERR_CODE,
                    ex=SquareNotFoundException(
                        msg=SquareNotFoundException.MSG,
                        err_code=SquareNotFoundException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return square_search_result


# Register the operation.
WorkerRegistryController.register_worker(worker=TokenAssemblyPrimer)