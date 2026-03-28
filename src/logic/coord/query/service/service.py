# src/logic/coord/query/service/transaction.py

"""
Module: logic.coord.query.service.service
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.coord import Coord
from logic.system import QueryService, IdFactory, LoggingLevelRouter, SearchResult

class CoordQueryService(QueryService[Coord]):
    """
    Role:
        -   API
        -   Search Micro Service,

    Responsibilities:
        1.  Public facing API for querying square collections.

    Args:
        id: int
        name: str
        router: SearchRouter[T]
        context_service: IntegrityService[Context[T]]

    Provides:
        -   execute(dataset: List[T], query: Context[T]) -> SearchResult[List[T]]

    Super Class:
        Service
    """
    """
    Role:
        Search Service, Lifecycle Management, Encapsulation, API layer.

    Responsibilities:
    1.  Public facingCoord search microservice API.
    2.  Provides a map aware utility for searchingCoord objects.
    3.  Encapsulate integrity assurance logic in one extendable module.
    4.  Create a single source of truth forCoord search results by having single entry and exit points for the
       Coord search flow.

    Super Class:
        *   QueryService

    # PROVIDES:
        *  CoordQueryService


    # INHERITED ATTRIBUTES:
        *   See QueryService for inherited attributes.
    """
    SERVICE_NAME = "CoordQueryService"
    _router: CooordSearchRouter
    _context_service: CoordContextService

    def __init__(
            self,
            name: str = SERVICE_NAME,
            router: CoordSearchRouter = CoordSearchRouter(),
            id: int = IdFactory.next_id(class_name="CoordQueryService"),
            context_service: CoordContextService =CoordContextService(),
    ):
        """
        Args:
            id: int
            name: str
            router: CoordSearchRouter
            context_service: CoordContextService
        """
        super().__init__(id=id, name=name)
        self._router = router
        self._context_service = context_service
    
    @property
    def router(self) ->CoordSearchRouter:
        return self._router
    
    @property
    def context_service(self) -> CoordContextService:
        return self._context_service
    
    @LoggingLevelRouter.monitor
    def execute(self, dataset: List[Coord], context: CoordContext) -> SearchResult[List[Coord]]:
        """
        Find coords whose attribute value fits the query.

        Action:
            Send an exception chain if the operation gets interrupted. Otherwise, send
            the success result.
        Args:
            context: CoordContext
            dataset: List[Coord]
        Returns:
            SearchResult[List[Coord]]
        Raises:
            CoordQueryServiceException
        """
        method = f"{self.__class__.__name__}.query"
        
        param_validation_result = self._run_safety_checks(dataset=dataset, context=context)
        if param_validation_result.is_failure:
            return param_validation_result
        # --- Forward the request to the context_service. ---#
        query_result = self._router.route(dataset=dataset, context=context)
        
        # Handle the case that, the request was not completed.
        if query_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordQueryServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordQueryServiceException.MSG,
                    err_code=CoordQueryServiceException.ERR_CODE,
                    ex=query_result.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return query_result
    
    @LoggingLevelRouter.monitor
    def _run_safety_checks(
            self,
            dataset: List[Coord],
            context: CoordContext
    ) -> SearchResult[List[Coord]]:
        method = f"{self.__class__.__name__}._run_safety_checks"
        
        # Handle the case that, the query is incorrect
        context_validation_result = self._context_service.validation.execute(context)
        if context_validation_result.is_failure:
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordQueryServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordQueryServiceException.MSG,
                    err_code=CoordQueryServiceException.ERR_CODE,
                    ex=context_validation_result.exception,
                )
            )
        # Handle the case that, the dataset does not exist
        if dataset is None:
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordQueryServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordQueryServiceException.MSG,
                    err_code=CoordQueryServiceException.ERR_CODE,
                    ex=CoordDatasetNullException(
                        msg=CoordDatasetNullException.MSG,
                        err_code=CoordDatasetNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the dataset is the wrong type.
        if not isinstance(dataset, List):
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordQueryServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordQueryServiceException.MSG,
                    err_code=CoordQueryServiceException.ERR_CODE,
                    ex=TypeError(f"Expected List, got {type(dataset).__name__} instead.")
                )
            )
        # Handle the case that, the does not contain coords.
        if not isinstance(dataset[0], Coord):
            # Return the exception chain on failure.
            return SearchResult.failure(
                CoordQueryServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordQueryServiceException.MSG,
                    err_code=CoordQueryServiceException.ERR_CODE,
                    ex=TypeError(f"List contains {type(dataset).__name__}  instead of squares.")
                )
            )
        return SearchResult.empty()
    
    