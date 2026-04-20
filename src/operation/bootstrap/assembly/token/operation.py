# src/operation/bootstrap/assembly/token/__ini__.py

"""
Module: operation.bootstrap.assembly.token.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from analysis import CollisionReport
from err import BootstrapTokenAssemblyException
from model import OpeningSquare, SquareContext, Token, TokenBlueprint
from operation import AssemblyBootstrapper
from result import AnalysisResult, SearchResult, ValidationResult
from search import SquareNotFoundException
from system import IdFactory, LoggingLevelRouter
from toolkit import TokenToolkit


class TokenAssemblyBootstrapper(AssemblyBootstrapper[Token]):
    
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
            BootstrapTokenAssemblyException
        """
        method = f"{cls.__name__}.execute"
        
        if toolkit is None:
            toolkit = TokenToolkit()
            
        # Handle the case that, a blueprint value is
        blueprint_validation_result = cls._run_validations(
            blueprint=blueprint,
            toolkit=toolkit,
        )
        if blueprint_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTokenAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTokenAssemblyException.MSG,
                    err_code=BootstrapTokenAssemblyException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        # Handle the case that, a blueprint value has already been used.
        collision_analysis_result = cls._run_collision_analysis(
            blueprint=blueprint
        )
        if collision_analysis_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTokenAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTokenAssemblyException.MSG,
                    err_code=BootstrapTokenAssemblyException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        # Handle the case that, the opening square discovery failed.
        opening_square_discovery_result = cls._opening_square_discovery(
            blueprint=blueprint
        )
        if opening_square_discovery_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTokenAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTokenAssemblyException.MSG,
                    err_code=BootstrapTokenAssemblyException.ERR_CODE,
                    ex=blueprint_validation_result.exception,
                )
            )
        # Handle the case that its Rank instance request is not satisfied.
        rank_assembly_result = toolkit.rank_service.assembly.assembly(
            persona=blueprint.formation.persona
        )
        if rank_assembly_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTokenAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTokenAssemblyException.MSG,
                    err_code=BootstrapTokenAssemblyException.ERR_CODE,
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
            BootstrapTokenAssemblyException
        """
        method = f"{cls.__name__}._run_validations"
        
        # Handle the case that, the id is not certified as safe.
        id_validation_result = cls._verify_id(
            blueprint=blueprint,
            toolkit=toolkit
        )
        if id_validation_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTokenAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTokenAssemblyException.MSG,
                    err_code=BootstrapTokenAssemblyException.ERR_CODE,
                    ex=id_validation_result.exception,
                )
            )
        # Handle the case that, the team does not pass a validation check.
        team_validation = toolkit.team_service.validator.validate(
            candidate=blueprint.team
        )
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTokenAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTokenAssemblyException.MSG,
                    err_code=BootstrapTokenAssemblyException.ERR_CODE,
                    ex=team_validation.exception,
                )
            )
        # Handle the case that, the formation does not pass a validation check.
        formation_validation = toolkit.formation_service.validator.validate(
            candidate=blueprint.formation
        )
        if formation_validation.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTokenAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTokenAssemblyException.MSG,
                    err_code=BootstrapTokenAssemblyException.ERR_CODE,
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
            BootstrapTokenAssemblyException
        """
        method = f"{cls.__name__}._verify_id"
        
        if blueprint.id is None:
            return ValidationResult.success(IdFactory.next_id(class_name="Token"))
        
        if blueprint.id is not None:
            id_validation = toolkit.identity_service.validate_id(blueprint.id)
            if id_validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    BootstrapTokenAssemblyException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=BootstrapTokenAssemblyException.MSG,
                        err_code=BootstrapTokenAssemblyException.ERR_CODE,
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
            BootstrapTokenAssemblyException
        """
        method = f"{cls.__name__}._run_collision_analysis"
        
        # Handle the case that a blueprint value has already been used.
        collision_analysis_result = blueprint.team.roster.run_collision_analysis(
            blueprint=blueprint
        )
        if collision_analysis_result.is_failure:
            # Return the exception chain on failure.
            return AnalysisResult.failure(
                BootstrapTokenAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTokenAssemblyException.MSG,
                    err_code=BootstrapTokenAssemblyException.ERR_CODE,
                    ex=collision_analysis_result.exception,
                )
            )
        if collision_analysis_result.payload.collision_exists:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTokenAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTokenAssemblyException.MSG,
                    err_code=BootstrapTokenAssemblyException.ERR_CODE,
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
            BootstrapTokenAssemblyException
        """
        method = f"{cls.__name__}._opening_square_discovery"
        
        square_search_result = blueprint.team.roster.search(
            context=SquareContext(formation=blueprint.formation)
        )
        # Handle the case that, the search is not completed.
        if square_search_result.is_failure:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTokenAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTokenAssemblyException.MSG,
                    err_code=BootstrapTokenAssemblyException.ERR_CODE,
                    ex=square_search_result.exception,
                )
            )
        # Handle the case that, the opening square is not found.
        if square_search_result.is_empty:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                BootstrapTokenAssemblyException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BootstrapTokenAssemblyException.MSG,
                    err_code=BootstrapTokenAssemblyException.ERR_CODE,
                    ex=SquareNotFoundException(
                        msg=SquareNotFoundException.MSG,
                        err_code=SquareNotFoundException.ERR_CODE,
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return square_search_result