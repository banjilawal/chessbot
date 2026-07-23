# src/builder/model/token/builder.py

"""
Module: builder.model.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import TokenBlueprint
from builder import ModelBuilder
from err import TokenBuilderException
from model import Token
from result import BuildResult, MethodResultType
from toolkit import TokenBuilderToolkit
from util import LoggingLevelRouter


class TokenBuilder(ModelBuilder[Token]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[TokenBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: TokenBlueprint) -> BuildResult[Token]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[TokenBuilderToolkit] | None = TokenBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[TokenBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> TokenBuilderToolkit:
        return cast(TokenBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TokenBlueprint) -> BuildResult[Token]:
        """
        Build a safe Token.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The TokenBlueprint object is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Token then, send in the success result,
        Args:
            blueprint: TokenBlueprint
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        blueprint_validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(
                TokenBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Token, assembly.payload))