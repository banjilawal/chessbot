# src/authorization/permitter/crud/insertion/add/vector/permitter.py

"""
Module: authorization.permitter.crud.insertion.add.vector.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AddVectorNodeDecision
from authorization import AddNodePermitter
from bootstrap import AddVectorNodeAuthorizationLoader
from request import AddVectorNodePermissionRequest, AddVectorNodeRequest
from util import LoggingLevelRouter


class AddVectorNodePermitter(AddNodePermitter[AddVectorNodePermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about an AddVectorNodePermissionRequest.

    Attributes:
        loader: AddAuthorizationLoader
        collision_manager: VectorCollisionManager
        
    Provides:
        -   def execute(request: AddVectorNodePermissionRequest) -> AddVectorNodeDecision

    Super Class:
        AddPermitter
    """

    def __init__(
            self,
            loader: Optional[AddVectorNodeAuthorizationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[AddAuthorizationLoader]
        """
        super().__init__(
            loader=loader or AddVectorNodeAuthorizationLoader(),
        )
    
    @property
    def loader(self) -> AddVectorNodeAuthorizationLoader:
        return cast(AddVectorNodeAuthorizationLoader, super().loader)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AddVectorNodeDecision:
        """
        Grant permission for a stack add.
        
        Action:
            1.  Send an exception chain in the InsertionDecision if the request
                cannot be loaded.
            2.  Return a do_nothing when the item already exists.
            3.  Otherwise, send an approval decision.
        Args:
            candidate: Any
        Returns:
           AddVectorNodeDecision
        Raises:
            AddVectorNodePermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate=candidate)
        if bootstrap.request_is_denied:
            # Send the exception chain in the denial.
            return AddVectorNodeDecision.denial(
                exception=AddVectorNodePermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AddVectorNodePermitterException.MSG,
                    err_code=AddVectorNodePermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Extract the transaction_request for processing. ---#
        permission_form = cast(AddVectorNodePermissionRequest, bootstrap.permission_request)
        applicant = cast(AddVectorNodeRequest, bootstrap.transaction_request)
        
        # Get the ids
        form_id = permission_form.id
        applicant_id = applicant.id
        # Get the applicant information
        item = applicant.item
        collection = applicant.collection
 
        # --- Otherwise prepare an approval of the transaction. ---#
        transaction_request = AddVectorNodeRequest(
            id=applicant_id,
            item=item,
            collection=collection,
        )
        permission_request = AddVectorNodePermissionRequest(
            id=form_id,
            authorization_applicant=transaction_request,
        )
        # --- Forward the approval. ---#
        return AddVectorNodeDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        