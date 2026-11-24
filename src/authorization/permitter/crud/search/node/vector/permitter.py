# src/authorization/permitter/crud/search/node/vector/permitter.py

"""
Module: authorization.permitter.crud.search.node.vector.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import VectorNodeSearchDecision
from authorization import NodeSearchPermitter
from bootstrap import VectorNodeSearchAuthorizationLoader
from err import VectorNodeSearchPermitterException
from request import VectorNodeSearchPermissionRequest, VectorNodeSearchRequest
from util import LoggingLevelRouter


class VectorNodeSearchPermitter(
    NodeSearchPermitter[VectorNodeSearchPermissionRequest]
):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Forward a searchDecision about an VectorNodeSearchPermissionRequest to an
            VectorNodeSearchPermitter.

    Attributes:
        loader: SearchAuthorizationLoader
        
    Provides:
        -   def execute(request: VectorNodeSearchPermissionRequest) -> SearchDecision

    Super Class:
        SearchPermitter
    """

    
    def __init__(
            self, loader: Optional[VectorNodeSearchAuthorizationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[VectorNodeSearchAuthorizationLoader]
        """
        super().__init__(loader=loader or VectorNodeSearchAuthorizationLoader())
        
    @property
    def loader(self) -> VectorNodeSearchAuthorizationLoader:
        return cast(VectorNodeSearchAuthorizationLoader, super().loader)

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> VectorNodeSearchDecision:
        """
        Grant permission for a stack search.
        
        Action:
            1.  Send an exception chain in the SearchDecision if any of the following occur
                    -   The loader cannot bootstrap the process.
                    -   The permission_request or transaction_request are null.
            2.  Otherwise, send an approval searchDecision.
        Args:
            candidate: Any
        Returns:
           SearchDecision
        Raises:
            VectorNodeSearchPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate=candidate)
        if bootstrap.request_is_denied:
            # Send the exception chain in the denial.
            return VectorNodeSearchDecision.denial(
                exception=VectorNodeSearchPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchPermitterException.MSG,
                    err_code=VectorNodeSearchPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_form = cast(VectorNodeSearchPermissionRequest, bootstrap.permission_request)
        applicant = cast(VectorNodeSearchRequest, bootstrap.transaction_request)
        # Get the ids
        form_id = permission_form.id
        applicant_id = applicant.id
        # Get the applicant information
        context = applicant.context
        collection = applicant.collection
        
        # --- Otherwise prepare an approval of the transaction. ---#
        transaction_request = VectorNodeSearchRequest(
            id=applicant_id,
            context=context,
            collection=collection,
        )
        permission_request = VectorNodeSearchPermissionRequest(
            id=form_id,
            authorization_applicant=transaction_request,
        )
        # --- Forward the approval. ---#
        return VectorNodeSearchDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        