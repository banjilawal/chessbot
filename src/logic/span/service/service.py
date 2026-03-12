# src/logic/span/service/service.py

"""
Module: logic.span.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from abc import abstractmethod

from logic.graph import Graph
from logic.coord import CoordService
from logic.span import CoordSpan, SpanGraphHandler, SpanServiceException, Spanner
from logic.vector import VectorService
from logic.square import SquareDatabase
from logic.token import Token, TokenService
from logic.system import ComputationResult, IdFactory, IdentityService, LoggingLevelRouter, Service

class SpanService(Service[CoordSpan]):
    """
    ROLE: Service, Computation
    TASK: Graphing
    
    RESPONSIBILITIES:
        1.  Generate a Graph from a Token's current position.
    
    INHERITED RESPONSIBILITIES:
        * See Service for inherited responsibilities.
    
    PARENT:
        *   Service
    
    PROVIDES:
    None
    
    LOCAL ATTRIBUTES:
        *   coord_service: CoordService
        *   vector_service: VectorService
    
    INHERITED ATTRIBUTES:
        *   See Service for inherited attributes.
    
    CONSTRUCTOR PARAMETERS:
        *   id: int
        *   name: str
        *   coord_service: CoordService
        *   vector_service: VectorService
    
    LOCAL METHODS:
        *   graph(
                    token: Token, square_database: SquareDatabase,token_service: TokenService
            ) -> ComputationResult[Graph]
    
    INHERITED METHODS:
    None
    """
    SERVICE_NAME = "SpanService"
    _graph_handler: SpanGraphHandler
    _coord_service: CoordService
    _vector_service: VectorService
    _identity_service: IdentityService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
            id: int = IdFactory.next_id(class_name="SpanService"),
            identity_service: IdentityService = IdentityService(),
            graph_handler: SpanGraphHandler = SpanGraphHandler(),
    ):
        """
        Args:
            id: int
            name: str
            coord_service: CoordService
            vector_service: VectorService
        """
        super().__init__(id=id, name=name,)
        self._coord_service = coord_service
        self._vector_service = vector_service
        self._identity_service = identity_service
        self._graph_handler = graph_handler
    
    @property
    @abstractmethod
    def spanner(self) -> Spanner:
        pass
    
    @property
    def graph_handler(self) -> SpanGraphHandler:
        return self._graph_handler
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def vector_service(self) -> VectorService:
        return self._vector_service
    
    @property
    def identity_service(self) -> IdentityService:
        return self._identity_service
    

    @LoggingLevelRouter.monitor
    def produce_graph(
            self,
            token: Token,
            square_database: SquareDatabase,
            token_service: TokenService = TokenService(),
    ) -> ComputationResult[Graph]:
        """
        Args:
            token: Token
            square_database: SquareDatabase
            token_service: TokenService

        Returns:
            ComputationResult[Graph]

        Raises:
            BishopSpanServiceException
        """
        method = f"{self.__class__.name}.graph"
        
        span_result = self._spanner.compute(
            origin=token.current_position,
            coord_service=self.coord_service,
        )
        # Handle the case that the span is not produced.
        if span_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                SpanServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SpanServiceException.MSG,
                    err_code=SpanServiceException.ERR_CODE,
                    ex=span_result.exception
                )
            )
        graph = Graph(id=IdFactory.next_id(class_name="Graph"))
        
    @LoggingLevelRouter.monitor
    def derive_squares