# src/fabrication/builder/model/token/builder.py

"""
Module: fabrication.builder.model.token.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Token, TokenBlueprint
from err import TokenBuilderException
from exchange import TokenBuildRequest
from fabrication import ModelBuilder, TokenBuildLoader
from util import LoggingLevelRouter


class TokenBuilder(ModelBuilder[Token]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Token from a blueprint.

    Attributes:
       loader: TokenBuildLoader

    Provides:
        -   def execute(blueprint: TokenBlueprint) -> BuildResult[Token]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[TokenBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[TokenBuildLoader]
        """
        super().__init__(loader=loader or TokenBuildLoader())
    
    @property
    def loader(self) -> TokenBuildLoader:
        return cast(TokenBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: TokenBuildRequest) -> BuildResult[Token]:
        """
        Assemble a Token from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Token for the success result.
        Args:
            request: TokenBuildRequest
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        result = self.loader.execute(request=request)
        # Handle the case that the loader aborts.
        if result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(TokenBlueprint, result.payload)
        
        # --- Send the work product. ---#
        product = Token(
            x=blueprint.x,
            y=blueprint.y,
        )
        return BuildResult.success(product)