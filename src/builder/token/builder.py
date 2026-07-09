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
from builder import Builder
from err import TokenBuilderException
from model import Token
from operation import TokenAssembler
from finalizer import TokenAssemblyFinalizer
from result import BuildResult
from toolkit import TokenToolkit
from util import LoggingLevelRouter
from validator import TokenCertifier


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
    _bootstrapper: TokenCertifier
    _assembler: TokenAssembler
    _finalizer: TokenAssemblyFinalizer
    _toolkit: TokenToolkit
    
    def __init__(
            self,
            bootstrapper: TokenCertifier | None = None,
            assembler : TokenAssembler | None = None,
            finalizer: TokenAssemblyFinalizer | None = None,
            toolkit: TokenToolkit | None = None,
    ):
        self._bootstrapper = bootstrapper or TokenCertifier()
        self._assembler = assembler or TokenAssembler()
        self._finalizer = finalizer or TokenAssemblyFinalizer()
        self._toolkit = toolkit or TokenToolkit()
    
    @LoggingLevelRouter.monitor
    def build(self, blueprint: TokenBlueprint,) -> BuildResult[Token]:
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
            blueprint_validator: Certifier
            assembler: TokenAssembler
            finalizer: TokenAssemblyFinalizer
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuilderException
        """
        method = f"{cls.__name__}.build"
        

        bootstrap_result = self._bootstrapper.execute(
            candidate=blueprint,
            toolkit=self._toolkit,
        )
        # Handle the case that, the blueprint is flagged.
        if bootstrap_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=bootstrap_result.exception,
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly_result = self._assembler.execute(
            blueprint=cast(TokenBlueprint, bootstrap_result.payload)
        )
        # Handle the case that, the assembly is not completed.
        if assembly_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=assembly_result.exception,
                )
            )
        # --- Handoff the product for consistency and other finalization steps. ---#
        finalization_result = self._finalizer.execute(
            product=assembly_result.payload
        )
        # Handle the case that, the clean is not successful.
        if finalization_result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=finalization_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(finalization_result.payload)


        