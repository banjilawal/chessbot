# src/authorization/permitter/promotion/permitter.py

"""
Module: authorization.permitter.promotion.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import PromotionDecision
from authorization import Permitter, ReadyTokenChecker
from bootstrap import PromotionAuthorizationLoader
from domain import Elevatable
from err import PromotionPermitterException, PromotionRowException
from exchange import PromotionPermissionRequest, PromotionRequest
from util import LoggingLevelRouter


class PromotionPermitter(Permitter[PromotionPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Grant a Token permission for a Promotion.

    Attributes:
        loader: PromotionAuthorizationLoader
        ready_token_checker: ReadyTokenChecker

    Provides:
        -   def execute(candidate: Any) -> PromotionDecision

    Super Class:
        Permitter
    """
    
    _ready_token_checker: ReadyTokenChecker
    
    def __init__(
            self,
            loader: Optional[PromotionAuthorizationLoader] | None = None,
            ready_token_checker: Optional[ReadyTokenChecker] | None = None,
    ):
        """
        Args:
            loader: Optional[PromotionAuthorizationLoader]
            ready_token_checker: Optional[ReadyTokenChecker]
        """
        super().__init__(loader=loader or PromotionAuthorizationLoader())
        self._ready_token_checker = ready_token_checker or ReadyTokenChecker()
    
    @property
    def loader(self) -> PromotionAuthorizationLoader:
        return cast(PromotionAuthorizationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> PromotionDecision:
        """
        Checks if a PromotionPermissionRequest can be granted.
        
        Action:
            1.  Send an exception in the denial if any of the following occur.
                    -   The loader cannot bootstrap the process.
                    -   The token is not actionable.
                    -   The token is not at the origin to start the promotion.
                    -   The token is already at the destination.
                    -   The destination is occupied by a friend.
            2.  Otherwise, send a promotion approval.
        Args:
            candidate: Any
        Returns:
           PromotionDecision
        Raises:
            PromotionPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate=candidate)
        if bootstrap.request_is_denied:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Extract the transaction_request for processing. ---#
        permission_form = cast(PromotionPermissionRequest, bootstrap.permission_request)
        applicant = cast(PromotionRequest, bootstrap.transaction_request)
        # Get the ids
        form_id = permission_form.id
        applicant_id = applicant.id
        # Get the applicant information
        token = applicant.token
        rank = applicant.promotion_level
        
        # Handle the case that the token is disabled.
        readiness = self._ready_token_checker.execute(
            candidate=token,
            permission_request=permission_form,
            transaction_request=applicant,
        )
        if readiness.request_is_denied:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    ex=readiness.exception,
                ),
            )
        # Handle the case that the pawn is not on its promotion row.
        promotion_row = token.team.enemy_rank_row
        row = token.footstep.position.row
        
        if row is not None and row != promotion_row:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    ex=PromotionRowException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PromotionRowException.MSG,
                        err_code=PromotionRowException.ERR_CODE,
                    ),
                ),
            )
        # Handle the case that the pawn has already been promoted.
        if token.is_promoted:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    ex=DoublePromotionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=DoublePromotionException.MSG,
                        err_code=DoublePromotionException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the rank is not an Elevatable.
        if not isinstance(rank, Elevatable):
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermitterException.MSG,
                    err_code=PromotionPermitterException.ERR_CODE,
                    ex=TypeError(
                        f"Expected an Elevatable Rank got {type(rank).__name__} "
                        f"instead."
                    )
                )
            )
        # --- Prepare an approval of the transaction. ---#
        transaction_request = PromotionRequest(
            id=applicant_id,
            pawn=token,
            promotion_level=rank,
        )
        permission_request = PromotionPermissionRequest(
            id=form_id,
            authorization_applicant=transaction_request,
        )
        # --- Forward the approval. ---#
        return PromotionDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
