# src/logic/span/service/service.py

"""
Module: logic.span.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations

from logic.coord import CoordService
from logic.graph import Graph
from logic.span import BishopSpanServiceException, BishopSpanner, SpanService
from logic.square import SquareDatabase
from logic.system import ComputationResult, IdFactory, LoggingLevelRouter
from logic.token import Token, TokenService
from logic.vector import VectorService


class BishopSpanService(SpanService):
    """
    ROLE: Service, Computation
    TASK: Graphing

    RESPONSIBILITIES:
        1.  Generate a Graph from a Token's current position.

    INHERITED RESPONSIBILITIES:
        * See SpanService for inherited responsibilities.

    PARENT:
        *   SpanService

    PROVIDES:
    None

    LOCAL ATTRIBUTES:
        *   spanner: BishopSpanner

    INHERITED ATTRIBUTES:
        *   See SpanService for inherited attributes.

    CONSTRUCTOR PARAMETERS:
        *   id: int
        *   name: str
        *   spanner: BishopSpanner
        *   coord_service: CoordService
        *   vector_service: VectorService

    LOCAL METHODS:
    None

    INHERITED METHODS:
        *   See SpanService for inherited messages.
    """
    SERVICE_NAME = "BishopSpanService"
    _spanner: BishopSpanner
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            spanner: BishopSpanner = BishopSpanner(),
            coord_service: CoordService = CoordService(),
            vector_service: VectorService = VectorService(),
            id: int = IdFactory.next_id(class_name="BishopSpanService"),
    ):
        """
        Args:
            id: int
            name: str
            spanner: BishopSpanner
            coord_service: CoordService
            vector_service: VectorService
        """
        super().__init__(
            id=id,
            name=name,
            coord_service=coord_service,
            vector_service=vector_service,
        )
        self._spanner = spanner

    
    @property
    def spanner(self) -> BishopSpanner:
        return self._spanner
    
    @LoggingLevelRouter.monitor
    def graph(
            self,
            token: Token,
            square_database: SquareDatabase,
            graph_service: GraphService =
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
                BishopSpanServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BishopSpanServiceException.MSG,
                    err_code=BishopSpanServiceException.ERR_CODE,
                    ex=span_result.exception
                )
            )
        
        @LoggingLevelRouter.monitor
        def _
