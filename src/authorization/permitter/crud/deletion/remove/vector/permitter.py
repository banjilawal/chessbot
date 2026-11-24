# src/authorization/permitter/crud/deletion/remove/vector/permitter.py

"""
Module: authorization.permitter.crud.deletion.remove.vector.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import RemoveVectorNodeDecision
from authorization import RemoveNodePermitter
from bootstrap import RemoveVectorNodeAuthorizationLoader
from request import RemoveVectorNodePermissionRequest, RemoveVectorNodeRequest
from util import LoggingLevelRouter


class RemoveVectorNodePermitter(RemoveNodePermitter[RemoveVectorNodePermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a decision about an RemoveVectorNodePermissionRequest.

    Attributes:
        loader: RemoveAuthorizationLoader
        collision_manager: VectorCollisionManager
        
    Provides:
        -   def execute(request: RemoveVectorNodePermissionRequest) -> RemoveVectorNodeDecision

    Super Class:
        RemovePermitter
    """

    def __init__(
            self,
            loader: Optional[RemoveVectorNodeAuthorizationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[RemoveAuthorizationLoader]
        """
        super().__init__(
            loader=loader or RemoveVectorNodeAuthorizationLoader(),
        )
    
    @property
    def loader(self) -> RemoveVectorNodeAuthorizationLoader:
        return cast(RemoveVectorNodeAuthorizationLoader, super().loader)
    

    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> RemoveVectorNodeDecision:
        """
        Grant permission for a stack remove.
        
        Action:
            1.  Send an exception chain in the DeletionDecision if the request
                cannot be loaded.
            2.  Return a do_nothing when the context already exists.
            3.  Otherwise, send an approval decision.
        Args:
            candidate: Any
        Returns:
           RemoveVectorNodeDecision
        Raises:
            RemoveVectorNodePermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate=candidate)
        if bootstrap.request_is_denied:
            # Send the exception chain in the denial.
            return RemoveVectorNodeDecision.denial(
                exception=RemoveVectorNodePermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RemoveVectorNodePermitterException.MSG,
                    err_code=RemoveVectorNodePermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Extract the transaction_request for processing. ---#
        permission_form = cast(RemoveVectorNodePermissionRequest, bootstrap.permission_request)
        applicant = cast(RemoveVectorNodeRequest, bootstrap.transaction_request)
        
        # Get the ids
        form_id = permission_form.id
        applicant_id = applicant.id
        # Get the applicant information
        context = applicant.context
        collection = applicant.collection
        
        if context.vector is None:
            # Send the exception chain in the denial.
            return RemoveVectorNodeDecision.denial(
                exception=RemoveVectorNodePermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RemoveVectorNodePermitterException.MSG,
                    err_code=RemoveVectorNodePermitterException.ERR_CODE,
                    ex=VectorNodeRemovalContextException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorNodeRemovalContextException.MSG,
                        err_code=VectorNodeRemovalContextException.ERR_CODE,
                    ),
                )
            )
        if collection.is_empty:
            # Send the exception chain in the denial.
            return RemoveVectorNodeDecision.denial(
                exception=RemoveVectorNodePermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RemoveVectorNodePermitterException.MSG,
                    err_code=RemoveVectorNodePermitterException.ERR_CODE,
                    ex=PoppingEmptyVectorChainException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PoppingEmptyVectorChainException.MSG,
                        err_code=PoppingEmptyVectorChainException.ERR_CODE,
                    ),
                )
            )
 
        # --- Otherwise prepare an approval of the transaction. ---#
        transaction_request = RemoveVectorNodeRequest(
            id=applicant_id,
            context=context,
            collection=collection,
        )
        permission_request = RemoveVectorNodePermissionRequest(
            id=form_id,
            authorization_applicant=transaction_request,
        )
        # --- Forward the approval. ---#
        return RemoveVectorNodeDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        