# src/authorization/activity/rank/approver.py

"""
Module: authorization.activity.rank.approver
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import Decision, ValidationResult
from authorization import ActivityApprover, AuthorizationLoader
from domain import Rank
from err import RankApproverException
from exchange import AuthorizationRequest, RankValidationRequest, RankValidationService
from transit import RankCarrier
from util import IdFactory, LoggingLevelRouter

T = TypeVar("T", bound="AuthorizationRequest")

class RankApprover(ActivityApprover[Rank], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Rank satisfies the requirements for an activity.

    Attributes:
        loader: AuthorizationLoader[T]
        validation_service: RankValidationService

    Provides:
        -   def execute(request: T) -> Decision[T]
        -   def validation_check(activity: Any) -> ValidationResult[Rank]
        -   def load_check(request: Any, loader: AuthorizationLoader[T]) -> Decision[T]


    Super Class:
        ActivityApprover
    """
    _loader: AuthorizationLoader[T]

    
    def __init__(
            self,
            loader: AuthorizationLoader[T],
            validation_service: RankValidationService
    ):
        """
        Args:
            loader: AuthorizationLoader[T]
            validation_service: RankValidationService
        """
        super().__init__(validation_service=validation_service)
        self._loader = loader
        
    @property
    def loader(self) -> AuthorizationLoader[T]:
        return self._loader
        
    @property
    def validation_service(self) -> RankValidationService:
        return cast(RankValidationService, super().validation_service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Checks if a Rank meets the requirements to perform an activity.

        Args:
            request: AuthorizationRequest[T]
        Returns:
           Decision[T]
        Raises:
            RankApproverException
        """
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def load_request(self, request: Any, loader: AuthorizationLoader[T], ) -> Decision[T]:
        """
        Loads the request into the RankApprover

        Action:
            1.  Send a denial if the loader fails.
            2.  Otherwise, send an Approval.
        Args:
            request: Any
            loader: AuthorizationLoader[T]
        Returns:
           Decision[T]
        Raises:
            RankApproverException
        """
        pass
    
    @LoggingLevelRouter.monitor
    def run_validation_check(self, activity: Any) -> ValidationResult[Rank]:
        """
        Checks if an activity Rank is safe.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate gets
                flagged.
            2.  Otherwise, send the success result.
        Args:
            activity: Any
        Returns:
           ValidationResult[Rank]
        Raises:
            RankApproverException
        """
        method = f"{self.__class__.__name__}.validation_check"
        
        # Handle the case that the candidate gets flagged.
        validation = self.validation_service.extract_model(
            request=RankValidationRequest(
                item=RankCarrier(model=activity),
                id=IdFactory.next_id(class_name="RankValidationRequest")
            )
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankApproverException.MSG,
                    err_code=RankApproverException.ERR_CODE,
                )
            )
        # --- Forward the work product. ---#
        rank = cast(Rank, validation.payload)
        return ValidationResult.success(rank)

    @abstractmethod
    @LoggingLevelRouter.monitor
    def run_activity_readiness_check(self, activity: T) -> Decision[T]:
        pass
        