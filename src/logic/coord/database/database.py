# src/logic/coord/database/validator.py

"""
Module: logic.coord.database.service
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import List, Optional

from logic.coord import Coord, CoordContext, CoordDatabaseException, CoordStackService, CoordService
from logic.system import (
    DeletionResult, IdFactory, IdentityService, InsertionResult, LoggingLevelRouter, MethodImplementationException,
    SearchResult, Database,
)


class CoordDatabase(Database[Coord]):
    """
    Role:
        -   Repo interface.
        -   Data Protection layer.

    Responsibilities:
        1.  Protects TokenStackService data from direct access.
        2.  Middle layer between clients and TokenStackService.
        3.  Platform for extending TokenStackService features.

    Attributes:
        SERVICE_NAME = "TokenDatabase"

        id: int
        stack: str
        size: int
        is_empty: bool
        iterator: Iterator[Token]
        kernel: TokenStackService
        current_item: Optional[Token]
        integrity_service: TokenService

    Provides:
        -   insert(token: Token) -> InsertionResult[bool]
        -   search(query: TokenContext) -> SearchResult[List[Token]]

    Super:
        Database
    """
    SERVICE_NAME = "CoordDatabase"
    _kernel: CoordStackService
    
    def __init__(
            self,
            kernel: CoordStackService,
            name: str = SERVICE_NAME,
            id: int = IdFactory.next_id(class_name="CoordDatabase"),
    ):
        """
        Args:
            id: int
            name: str
            kernel: CoordStackService
        """
        super().__init__(id=id, name=name)
        self._kernel = kernel
    
    @property
    def integrity_service(self) -> CoordService:
        return self._kernel.integrity_service
    
    @property
    def iterator(self) -> Iterator[Coord]:
        return self._kernel.iterator
    
    @property
    def size(self) -> int:
        return self._kernel.size
    
    @property
    def is_empty(self) -> bool:
        return self._kernel.is_empty
    
    @property
    def current_item(self) -> Optional[Coord]:
        return self._kernel.current_item
    
    @LoggingLevelRouter.monitor
    def insert(self, coord: Coord) -> InsertionResult[bool]:
        """
        Insert a coord into the database.

        Action:
            If the insertion fails, send an exception chain. Otherwise, send the success result.
        Args:
            coord: Coord
        Returns:
            InsertionResult[Coord]
        Raises:
            CoordDatabaseException
        """
        method = f"{self.__class__.__name__}.insert"
        
        # --- Forward the request to the kernel. ---#
        request_result = self._kernel.push(item=coord)
        
        # Handle the case that, the request was not completed.
        if request_result.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                CoordDatabaseException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordDatabaseException.MSG,
                    err_code=CoordDatabaseException.ERR_CODE,
                    ex=request_result.exception
                )
            )
        # --- Forward the response to the client. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def search(self, context: CoordContext) -> SearchResult[List[Coord]]:
        """
        Find coords whose attribute value fits the query.

        Action:
            Send an exception chain if the operation gets interrupted. Otherwise, send
            the success result.
        Args:
            context: CoordContext
        Returns:
            SearchResult[List[Coord]]
        Raises:
            CoordDatabaseException
        """
        method = f"{self.__class__.__name__}.search_coords"
        
        # --- Forward the request to the kernel. ---#
        request_result = self._kernel.query(context=context)
        
        # Handle the case that, the request was not completed.
        if request_result.is_failure:
            # Return the exception chain on failure
            return SearchResult.failure(
                CoordDatabaseException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordDatabaseException.MSG,
                    err_code=CoordDatabaseException.ERR_CODE,
                    ex=request_result.exception
                )
            )
        # --- Forward the response to the client. ---#
        return request_result
    
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService(),
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
            CoordDatabaseException
            MethodImplementationException
        """
        method = f"{self.__class__.__name__}.delete_by_id"
        
        # Handle the case that, the method is called.
        return DeletionResult.failure(
            CoordDatabaseException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=CoordDatabaseException.MSG,
                err_code=CoordDatabaseException.ERR_CODE,
                ex=MethodImplementationException(
                    var=method,
                    err_code=MethodImplementationException.ERR_CODE,
                    msg=(
                        f"{method} is not implemented: coords does not have ids."
                    )
                )
            )
        )
