# src/microservice/stack/coord/microservice.py

"""
Module: microservice.stack.coord.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
class CoordStackService(StackService[Coord]):
    """
    Role:
        -   API
        -   ACID compliance
        -   Stateful microservice
        -   Stateful CRUD Controller
        -   Operations Provider

    Responsibilities:
        1.  Baremetal service request API for Coord collections.
        2.  Preserve consistency during updates and deletes.
        3.  Stateful, scalable integrity management of Coords.
        4.  Coord search and retrieval.

    Attributes:
        SERVICE_NAME = CoordStackService

        id: int
        schema: str
        size: int
        is_empty: bool
        items: List[Coord]
        iterator: Iterator[Coord]
        stack_state: CoordStackState
        current_item: Optional[Coord]
        integrity_service: CoordService
        previous_coord: Optional[Coord]
        ops_controller: CoordStackOpsController

    Provides:
        -   pop() -> DeletionResult[Coord]
        -   push(item: Coord) -> InsertionResult
        -   context(context: Context[Coord]) -> SearchResult[List[Coord]]

    Super Class:
        StackService
    """
    SERVICE_NAME = "CoordStackService"
    
    _stack: List[Coord]
    _current_coord: Optional[Coord]
    _previous_coord: Optional[Coord]
    _ops_controller: CoordStackOpsController
    
    def service(
            self,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="CoordStackService"),
            ops_controller: CoordStackOpsController = CoordStackOpsController(),
    ):
        """
        Args:
            id: int
            name: str
            ops_controller: CoordStackOpsController
        """
        super().__init__(id=id, name=name,)
        self._stack = []
        self._current_coord = None
        self._previous_coord = None
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
        return self._ops_controller.service
    
    @property
    def items(self) -> List[Coord]:
        return self._stack
    
    @property
    def iterator(self) -> Iterator[Coord]:
        return iter(self._stack)
   
    @LoggingLevelRouter.monitor
    def push(self, item: Coord) -> InsertionResult:
        """
        Put a coord ontop of the schema.

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
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud_controller.push.analyze(
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
        Get the coord at the top of the schema, if it exists.

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
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud_controller.pop.analyze(
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
    def search(self, context: CoordContext) -> SearchResult[List[Coord]]:
        """
        Find a coord in the schema.

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
        method = f"{self.__class__.__name__}.context"
        
        # --- Handoff request fulfilment to the ops_controller. ---#
        request_result = self._ops_controller.crud_controller.query.query(
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
        return DeletionResult.failure(
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
                    )
                )
            )
        )
    

    
