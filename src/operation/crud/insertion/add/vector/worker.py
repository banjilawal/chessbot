# src/operation/crud/insertion/add/vector/worker.py

"""
Module: operation.crud.insertion.add.vector.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

import curses
from typing import Optional, cast

from artifcat import InsertionResult
from operation import NodeAdder
from request import AddVectorNodePermissionRequest, AddVectorNodeRequest
from transit import AddVectorNodePermissionDispatcher
from util import IdFactory, LoggingLevelRouter


class VectorNodeAdder(NodeAdder[AddVectorNodeRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an AddVectorNodeRequest

    Attributes:
        permitter: AddVectorNodePermissionDispatcher

    Provides:
        -   def execute(request: AddVectorNodeRequest) -> InsertionResult

    Super Class:
        NodeAdder
    """
    
    def __init__(
            self,
            permitter: Optional[AddVectorNodePermissionDispatcher] | None = None,
    ):
        """
        Args:
            permitter: Optional[AddVectorNodePermissionDispatcher]
        """
        super().__init__(permitter=permitter or AddVectorNodePermissionDispatcher())
    
    @property
    def permitter(self) -> AddVectorNodePermissionDispatcher:
        return cast(AddVectorNodePermissionDispatcher, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AddVectorNodeRequest) -> InsertionResult:
        """
        Add a new, unique vector to the collection.
        
        Action:
            1.  Send an exception in the InsertionResult if any of the following occur.
                    -   The request is denied.
                    -   An approval lacks either the AddVectorNodeRequest or its
                        PermissionRequest.
            2.  Otherwise, append to the collection before sending the success.
        Args:
            request: AddVectorNodeRequest
        Result:
            InsertionResult
        Raises:
            VectorNodeAdderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the permission_permitter sends a denial.
        decision = self.permitter.execute(
            candidate=AddVectorNodePermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="AddVectorNodePermissionRequest"),
            )
        )
        if decision.request_is_denied:
            # Send a failure in the Result
            return InsertionResult.failure(
                VectorNodeAdderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeAdderException.MSG,
                    err_code=VectorNodeAdderException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = cast(AddVectorNodePermissionRequest, decision.permission_request)
        transaction_request = cast(AddVectorNodeRequest, decision.transaction_request)
        
        # Handle the case that the permission_request is null.
        if permission_request is None:
            # Send the exception chain in the denial.
            return InsertionResult.failure(
                exception=AcountAdderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AcountAdderException.MSG,
                    err_code=AcountAdderException.ERR_CODE,
                    ex=AddVectorNodePermissionRequestNullException(),
                )
            )
        # Handle the case that the transaction_request is null.
        if transaction_request is None:
            # Send the exception chain in the denial.
            return InsertionResult.failure(
                exception=AcountAdderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AcountAdderException.MSG,
                    err_code=AcountAdderException.ERR_CODE,
                    ex=AddVectorNodeRequestNullException()
                )
            )
        # --- Extract the transaction participants. ---#
        node = transaction_request.item
        offset = transaction_request.offset
        collection = transaction_request.collection
        
        counter = 0
        size = collectzion.size
        cursor = collection.iterator
        while counter < offset and cursor.has_next:
            cursor = cursor.next
            counter = counter + 1
        node.previous = cursor
        node.next = cursor.next
        cursor.next = node
        collection.size = size + 1
        
        # --- Perform transaction and state management work. ---#
        # --- Forward the work product to the client. ---#
        return InsertionResult.success()