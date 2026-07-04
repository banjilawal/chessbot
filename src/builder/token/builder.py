# src/builder/token/builder.py

"""
Module: builder.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from blueprint import TokenBlueprint
from err import TokenBuilderException
from model import Token
from operation import TokenAssembler
from operation.finalize.build import TokenAssemblyFinalizer
from result import BuildResult
from util import LoggingLevelRouter
from validation import BlueprintValidator, TokenBlueprintValidator


class TokenBuilder(Builder[Token]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner
        
   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> BuildResult[Token]

     Super Class:
         Builder
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            blueprint: TokenBlueprint,
            blueprint_validator: BlueprintValidator | None = None,
            assembler: TokenAssembler | None = None,
            finalizer: TokenAssemblyFinalizer | None = None,
    ) -> BuildResult[Token]:
        """
        Build a safe Token.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following
                occur:
                    -   The blueprint is not validated.
                    -   The token cannot be assembled from the blueprint.
                    -   An error occurs during the clean up.
            2.  Otherwise, send the success result.
        Args:
            blueprint: TokenBlueprint
            blueprint_validator: BlueprintValidator
            assembler: TokenAssembler
            finalizer: TokenAssemblyFinalizer
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuilderException
        """
        method = f"{cls.__name__}.build"
        
        # --- Supply any missing dependencies. ---#
        if assembler is None:
            assembler = TokenAssembler()
        if blueprint_validator is None:
            blueprint_validator = TokenBlueprintValidator()
        if finalizer is None:
            finalizer = TokenAssemblyFinalizer()
        
        # Handle the case that, the blueprint is flagged.
        validation_result = blueprint_validator.validate(candidate=blueprint)
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=validation_result.exception,
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly_result = assembler.execute(
            blueprint=cast(TokenBlueprint, validation_result.payload)
        )
        # Handle the case that, the assembly is not completed.
        if assembly_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=assembly_result.exception,
                )
            )
        # --- Handoff the product for consistency and other finalization steps. ---#
        finalization_result = finalizer.execute(
            product=assembly_result.payload
        )
        # Handle the case that, the clean is not successful.
        if finalization_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=finalization_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(finalization_result.payload)


        