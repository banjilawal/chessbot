# src/fabrication/loader/model/account/loader.py

"""
Module: fabrication.loader.model.account.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Account, AccountBlueprint
from err import AccountBuildLoaderException, AccountBuildRequestNullException
from exchange import AccountBuildRequest, AccountValidationRequest, AccountValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class AccountBuildLoader(ModelBuildLoader[Account]):
    """
    Role
        -   Authorization
        -   Bootstrapper
        
    Responsibilities:
        1.  Initialize the Account build process by preparing a AccountBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: AccountValidationServer

    Provides:
        -   def execute(request: AccountBuildRequest) -> BuildResult[AccountBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[AccountValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[AccountValidationServer]
        """
        super().__init__(validator=validator or AccountValidationService())
    
    @property
    def validator(self) -> AccountValidationService:
        return cast(AccountValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountBuildRequest) -> BuildResult[AccountBlueprint]:
        """
        Prepare a AccountBlueprint which guarantees a safe Account.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid AccountBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: AccountBuildRequest
        Returns:
            BuildResult[AccountBlueprint]
        Raises:
            AccountBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=AccountBuildRequest,
            null_exception=AccountBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                AccountBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountBuildLoaderException.MSG,
                    err_code=AccountBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(AccountBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=AccountValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="AccountValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                AccountBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountBuildLoaderException.MSG,
                    err_code=AccountBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(AccountBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)