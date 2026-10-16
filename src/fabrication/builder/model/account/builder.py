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
from fabrication import ModelBuilder, AccountBuildLoader
from util import LoggingLevelRouter


class AccountBuilder(ModelBuilder[Account]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Account from a blueprint.

    Attributes:
       loader: AccountBuildLoader

    Provides:
        -   def execute(blueprint: AccountBlueprint) -> BuildResult[Account]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[AccountBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[AccountBuildLoader]
        """
        super().__init__(loader=loader or AccountBuildLoader())
    
    @property
    def loader(self) -> AccountBuildLoader:
        return cast(AccountBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountBuildRequest) -> BuildResult[Account]:
        """
        Assemble a Account from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Account for the success result.
        Args:
            request: AccountBuildRequest
        Returns:
            BuildResult[Account]
        Raises:
            AccountBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        result = self.loader.execute(request=request)
        # Handle the case that the loader aborts.
        if result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                AccountBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountBuilderException.MSG,
                    err_code=AccountBuilderException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(AccountBlueprint, result.payload)
        
        # --- Send the work product. ---#
        product = Account(
            x=blueprint.x,
            y=blueprint.y,
        )
        return BuildResult.success(product)