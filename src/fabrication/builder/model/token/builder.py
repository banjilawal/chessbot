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
from fabrication import BuildFactory, TokenBuildLoader
from transit import TokenBuildRouter
from util import LoggingLevelRouter


class TokenBuilder(BuildFactory[Token]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create different Token products from the different types of blueprints.

    Attributes:
       loader: TokenBuildLoader
       router: TokenBuildRouter

    Provides:
        -   def execute(blueprint: TokenBlueprint) -> BuildResult[Token]

    Super Class:
        BuildFactory
    """
    
    def __init__(
            self,
            loader: Optional[TokenBuildLoader] | None = None,
            router: Optional[TokenBuildRouter] | None = None,
    ):
        """
        Args:
            loader: Optional[TokenBuildLoader]
            router: Optional[TokenBuildRouter]
        """
        super().__init__(
            loader=loader or TokenBuildLoader(),
            router=router or TokenBuildRouter(),
        )
    
    @property
    def loader(self) -> TokenBuildLoader:
        return cast(TokenBuildLoader, super().loader)
    
    @property
    def router(self) -> TokenBuildRouter:
        return cast(TokenBuildRouter, super().router)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: TokenBuildRequest) -> BuildResult[Token]:
        """
        Assemble a Token from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if either:
                -   the loader does not produce a blueprint.
                -   the router does not return a product from the blueprint.
            2.  Otherwise, cast the product as a Token then send in the success result.
        Args:
            request: TokenBuildRequest
        Returns:
            BuildResult[Token]
        Raises:
            TokenBuilderException
        """
        method = f"{self.__class__.__name__}"
        
       # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(TokenBlueprint, bootstrap.authorization_applicant)
        result = self.router.execute(blueprint)
        
        # Handle the case that a product is not routed back.
        if result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TokenBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuilderException.MSG,
                    err_code=TokenBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Send the work product. ---#
        return BuildResult.success(cast(Token, result.payload))