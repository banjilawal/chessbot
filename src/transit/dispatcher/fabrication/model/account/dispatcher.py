# src/transit/dispatcher/fabrication/model/account/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.account.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import AccountBuilder
from artifcat import BuildResult
from domain import Account
from err import AccountBuildDispatcherException
from transit import ModelBuildDispatcher, AccountCarrier
from util import LoggingLevelRouter


class AccountBuildDispatcher(ModelBuildDispatcher[Account]):
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
            builder: AccountBuilder | None = None,
    ):
        super().__init__(builder=builder or AccountBuilder())
        
    @property
    def builder(self) -> AccountBuilder:
        return cast(AccountBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[AccountCarrier]:
        """
        Forward a job to a AccountBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a AccountCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[AccountCarrier]
        Raises:
             AccountBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
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
        carrier = cast(AccountCarrier, build.payload)
        return BuildResult.success(carrier)