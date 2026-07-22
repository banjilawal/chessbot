# src/builder/model/token/builder.py

"""
Module: builder.model.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast
r
from blueprint import TokenBlueprint
from builder import ModelBuilder
from err import TokenBuilderException
from finalizer import TokenBuildFinalizer
from model import Token

from result import BuildResult, MethodResultType
from util import LoggingLevelRouter


class TokenBuilder(ModelBuilder[Token]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Owns the Token build lifecycle.
        2.  Preserve the chain of error custody when a Token build fails.

    Attributes:

    Provides:
        -   def execute(self, blueprint: TokenBlueprint) -> BuildResult[Token]

     Super Class:
         ModelBuilder
     """
    _finalizer: TokenBuildFinalizer

    
    def __init__(
        self,
        build_toolkit: TokenBuildToolkit | None = TokenBuildToolkit(),
        finalizer: TokenBuildFinalizer | None = TokenBuildFinalizer(),
    ):
        super().__init__(build_toolkit=build_toolkit)
        self._finalizer = finalizer
        
    @property
    def build_toolkit(self) -> ModelBuildToolkit[T]:
        return cast(TokenBuildToolkit, super().build_toolkit)

    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TokenBlueprint, ) -> BuildResult[Token]:
        """
        Build a safe Token.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The bootstrap is not successful.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assemble product then, send in the success result,
        Args:
            blueprint: TokenBlueprint
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the bootstrap is not successful.
        bootstrap = self.build_toolkit.bootstrapper.execute(candidate=blueprint)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=bootstrap.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.build_toolkit.assembler.execute(
            blueprint=cast(TokenBlueprint, bootstrap.payload)
        )
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Handoff the product for consistency and other finalization steps. ---#
        finalization = self._finalizer.execute(
            product=cast(Token, assembly.payload)
        )
        # Handle the case that, the clean is not successful.
        if finalization.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=finalization.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Token, finalization.payload))


        