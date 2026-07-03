# src/stack/attack/stack.py

"""
Module: stack.attack.stack
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Iterator, List, Optional

from analyzer import CollisionAnalyzer
from controller.stack.attack.controller import AttackStackOpsController

from event import AttackEvent
from microservice import IdentityService, AttackService
from model import Attack, AttackContext
from result import DeletionResult, InsertionResult, SearchResult
from stack import StackService, AttackStackState
from system import IdFactory, LoggingLevelRouter


class AttackStackService(StackService[AttackEvent]):
    """
    Role:
        -   API
        -   ACID compliance
        -   Stateful microservice
        -   Stateful CRUD Controller
        -   Operations Provider

    Responsibilities:
        1.  Baremetal service request API for Attack collections.
        2.  Preserve consistency during updates and deletes.
        3.  Stateful, scalable integrity management of Attacks.
        4.  Attack search and retrieval.

    Attributes:
        CAPACITY = 16
        SERVICE_NAME = AttackStackService
 
        id: int
        schema: str
        size: int
        capacity: int
        items: List[AttackEvent]
        iterator: Iterator[AttackEvent]
        stack_state: AttackStackState
        current_item: Optional[AttackEvent]
        integrity_service: AttackService
        ops_controller: AttackStackOpsController

    Provides:
        -   is_empty() -> bool
        -   is_being_deployed() -> bool
        -   is_deployed_on_board() -> bool
        -   pop() -> DeletionResult[AttackEvent]
        -   push(item: Attack) -> InsertionResult
        -   is_ready_for_deployment() -> bool
        -   is_getting_ready_for_deployment() -> bool
        -   delete_by_id(id: int) -> DeletionResult[AttackEvent]
        -   context(context: Context[AttackEvent]) -> SearchResult[List[AttackEvent]]

    Super Class:
        StackService
    """
    SERVICE_NAME: str = "AttackStackService"
    _stack: List[AttackEvent]
    _state: AttackStackState
    _ops_controller: AttackStackOpsController
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="AttackStackService"),
    ):
        """
        Args:
            id: int
            name: str
        """
        super().__init__(id=id, name=name,)
        self._stack = []
    
    @property
    def items(self) -> List[AttackEvent]:
        return self._stack
    
    @property
    def iterator(self) -> Iterator[AttackEvent]:
        return iter(self._stack)

    @property
    def size(self) -> int:
        return len(self._stack)
    
    @property
    def current_attack(self) -> Optional[AttackEvent]:
        return self._stack[-1] if self._stack else None
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def current_item(self) -> Optional[AttackEvent]:
        return self._stack[-1] if self._stack else None
    
    @property
    def request(self) -> AttackStackOpsController:
        return self._ops_controller
    
    @property
    def microservice(self) -> AttackService:
        return self._ops_controller.integrity_service
    
    @property
    def is_getting_ready_for_deployment(self) -> bool:
        return not (
                self.is_full and
                self._state == AttackStackState.NOT_READY_FORD_DEPLOYMENT
        )
    
    @property
    def is_ready_for_deployment(self) -> bool:
        return (
                self.is_full and
                self._state == AttackStackState.READY_FOR_DEPLOYMENT
        )
    
    @property
    def is_being_deployed(self) -> bool:
        return self.is_partially_full and self._state == AttackStackState.BEING_DEPLOYED
    
    @property
    def is_deployed_on_board(self) -> bool:
        return (
                self.is_empty and
                self._state == AttackStackState.DEPLOYED_ON_BOARD
        )
    
    @property
    def collision_analyst(self) -> CollisionAnalyzer[AttackEvent]:
        return self._ops_controller.collision_analyst
    
    @property
    def stack_state(self) -> AttackStackState:
        return self._state
    
    @stack_state.setter
    def stack_state(self, state: AttackStackState):
        self._state = state
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[AttackEvent]:
        """
        Remove the last attack put on the stack.

        Action:
            If the pop fails, send an exception chain. Otherwise, send the success result.
        Args:
        Returns:
            DeletionResult[AttackEvent]
        Raises:
            AttackStackServiceException
        """
        method = f"{self.__class__.__name__}.pop"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.pop.build()
        
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                AttackStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackStackServiceException.MSG,
                    err_code=AttackStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def push(self, item: Attack) -> InsertionResult[bool]:
        """
        Put the attack onto the schema.

        Action:
            If the insertion fails, send an exception chain. Otherwise, send
            the success result.
        Args:
            item: Attack
        Returns:
            InsertionResult[bool]
        Raises:
            AttackStackServiceException
        """
        method = f"{self.__class__.__name__}.push"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.push.build(
            attack=item,
            stream=self,
            rank_quota_analyzer=self._ops_controller.rank_quota_analyzer,
            attack_collision_detector=self._ops_controller.collision_detector
        )
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                AttackStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackStackServiceException.MSG,
                    err_code=AttackStackServiceException.ERR_CODE,
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
    ) -> DeletionResult[AttackEvent]:
        """
        Delete any attack which has that id.
        
        Action:
            If the operation gets interrupted send an exception chain. Otherwise,
            send the success result.
        Args:
            id: int
            identity_service: IdentityService
        Returns:
            DeletionResult[AttackEvent]
        Raises:
            AttackStackServiceException
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
                AttackStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackStackServiceException.MSG,
                    err_code=AttackStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: AttackContext) -> SearchResult[List[AttackEvent]]:
        """
        Find attacks whose attribute value fits the context.

        Action:
            Send an exception chain if the operation gets interrupted. Otherwise, send
            the success result.
        Args:
            context: AttackContext
        Returns:
            SearchResult[List[AttackEvent]]
        Raises:
            AttackStackServiceException
        """
        method = f"{self.__class__.__name__}.context"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud.query.build(context=context)
        
        # Handle the case that, the request was not fulfilled.
        if request_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                AttackStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackStackServiceException.MSG,
                    err_code=AttackStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result