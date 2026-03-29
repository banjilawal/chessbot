# src/logic/coord/database/kernel/stack.py

"""
Module: logic.coord.database.kernel.stack
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import Iterator, List, Optional, cast

from logic.system import (
    IdFactory, IdentityService, LoggingLevelRouter, MethodImplementationException,
    StackService, DeletionResult, InsertionResult, SearchResult,
)
from logic.coord import (
    Coord, CoordContext, CoordService, CoordStackOpsController, CoordStackServiceException

)

class CoordStackService(StackService[Coord]):
    """
    Role:Data Stack, Search Service, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Microservice API for managing and searching Coord collections.
    2.  Assures collection is always reliable.
    3.  Assure only valid Coords are put in the collection.
    4.  Assure updates do not break the integrity individual bag in the collection or
        the collection itself.
    5.  Provide Coord stack data structure with no guarantee of uniqueness.
    6.  Search utility.

    Super Class:
        *   StackService

    Provides:


    # INHERITED ATTRIBUTES:
        *   See StackService class for inherited attributes.
    """
    
    SERVICE_NAME = "CoordStackService"
    
    _stack: List[Coord]
    _current_coord: Optional[Coord]
    _previous_coord: Optional[Coord]
    _ops_controller: CoordStackOpsController

    
    def service(
            self,
            name: str = SERVICE_NAME,
            items: List[Coord] = List[Coord],
            id: int = IdFactory.next_id(class_name="CoordStackService"),
            ops_controller: CoordStackOpsController = CoordStackOpsController(),
    ):
        """
        Args:
            name: str
            id: int
            items: List[Coord]
            ops_controller: CoordStackOpsController
        """
        super().__init__(id=id, name=name,)
        self._stack = items
        self._previous_coord = None
        self._current_coord = None
        self._ops_controller = ops_controller

    
    @property
    def size(self) -> int:
        return len(self._stack)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def previous_coord(self) -> Optional[Coord]:
        return self._stack[-2] if self._stack else None
    
    @property
    def current_item(self) -> Optional[Coord]:
        return self._stack[-1] if self._stack else None
    
    @property
    def integrity_service(self) -> CoordService:
        return self._ops_controller.integrity_service
    
    @property
    def items(self) -> List[Coord]:
        return self._stack
    
    @property
    def iterator(self) -> Iterator[Coord]:
        return iter(self._stack)
    
    @LoggingLevelRouter.monitor
    def push(self, item: Coord) -> InsertionResult:
        """
        Put a coord ontop of the stack.

        Actions:
            1.  Send an exception chain in the InsertionResult if push fails.
                Otherwise, send the success result.
        Args:
            item: Coord
        Returns:
            InsertionResult
        Raises:
            CoordStackServiceException
        """
        method = f"{self.__class__.__name__}.push"
        
        # Request a push from the controller.
        request_result = self._ops_controller.crud_controller.push.execute(
            coord=item,
            coord_stack=self,
        )
        # Handle the case that, the request is not fulfilled.
        if request_result.is_failure:
            return InsertionResult.failure(
                CoordStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordStackServiceException.MSG,
                    err_code=CoordStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[Coord]:
        """
        Get the coord at the top of the stack, if it exists.

        Actions:
            1.  Send an exception chain in the DeletionResult if pop fails.
                Otherwise, send the success result.
        Args:
        Returns:
            DeletionResult[Coord]
        Raises:
            CoordStackServiceException
        """
        method = f"{self.__class__.__name__}.pop"
        
        # Request a pop from the controller.
        request_result = self._ops_controller.crud_controller.pop.execute(
            coord_stack=self,
        )
        # Handle the case that, the request is not fulfilled.
        if request_result.is_failure:
            return DeletionResult.failure(
                CoordStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordStackServiceException.MSG,
                    err_code=CoordStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self, id: int, identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Coord]:
        """
        Send an exception chain in the DeletionResult if the method
        is called. Coords do not have ids.

        Actions:
            1.  Coords do not have ids. Send an exception chain if this method is called.
        Args:
            id: int
            identity_service: IdentityService
        Returns:
            DeletionResult[Coord]
        Raises:
            CoordStackServiceException
            MethodImplementationException
        """
        method = f"{self.__class__.__name__}.delete_by_id"
        
        # Handle the case that, the method is called.
        return SearchResult.failure(
            CoordStackServiceException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=CoordStackServiceException.MSG,
                err_code=CoordStackServiceException.ERR_CODE,
                ex=MethodImplementationException(
                    var=method,
                    err_code=MethodImplementationException.ERR_CODE,
                    msg=(
                        f"{method} is not implemented: coords does not have ids."
                    ),
  
                ),
            )
            )
    
    @LoggingLevelRouter.monitor
    def query(self, context: CoordContext) -> SearchResult[List[Coord]]:
        """
        Find a coord in the stack.

        Actions:
            1.  Send an exception chain in the ComputationResult if either:
                    -   The vector is unsafe.
                    -   A coord cannot be built from the vector's components.
            2.  Otherwise, send the success result.
        Args:
            context: CoordContext
        Returns:
            SearchResult[Coord]
        Raises:
            CoordStackServiceException
        """
        method = f"{self.__class__.__name__}.query"
        
        # Request a search from the controller.
        request_result = self._ops_controller.crud_controller.query.execute(
            context=context,
            dataset=self.items,
        )
        # Handle the case that, the request is not fulfilled.
        if request_result.is_failure:
            return SearchResult.failure(
                CoordStackServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordStackServiceException.MSG,
                    err_code=CoordStackServiceException.ERR_CODE,
                    ex=request_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return request_result
    
