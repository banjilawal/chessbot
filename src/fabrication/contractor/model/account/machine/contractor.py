# src/fabrication/contractor/model/account/machine/contractor.py

"""
Module: fabrication.contractor.model.account.machine.contractor
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import BuildResult
from domain import Account, AccountBlueprint, MachineAccount, MachineAccountBlueprint
from err import AccountSubcontractorException, AccountBlueprintNullException
from fabrication import AccountSubcontractor
from util import IdFactory, LoggingLevelRouter

class MachineAccountSubcontractor(AccountSubcontractor[Account]):
    """
    Role
        -   Builder
        
    Responsibilities:
        1.  Instantiate a concrete Account.

    Attributes:

    Provides:
            -   def execute(blueprint: AccountBlueprint) -> BuildResult[Account]

    Super Class:
        AccountSubcontractor
    """
    
    def __init__(self):
        """
        Args:
        """
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: AccountBlueprint) -> BuildResult[Account]:
        """
        Routes a MachineAccountBlueprint subclass to its corresponding SubBuilder.

        Args:
             blueprint: Blueprint[MachineAccount]
        Returns:
            BuildResult[MachineAccount]
        Raises:
            AccountSubcontractorException
        """
        method = f"{self.__class__.__name__}"
        
        # Handle the blueprint is null or the wrong type cannot be primed.
        validation = self.priming_validator.execute(
            candidate=blueprint,
            target_model=AccountBlueprint,
            null_exception=AccountBlueprintNullException(),
        )
        # Send the exception chain on failure.
        if validation.is_failure:
            return BuildResult.failure(
                AccountSubcontractorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountSubcontractorException.MSG,
                    err_code=AccountSubcontractorException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        fingerprint = cast(MachineAccountBlueprint, validation.payload)
        # Ensure an id exists.
        id = fingerprint.id or IdFactory.next_id(class_name="MachineAccount")
    
        # --- Send the work product to the caller. ---#
        model = MachineAccount(
            id=id,
            name=fingerprint.name,
        )
        return BuildResult.success(model)