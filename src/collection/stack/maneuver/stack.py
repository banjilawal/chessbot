# src/stack/maneuver/stack.py

"""
Module: stack.maneuver.stack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Iterator, List, Optional

from sensor.analyzer import CollisionAnalyzer
from transit.controller import ManeuverStackOpsController

from event import ManeuverEvent
from microservice import IdentityService, ManeuverService
from domain.model import Maneuver, ManeuverContext
from artifcat import DeletionResult, InsertionResult, SearchResult
from collection.stack import StackService, ManeuverStackState
from system import IdFactory, LoggingLevelRouter


class ManeuverStackService(StackService[ManeuverEvent]):
    """
    Role:
        - API
        -  ACID compliance
        -  Stateful microservice
        -  Stateful CRUD Controller
        -  Operations Provider

    Responsibilities:
        1.  Baremetal service request API for Maneuver collections.
        2.  Preserve consistency during updates and deletes.
        3.  Stateful, scalable integrity management of Maneuvers.
        4.  Maneuver search and retrieval.

    Attributes:
        CAPACITY = 16
        SERVICE_NAME = ManeuverStackService
 
        id: int
        schema: str
        size: int
        capacity: int
        items: List[ManeuverEvent]
        iterator: Iterator[ManeuverEvent]
        stack_state: ManeuverStackState
        current_item: Optional[ManeuverEvent]
        integrity_service: ManeuverService
        ops_controller: ManeuverStackOpsController

    Provides:
        -  is_empty() -> bool
        -  is_being_deployed() -> bool
        -  is_deployed_on_board() -> bool
        -  pop() -> DeletionResult[ManeuverEvent]
        -  push(item: Maneuver) -> InsertionResult
        -  is_ready_for_deployment() -> bool
        -  is_getting_ready_for_deployment() -> bool
        -  delete_by_id(id: int) -> DeletionResult[ManeuverEvent]
        -  context(context: Context[ManeuverEvent]) -> SearchResult[List[ManeuverEvent]]

    Super Class:
        StackService
    """
    SERVICE_NAME: str = "ManeuverStackService"
    _stack: List[ManeuverEvent]
    _state: ManeuverStackState
    _ops_controller: ManeuverStackOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="ManeuverStackService"),
    ):
        """
        Args:
            id: int
            name: str
        """
        super().__init__(id=id, name=name,)
        self._stack = []
    
    @property
    def items(self) -> List[ManeuverEvent]:
        return self._stack
    
    @property
    def iterator(self) -> Iterator[ManeuverEvent]:
        return iter(self._stack)

    @property
    def size(self) -> int:
        return len(self._stack)
    
    @property
    def current_maneuver(self) -> Optional[ManeuverEvent]:
        return self._stack[-1] if self._stack else None
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def current_item(self) -> Optional[ManeuverEvent]:
        return self._stack[-1] if self._stack else None
    
    @property
    def request(self) -> ManeuverStackOpsController:
        return self._ops_controller
    
    @property
    def microservice(self) -> ManeuverService:
        return self._ops_controller.integrity_service
    
    @property
    def is_getting_ready_for_deployment(self) -> bool:
        return not (
                self.is_full and
                self._state == ManeuverStackState.NOT_READY_FORD_DEPLOYMENT
        )
    
    @property
    def is_ready_for_deployment(self) -> bool:
        return (
                self.is_full and
                self._state == ManeuverStackState.READY_FOR_DEPLOYMENT
        )
    
    @property
    def is_being_deployed(self) -> bool:
        return self.is_partially_full and self._state == ManeuverStackState.BEING_DEPLOYED
    
    @property
    def is_deployed_on_board(self) -> bool:
        return (
                self.is_empty and
                self._state == ManeuverStackState.DEPLOYED_ON_BOARD
        )
    
    @property
    def collision_analyst(self) -> CollisionAnalyzer[ManeuverEvent]:
        return self._ops_controller.collision_analyst
    
    @property
    def stack_state(self) -> ManeuverStackState:
        return self._state
    
    @stack_state.setter
    def stack_state(self, state: ManeuverStackState):
        self._state = state
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[ManeuverEvent]:
        """
        Remove the last maneuver put on the stack.

        Action:
            If the pop fails, send an exception chain. Otherwise, send the success result.
        Args:
        Returns:
            DeletionResult[ManeuverEvent]
        Raises:
            ManeuverStackServiceException
        """
        method = f"{self.__class__.__name__}.pop"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.pop.execute()
        
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                ManeuverStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverStackServiceException.MSG,
                    err_code=ManeuverStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def push(self, item: Maneuver) -> InsertionResult[bool]:
        """
        Put the maneuver onto the schema.

        Action:
            If the insertion fails, send an exception chain. Otherwise, send
            the success result.
        Args:
            item: Maneuver
        Returns:
            InsertionResult[bool]
        Raises:
            ManeuverStackServiceException
        """
        method = f"{self.__class__.__name__}.push"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.push.execute(
            maneuver=item,
            stream=self,
            rank_quota_analyzer=self._ops_controller.rank_quota_analyzer,
            maneuver_collision_detector=self._ops_controller.collision_detector
        )
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                ManeuverStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverStackServiceException.MSG,
                    err_code=ManeuverStackServiceException.ERR_CODE,
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
    ) -> DeletionResult[ManeuverEvent]:
        """
        Delete any maneuver which has that id.
        
        Action:
            If the operation gets interrupted send an exception chain. Otherwise,
            send the success result.
        Args:
            id: int
            identity_service: IdentityService
        Returns:
            DeletionResult[ManeuverEvent]
        Raises:
            ManeuverStackServiceException
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
                ManeuverStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverStackServiceException.MSG,
                    err_code=ManeuverStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: ManeuverContext) -> SearchResult[List[ManeuverEvent]]:
        """
        Find maneuvers whose attribute value fits the context.

        Action:
            Send an exception chain if the operation gets interrupted. Otherwise, send
            the success result.
        Args:
            context: ManeuverContext
        Returns:
            SearchResult[List[ManeuverEvent]]
        Raises:
            ManeuverStackServiceException
        """
        method = f"{self.__class__.__name__}.context"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.query.execute(context=context)
        
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                ManeuverStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverStackServiceException.MSG,
                    err_code=ManeuverStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result