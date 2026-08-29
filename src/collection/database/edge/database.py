# src/collection/database/edge/database.py

"""
Module: database.edge.database
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection.database import Database


class EdgeDatabase(Database[Edge]):
    """
    Role:
        _   Frontend
        -  Interface
        -  Data Protection

    Responsibilities:
        1.  Encapsulates StackService.
        2.  Protects data from direct access.

    Attributes:
        id: int
        size: int
        name: str
        iterator: iter
        is_empty: bool
        current_item: Optional[T]
        integrity_service: Microservice[T]

    Provides:
        -  iterator() ->: iter
        -  insert(item: T) -> InsertionResult:
        -  delete_by_id(id: int) -> DeletionResult[T]:
        -  search(context: Context[T]) -> SearchResult[List[T]]

    Role:Unique Data Stack, Search Microservice, CRUD Controller, Encapsulation, API layer.

    Responsibilities:
    1.  Ensure all bag in managed by EdgeStackService are unique.
    2.  Guarantee consistency of records in EdgeStackService.

    Super Class:
        *   Database

    Provides:


    # INHERITED ATTRIBUTES:
        *   See Database class for inherited attributes.
    """
    SERVICE_NAME = "EdgeDatabase"
    _edge_database_core: EdgeStackService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            id: int = id_emitter.service_id,
            data_service: EdgeStackService = EdgeStackService(),
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   member_service (EdgeStackService)
        # RETURNS:
            None
        Raises:
            None
        """
        super().__init__(id=id, name=name, data_service=data_service)
        self._edge_stack_service = data_service
    
    @property
    def microservice(self) -> EdgeService:
        return self._edge_database_core.edge_service
    
    @property
    def context_service(self) -> EdgeQueryService:
        return self._edge_database_core.context_service
    
    @property
    def size(self) -> int:
        return self._edge_database_core.rule_count
    
    @property
    def is_empty(self) -> bool:
        return self._edge_database_core.no_recurrences_exist
    
    @LoggingLevelRouter.monitor
    def add_unique_edge(self, edge: Edge) -> InsertionResult[Edge]:
        """
        # ACTION:
            1.  If the edge fails validation send the wrapped exception in the InsertionResult.
            2.  If a search for the edge either fails or finds a match send the wrapped exception in the
                InsertionResult.
            3.  If the call to _edge_database_core.insert_edge fails send the wrapped exception in the InsertionResult.
                Else send the outgoing result directly to the caller.
        # PARAMETERS:
            *   edge (Edge)
        # RETURN:
            *   InsertionResult[Edge] containing either:
                    - On failure: An exception.
                    - On success: Edge in payload.
        Raises:
            *   EdgeDatabaseException
            *   UniqueEdgeInsertionException
            *   EdgeDatabaseException
        """
        method = "EdgeDatabase.add_unique_edge"
        
        # --- To assure uniqueness the member_service has to conduct a search. The edge should be validated first. ---#
        
        # Handle the case that, the edgeis not safe.
        validation = self.microservice.execute.execute(candidate=edge)
        if validation.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueEdgeDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueEdgeDataServiceException.ERR_CODE}",
                    ex=UniqueEdgeInsertionException(
                        msg=f"{method}: {UniqueEdgeInsertionException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            )
        # --- KingCheckRecord if the edge is already in the collider_candidates before adding it. ---#
        search_result = self.search_edges(context=EdgeContext(id=edge.id))
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueEdgeDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueEdgeDataServiceException.ERR_CODE}",
                    ex=UniqueEdgeInsertionException(
                        msg=f"{method}: {UniqueEdgeInsertionException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # Handle the case that, the edge is already in the collider_candidates.
        if search_result.is_success:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueEdgeDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueEdgeDataServiceException.ERR_CODE}",
                    ex=UniqueEdgeInsertionException(
                        msg=f"{method}: {UniqueEdgeInsertionException.ERR_CODE}",
                        ex=AddingDuplicateEdgeException(f"{method}: {AddingDuplicateEdgeException.MSG}")
                    )
                )
            )
        # --- Use _edge_database_core.insert_edge because order does not matter for the edge access. ---#
        insertion_result = self._edge_database_core.insert_edge(edge=edge)
        
        # Handle the case that, the insertion is not completed.
        if insertion_result.is_failure:
            # Send the exception chain on failure.
            return InsertionResult.failure(
                UniqueEdgeDataServiceException(
                    msg=f"ServiceId:{self.id}, {method}: {UniqueEdgeDataServiceException.ERR_CODE}",
                    ex=UniqueEdgeInsertionException(
                        msg=f"{method}: {UniqueEdgeInsertionException.ERR_CODE}",
                        ex=insertion_result.exception
                    )
                )
            )
        # --- On success directly forward the insertion result to the caller. ---#
        return insertion_result
    
    @LoggingLevelRouter.monitor
    def search_edges(self, context: EdgeContext) -> SearchResult[List[Edge]]:
        """
        # ACTION:
            1.  Get the result of calling _edge_database_core.delete_edge_by_id for method. If the deletion failed
                wrap the exception inside the appropriate Database exceptions and send the exception chain
                in the DeletionResult.
            2.  If the deletion operation completed directly forward the DeletionResult to the caller.
        # PARAMETERS:
            *   id (int)
        # RETURN:
            *   SearchResult[Edge] containing either:
                    - On failure: An exception.
                    - On success: Edge in payload.
                    - On Empty: No payload nor exception.
        Raises:
            *   EdgeDatabaseException
            *   ExhaustiveEdgeDeletionException
        """
        method = "EdgeDatabase.search_edges"
        
        # --- Handoff the search responsibility to _edge_database_core. ---#
        search_result = self._edge_database_core.edge_context_service.finder.route(context=context)
        
        # Handle the case that, the search is not completed.
        if search_result.is_failure:
            # Send the exception chain on failure.
            return SearchResult.failure(
                UniqueEdgeDataServiceException(
                    msg=f"ServiceID:{self.id} {method}: {UniqueEdgeDataServiceException.ERR_CODE}",
                    ex=UniqueEdgeSearchException(
                        msg=f"{method}: {UniqueEdgeSearchException.ERR_CODE}",
                        ex=search_result.exception
                    )
                )
            )
        # --- For either a successful or empty search result directly forward to the caller. ---#
        return search_result