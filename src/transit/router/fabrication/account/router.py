# src/transit/route/fabrication/account/router.py

"""
Module: transit.route.fabrication.account.router
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import (
    HumanAccountBlueprint, MachineAccountBlueprint, Account, AccountBlueprint
)
from err import (
    AccountBlueprintNullException, MissingAccountBuildRouteException,
    AccountBuildRouterException
)
from fabrication import (
    HumanAccountSubcontractor, BuildRouter, MachineAccountSubcontractor
)
from util import LoggingLevelRouter


class AccountBuildRouter(BuildRouter[Account]):
    """
    Role
        -   Execution Routing
        
    Responsibilities:
        1.  Routes AccountBlueprint subclasses to the appropriate assembler.

    Attributes:
        human_subcontractor: HumanAccountSubcontractor
        machine_subcontractor: MachineAccountSubcontractor
        
    Provides:
            -   def execute(blueprint: AccountBlueprint) -> BuildResult[Account]

    Super Class:
        BuildRouter
    """
    
    _human_subcontractor: HumanAccountSubcontractor
    _machine_subcontractor: MachineAccountSubcontractor

    
    def __init__(
            self,
            human_subcontractor: Optional[HumanAccountSubcontractor] | None = None,
            machine_subcontractor: Optional[MachineAccountSubcontractor] | None = None,
    ):
        """
        Args:
            human_subcontractor: Optional[HumanAccountSubcontractor]
            machine_subcontractor: Optional[MachineAccountSubcontractor]
        """
        super().__init__()
        self._human_subcontractor = human_subcontractor or HumanAccountSubcontractor()
        self._machine_subcontractor = machine_subcontractor or MachineAccountSubcontractor()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: AccountBlueprint) -> BuildResult[Account]:
        """
        Routes an AccountBlueprint to a Subcontractor for construction.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                -   The blueprint is null or the wrong type.
                -   No subcontractor exists for the blueprint.
                -   The subcontractor fails.
            2.  Otherwise, cast the subcontract's product to an Account then send in the
                success result.
        Args:
             blueprint: Blueprint[Account]
        Returns:
            BuildResult[Account]
        Raises:
            AccountBuildRouterException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the case that the router cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=AccountBlueprint,
            null_exception=AccountBlueprintNullException(),
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                AccountBuildRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountBuildRouterException.MSG,
                    err_code=AccountBuildRouterException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # Otherwise cast the payload for additional processing.
        fingerprint = cast(AccountBlueprint, validation.payload)
        
        # Initialize the default failure result
        result = BuildResult.failure(
            MissingAccountBuildRouteException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=MissingAccountBuildRouteException.MSG,
                err_code=MissingAccountBuildRouteException.ERR_CODE,
            )
        )
        # --- Route to the appropriate account_build subcontractor. ---#
        if isinstance(fingerprint, MachineAccountBlueprint):
            result = self._machine_subcontractor.execute(fingerprint)
        if isinstance(fingerprint, HumanAccountBlueprint):
            result = self._human_subcontractor.execute( fingerprint)
        
        # Handle the case that the subcontractor does make a product.
        if result.is_failure:
            # Handle the case that no route exists for the fingerprint.
            return BuildResult.failure(
                AccountBuildRouterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountBuildRouterException.MSG,
                    err_code=AccountBuildRouterException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        model = cast(Account, result.payload)
        return BuildResult.success(model)
        
        
        
        