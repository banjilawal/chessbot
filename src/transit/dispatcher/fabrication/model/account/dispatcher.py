# src/transit/dispatcher/fabrication/model/account/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.account.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import BuildResult
from domain import Account
from exchange import AccountBuildRequest
from fabrication import AccountBuilder
from transit import ModelBuildDispatcher
from util import LoggingLevelRouter


class AccountBuildDispatcher(ModelBuildDispatcher[AccountBuildRequest, AccountBuilder]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the AccountBuild workflow.

    Attributes:
        builder: AccountBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: Optional[AccountBuilder] | None = None,
    ):
        super().__init__(builder=builder or AccountBuilder())
        
    @property
    def builder(self) -> AccountBuilder:
        return cast(AccountBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: AccountBuildRequest) -> BuildResult[Account]:
        """
        Forward a job to a AccountBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a AccountCarrier and send in
                the success result.
        Args:
            request: Any
        Returns:
            BuildResult[AccountCarrier]
        Raises:
             AccountBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(request)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                AccountBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountBuildDispatcherException.MSG,
                    err_code=AccountBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        product = cast(Account, build.payload)
        return BuildResult.success(product)