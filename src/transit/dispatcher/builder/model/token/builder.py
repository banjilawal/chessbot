# src/transit/dispatcher/builder/model/token/dispatcher/builder.py

"""
Module: transit.dispatcher.builder.model.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import TokenBlueprint
from transit.dispatcher.builder import ModelBuilder
from err import TokenBuilderException
from domain.model import Token
from artifcat import BuildResult, MethodResultType
from operation.toolkit import TokenBuilderToolkit
from util import LoggingLevelRouter


class TokenBuilder(ModelBuilder[Token]):
    """
    Role
        -  Build Pipeline
        -  Integrity Management
        -  Consistency Assurance
        -  Workflow Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[TokenBuilderToolkit]

    Provides:
        - def execute(self, blueprint: TokenBlueprint) -> BuildResult[Token]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[TokenBuilderToolkit] |
                             None = TokenBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[TokenBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> TokenBuilderToolkit:
        return cast(TokenBuilderToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TokenBlueprint) -> BuildResult[Token]:
        """
        Build a safe Token.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -  The TokenBlueprint object is flagged unsafe.
                    -  The assembler does not return a product.
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
        validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(TokenBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
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
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Token, assembly.payload))