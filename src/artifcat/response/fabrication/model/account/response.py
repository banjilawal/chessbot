# src/artifact/response/fabrication/model/account/response.py

"""
Module: artifact.response.fabrication.model.account.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ModelBuildResponse, ResponseState
from domain import Account
from exchange import Request, AccountBuildRequest
from transit import AccountCarrier


class AccountBuildResponse(ModelBuildResponse[AccountBuildRequest]):
    """
    Role
        -   Persistence

    Responsibilities:
        1.  Capture the outcome of a AccountBuild transaction.

    Attributes:
        request: AccountBuildRequest
        model: Optional[Account]
        carrier: Optional[AccountCarrier]

        is_success: bool
        is_failure: bool

    Provides:
        -   def success(result: BuildResult, request: Request) -> AccountBuildResponse
        -   def failure(request: Request, exception: Exception) -> AccountBuildResponse

    Super Class:
        ModelBuildResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            request: AccountBuildRequest,
            result: Optional[BuildResult] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: BuildResult
            request: AccountBuildRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception,
        )
        
    @property
    def result(self) -> Optional[BuildResult]:
        return cast(BuildResult, super().result)
        
    @property
    def request(self) -> AccountBuildRequest:
        return cast(AccountBuildRequest, super().request)
    
    @property
    def is_success(self) -> bool:
        return (
                super().is_success and
                self.model is not None and
                isinstance(self.model, Account)
        )
    
    @property
    def is_failure(self) -> bool:
        return not self.is_success
    
    @property
    def model(self) -> Optional[Account]:
        carrier = self.carrier
        if carrier is None:
            return None
        model = cast(Account, carrier.entity)
        return model
    
    @property
    def carrier(self) -> Optional[AccountCarrier]:
        result = self.result
        if (
            result is None or
            not isinstance(result, BuildResult)
        ):
            return None
        carrier = cast(AccountCarrier, result.payload)
        if (
            carrier is None or
            carrier.is_empty or
            not carrier.has_model
        ):
            return None
        return carrier
        
    @classmethod
    def success(cls, result: BuildResult, request: Request) -> AccountBuildResponse:
        req = cast(AccountBuildRequest, request)
        return cls(
            request=req,
            result=result,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(cls, request: Request, exception: Exception) -> AccountBuildResponse:
        req = cast(AccountBuildRequest, request)
        return cls(
            request=req,
            exception=exception,
            state=ResponseState.FAILURE,
        )