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
from logic.span import Span, Spanner
from logic.vector import VectorService
from logic.square import SquareDatabase
from logic.token import Token, TokenService
from logic.system import ComputationResult, IdFactory, LoggingLevelRouter, Service

class SpanService(Service[Span]):
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
    _coord_service: CoordService
    _vector_service: VectorService
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
            id: int = IdFactory.next_id(class_name="SpanService"),
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
    
    @property
    @abstractmethod
    def spanner(self) -> Spanner:
        pass
    
    @property
    def coord_service(self) -> CoordService:
        return self._coord_service
    
    @property
    def vector_service(self) -> VectorService:
        return self._vector_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def graph(
            self,
            token: Token,
            square_database: SquareDatabase,
            token_service: TokenService = TokenService(),
    ) -> ComputationResult[Graph]:
        pass