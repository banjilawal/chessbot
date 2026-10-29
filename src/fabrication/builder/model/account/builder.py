# src/fabrication/builder/model/account/builder.py

"""
Module: fabrication.builder.model.account.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Account, AccountBlueprint
from err import AccountBuilderException
from exchange import AccountBuildRequest
from production import BuildFactory
from transit import AccountBuildRouter
from util import LoggingLevelRouter


class AccountBuilder(BuildFactory[Account]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create different Account products from the different types of blueprints.

    Attributes:
       loader: AccountBuildLoader
       router: AccountBuildRouter

    Provides:
        -   def execute(blueprint: AccountBlueprint) -> BuildResult[Account]

    Super Class:
        BuildFactory
    """
    
    def __init__(
            self,
            loader: Optional[AccountBuildLoader] | None = None,
            router: Optional[AccountBuildRouter] | None = None,
    ):
        """
        Args:
            loader: Optional[AccountBuildLoader]
            router: Optional[AccountBuildRouter]
        """
        super().__init__(
            loader=loader or AccountBuildLoader(),
            router=router or AccountBuildRouter(),
        )
    
    @property
    def loader(self) -> AccountBuildLoader:
        return cast(AccountBuildLoader, super().loader)
    
    @property
    def router(self) -> AccountBuildRouter:
        return cast(AccountBuildRouter, super().router)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountBuildRequest) -> BuildResult[Account]:
        """
        Assemble a Account from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if either:
                -   the loader does not produce a blueprint.
                -   the router does not return a product from the blueprint.
            2.  Otherwise, cast the product as a Account then send in the success result.
        Args:
            request: AccountBuildRequest
        Returns:
            BuildResult[Account]
        Raises:
            AccountBuilderException
        """
        method = f"{self.__class__.__name__}"
        
       # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                AccountBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountBuilderException.MSG,
                    err_code=AccountBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(AccountBlueprint, bootstrap.payload)
        result = self.router.execute(blueprint)
        
        # Handle the case that a product is not routed back.
        if result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                AccountBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountBuilderException.MSG,
                    err_code=AccountBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Send the work product. ---#
        return BuildResult.success(cast(Account, result.payload))