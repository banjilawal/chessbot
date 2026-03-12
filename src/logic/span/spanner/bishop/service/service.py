# src/logic/span/service/service.py

"""
Module: logic.span.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict

from logic.coord import Coord, CoordService
from logic.edge import Edge, EdgeBuilder
from logic.graph import Graph
from logic.node import Node, NodeBuilder
from logic.span import BishopSpanServiceException, BishopSpanner, CoordSpan, SpanService
from logic.square import Square, SquareContext, SquareDatabase
from logic.system import BuildResult, ComputationResult, IdFactory, LoggingLevelRouter
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
            token_service: TokenService = TokenService(),
    ) -> ComputationResult[Graph]:

        
        @LoggingLevelRouter.monitor
        def _squares(
                self,
                span: CoordSpan,
                graph: Graph,
                square_database: SquareDatabase
        ):
            previous_square: Square = None
            current_square: Square = None
            
            for ray in span.rays:

                previous_point: Coord = ray.origin
                current_coord: Coord = ray.origin
                for point in ray.members:
                    
                    tail_square_search_result = square_database.search(context=SquareContext(coord=previous_point))
                    # Handle the case that the search is not completed
                    if tail_square_search_result.is_failure:
                        # Return the exception chain on failure.
                        return ComputationResult.failure(
                            BishopSpanServiceException(
                                cls_mthd=method,
                                cls_name=self.__class__.__name__,
                                msg=BishopSpanServiceException.MSG,
                                err_code=BishopSpanServiceException.ERR_CODE,
                                ex=tail_square_search_result.exception
                            )
                        )
                    
                    head_square_search_result = square_database.search(context=SquareContext(coord=point))
                    # Handle the case that the search is not completed
                    if head_square_search_result.is_failure:
                        # Return the exception chain on failure.
                        return ComputationResult.failure(
                            BishopSpanServiceException(
                                cls_mthd=method,
                                cls_name=self.__class__.__name__,
                                msg=BishopSpanServiceException.MSG,
                                err_code=BishopSpanServiceException.ERR_CODE,
                                ex=head_square_search_result.exception
                            )
                        )
                    square_v = square_v_search.payload[0]

                    square_u_search_result = square_database.search(context=SquareContext(coord=previous_point))
                    square_u = square_u_search_result.payload[0]
                    
                    node_pair_build_result = self._build_node_pair(
                        head_square=square_u,
                        tail_square=square_v,
                        node_builder=graph.vertices.integrity_service.builder
                    )
                    v_build_result = graph.vertices.integrity_service.builder.build(
                        square=square_v,
                        square_validator=square_database.integrity_service.validator,
                    )
                    u_build_result = graph.vertices.integrity_service.builder.build(
                        square=square_u,
                        square_validator=square_database.integrity_service.validator,
                    )
                    graph.vertices.push(u_build_result.payload)
                    graph.vertices.push(v_build_result.payload)
                    
                    e = graph.edges.integrity_service.builder.build(
                        head=u_build_result.payload,
                        tail=v_build_result.payload,
                        coord_service=self.coord_service,
                    )
                    f = graph.edges.integrity_service.builder.build(
                        head=v_build_result.payload,
                        tail=u_build_result.payload,
                        coord_service=self.coord_service,
                    )
                    graph.edges.push(e)
                    graph.edges.push(f)

                    u = graph.vertices.integrity_service.add_vertex(previous_square)
                    
                    e = graph.edges.integrity_service.add_edge(
                        source=u,
                        target=v,
                        weight=graph.edges.integrity_service
                    )
                    f = graph.edges.push(
                        graph.edges.integrity_service.builder.build(
                        
                        )
                    )
                    previous_point = point
                    current_coord = point
        
        @LoggingLevelRouter.monitor
        def _find_adjacent_squares(
                self,
                previous_point: Coord,
                point: Coord,
                square_database: SquareDatabase
        ):
            """
            """
            method = f"{self.__class__.name}.find_adjacent_squares"
            
            for ray in span.rays:
                
                previous_point: Coord = ray.origin
                current_coord: Coord = ray.origin
                for point in ray.members:
                    
                    tail_square_search_result = square_database.search(
                        context=SquareContext(coord=previous_point)
                    )
                    # Handle the case that the search is not completed
                    if tail_square_search_result.is_failure:
                        # Return the exception chain on failure.
                        return ComputationResult.failure(
                            BishopSpanServiceException(
                                cls_mthd=method,
                                cls_name=self.__class__.__name__,
                                msg=BishopSpanServiceException.MSG,
                                err_code=BishopSpanServiceException.ERR_CODE,
                                ex=tail_square_search_result.exception
                            )
                        )
                    
                    head_square_search_result = square_database.search(context=SquareContext(coord=point))
                    # Handle the case that the search is not completed
                    if head_square_search_result.is_failure:
                        # Return the exception chain on failure.
                        return ComputationResult.failure(
                            BishopSpanServiceException(
                                cls_mthd=method,
                                cls_name=self.__class__.__name__,
                                msg=BishopSpanServiceException.MSG,
                                err_code=BishopSpanServiceException.ERR_CODE,
                                ex=head_square_search_result.exception
                            )
                        )
                    square_v = square_v_search.payload[0]
                    
                    square_u_search_result = square_database.search(context=SquareContext(coord=previous_point))
                    square_u = square_u_search_result.payload[0]
                    
                    node_pair_build_result = self._build_node_pair(
                        head_square=square_u,
                        tail_square=square_v,
                        node_builder=graph.vertices.integrity_service.builder
                    )
                    v_build_result = graph.vertices.integrity_service.builder.build(
                        square=square_v,
                        square_validator=square_database.integrity_service.validator,
                    )
                    u_build_result = graph.vertices.integrity_service.builder.build(
                        square=square_u,
                        square_validator=square_database.integrity_service.validator,
                    )
                    graph.vertices.push(u_build_result.payload)
                    graph.vertices.push(v_build_result.payload)
                    
                    e = graph.edges.integrity_service.builder.build(
                        head=u_build_result.payload,
                        tail=v_build_result.payload,
                        coord_service=self.coord_service,
                    )
                    f = graph.edges.integrity_service.builder.build(
                        head=v_build_result.payload,
                        tail=u_build_result.payload,
                        coord_service=self.coord_service,
                    )
                    graph.edges.push(e)
                    graph.edges.push(f)
                    
                    u = graph.vertices.integrity_service.add_vertex(previous_square)
                    
                    e = graph.edges.integrity_service.add_edge(
                        source=u,
                        target=v,
                        weight=graph.edges.integrity_service
                    )
                    f = graph.edges.push(
                        graph.edges.integrity_service.builder.build(
                        
                        )
                    )
                    previous_point = point
                    current_coord = point
        
        @LoggingLevelRouter.monitor
        def _build_node_pair(
                self,
                head_square: Square,
                tail_square: Square,
                node_builder: NodeBuilder,
        ) -> BuildResult[Dict[str, Node]]:
            """
            Args:
                head_square: Square
                tail_square: Square
                node_builder: NodeBuilder
                
            Returns:
                BuildResult[Dict[str, Node]]
                
            Raises:
                BishopSpanServiceException
            """
            method = f"{self.__class__.__name__}._build_node_pair"
            
            head_build_result = node_builder.build(square=head_square)
            # Handle the case that, the head node is not built successfully.
            if head_build_result.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    BishopSpanServiceException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BishopSpanServiceException.MSG,
                        err_code=BishopSpanServiceException.ERR_CODE,
                        ex=head_build_result.exception
                    )
                )
            
            tail_build_result = node_builder.build(square=tail_square)
            # Handle the case that, the tail node is not built successfully.
            if tail_build_result.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    BishopSpanServiceException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BishopSpanServiceException.MSG,
                        err_code=BishopSpanServiceException.ERR_CODE,
                        ex=tail_build_result.exception
                    )
                )
            
            node_dict = {
                "head": head_build_result.payload,
                "tail": tail_build_result.payload
            }
            BuildResult.success(payload=node_dict)
        
        @LoggingLevelRouter.monitor
        def _build_edge_pair(
                self,
                head: Node,
                tail: Node,
                edge_builder: EdgeBuilder,
        ) -> BuildResult[Dict[str, Edge]]:
            """
            """
            method = f"{self.__class__.__name__}._build_edge_pair"
            
            forward_edge_result = edge_builder.build(head=head, tail=tail,)
            # Handle the case that, the e is not built successfully.
            if forward_edge_result.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    BishopSpanServiceException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BishopSpanServiceException.MSG,
                        err_code=BishopSpanServiceException.ERR_CODE,
                        ex=forward_edge_result.exception
                    )
                )
            
            reverse_edge_result = edge_builder.build(head=tail, tail=head)
            # Handle the case that, the tail node is not built successfully.
            if reverse_edge_result.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    BishopSpanServiceException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BishopSpanServiceException.MSG,
                        err_code=BishopSpanServiceException.ERR_CODE,
                        ex=reverse_edge_result.exception
                    )
                )
            node_dict = {
                "forward": forward_edge_result.payload,
                "reverse": reverse_edge_result.payload
            }
            BuildResult.success(payload=node_dict)
                    
                    
                    
                    
            
