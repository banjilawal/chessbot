# src/stack/path/stack.py

"""
Module: stack.path.stack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Iterator, List, Optional

from sensor.analyzer import CollisionAnalyzer
from transit.controller import PathStackOpsController

from event import PathEvent
from microservice import IdentityService, PathService
from domain.model import Path, PathContext
from artifcat import DeletionResult, InsertionResult, SearchResult
from collection.stack import StackService, PathStackState
from system import IdFactory, LoggingLevelRouter


class PathStackService(StackService[PathEvent]):
    """
    Role:
        - API
        -  ACID compliance
        -  Stateful microservice
        -  Stateful CRUD Controller
        -  Operations Provider

    Responsibilities:
        1.  Baremetal service request API for Path collections.
        2.  Preserve consistency during updates and deletes.
        3.  Stateful, scalable integrity management of Paths.
        4.  Path search and retrieval.

    Attributes:
        CAPACITY = 16
        SERVICE_NAME = PathStackService
 
        id: int
        schema: str
        size: int
        capacity: int
        items: List[PathEvent]
        iterator: Iterator[PathEvent]
        stack_state: PathStackState
        current_item: Optional[PathEvent]
        integrity_service: PathService
        ops_controller: PathStackOpsController

    Provides:
        -  is_empty() -> bool
        -  is_being_deployed() -> bool
        -  is_deployed_on_board() -> bool
        -  pop() -> DeletionResult[PathEvent]
        -  push(item: Path) -> InsertionResult
        -  is_ready_for_deployment() -> bool
        -  is_getting_ready_for_deployment() -> bool
        -  delete_by_id(id: int) -> DeletionResult[PathEvent]
        -  context(context: Context[PathEvent]) -> SearchResult[List[PathEvent]]

    Super Class:
        StackService
    """
    SERVICE_NAME: str = "PathStackService"
    _stack: List[PathEvent]
    _state: PathStackState
    _ops_controller: PathStackOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="PathStackService"),
    ):
        """
        Args:
            id: int
            name: str
        """
        super().__init__(id=id, name=name,)
        self._stack = []
    
    @property
    def items(self) -> List[PathEvent]:
        return self._stack
    
    @property
    def iterator(self) -> Iterator[PathEvent]:
        return iter(self._stack)

    @property
    def size(self) -> int:
        return len(self._stack)
    
    @property
    def current_path(self) -> Optional[PathEvent]:
        return self._stack[-1] if self._stack else None
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def current_item(self) -> Optional[PathEvent]:
        return self._stack[-1] if self._stack else None
    
    @property
    def request(self) -> PathStackOpsController:
        return self._ops_controller
    
    @property
    def microservice(self) -> PathService:
        return self._ops_controller.integrity_service
    
    @property
    def is_getting_ready_for_deployment(self) -> bool:
        return not (
                self.is_full and
                self._state == PathStackState.NOT_READY_FORD_DEPLOYMENT
        )
    
    @property
    def is_ready_for_deployment(self) -> bool:
        return (
                self.is_full and
                self._state == PathStackState.READY_FOR_DEPLOYMENT
        )
    
    @property
    def is_being_deployed(self) -> bool:
        return self.is_partially_full and self._state == PathStackState.BEING_DEPLOYED
    
    @property
    def is_deployed_on_board(self) -> bool:
        return (
                self.is_empty and
                self._state == PathStackState.DEPLOYED_ON_BOARD
        )
    
    @property
    def collision_analyst(self) -> CollisionAnalyzer[PathEvent]:
        return self._ops_controller.collision_analyst
    
    @property
    def stack_state(self) -> PathStackState:
        return self._state
    
    @stack_state.setter
    def stack_state(self, state: PathStackState):
        self._state = state
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[PathEvent]:
        """
        Remove the last path put on the stack.

        Action:
            If the pop fails, send an exception chain. Otherwise, send the success result.
        Args:
        Returns:
            DeletionResult[PathEvent]
        Raises:
            PathStackServiceException
        """
        method = f"{self.__class__.__name__}.pop"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.pop.execute()
        
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                PathStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathStackServiceException.MSG,
                    err_code=PathStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def push(self, item: Path) -> InsertionResult[bool]:
        """
        Put the path onto the schema.

        Action:
            If the insertion fails, send an exception chain. Otherwise, send
            the success result.
        Args:
            item: Path
        Returns:
            InsertionResult[bool]
        Raises:
            PathStackServiceException
        """
        method = f"{self.__class__.__name__}.push"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.push.execute(
            path=item,
            stream=self,
            rank_quota_analyzer=self._ops_controller.rank_quota_analyzer,
            path_collision_detector=self._ops_controller.collision_detector
        )
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                PathStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathStackServiceException.MSG,
                    err_code=PathStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return InsertionResult.success()
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService
    ) -> DeletionResult[PathEvent]:
        """
        Delete any path which has that id.
        
        Action:
            If the operation gets interrupted send an exception chain. Otherwise,
            send the success result.
        Args:
            id: int
            identity_service: IdentityService
        Returns:
            DeletionResult[PathEvent]
        Raises:
            PathStackServiceException
        """
        method = f"{self.__class__.__name__}.delete_by_id"
        
        if identity_service is None:
            identity_service = IdentityService()
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.pop.delete_by_id(
            id=id,
            identity_service=identity_service
        )
        # Handle the case that, the request was not completed
        if request_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                PathStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathStackServiceException.MSG,
                    err_code=PathStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: PathContext) -> SearchResult[List[PathEvent]]:
        """
        Find paths whose attribute value fits the context.

        Action:
            Send an exception chain if the operation gets interrupted. Otherwise, send
            the success result.
        Args:
            context: PathContext
        Returns:
            SearchResult[List[PathEvent]]
        Raises:
            PathStackServiceException
        """
        method = f"{self.__class__.__name__}.context"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.query.execute(context=context)
        
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                PathStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathStackServiceException.MSG,
                    err_code=PathStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result