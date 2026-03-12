# src/logic/span/service/handler/node/handler.py

"""
Module: logic.span.service.handler.node.handler
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

from logic.graph import Graph
from logic.span import (
    NodePairInsertionException, NodeStackServiceProductionException, SquareGraphHandlerException,
    SquareRay, SquareSpan
)
from logic.square import Square, SquareService, SquareStackService
from logic.node import Node, NodeBuilder, NodeService, NodeStackService
from logic.span.service.handler import NodePairBuildException
from logic.system import BuildResult, InsertionResult, LoggingLevelRouter

@dataclass
class NodePair:
    head: Node
    tail: Node

@dataclass    
class NodePairList:
    items: List[NodePair]

@dataclass    
class NodeTree:
    root: Node
    branches: List[NodePairList]

class NodeTreeProducer:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def produce(
            cls,
            square_span: SquareSpan,
            node_service: NodeService = NodeService(),
    ) -> BuildResult[NodeStackService]:
        """
        Action:
            Build a dictionary of adjacent nodes from a square hashtable., from a square hashtable.
            
        Args:
            square_span: SquareSpan
            node_service: NodeService
            
        Returns:
            BuildResult[SquareStackService]
            
        Raises:
            NodePairBuildException
        """
        method = f"{cls.__class__.__name__}.build_node_stack_service"
        
        
        
        
        
        node_dict: Dict[str, Node] = {}
        for key in square_dict:
            build_result = node_builder.build(square=square_dict[key])
            # Handle the case that, the node is not built
            if build_result.is_failure:
                # Return the exception chain on failure.
                return BuildResult.failure(
                    SquareGraphHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=SquareGraphHandlerException.MSG,
                        err_code=SquareGraphHandlerException.ERR_CODE,
                        ex=NodePairBuildException(
                            mthd=method,
                            op=NodePairBuildException.OP,
                            msg=NodePairBuildException.MSG,
                            err_code=NodePairBuildException.ERR_CODE,
                            ex=build_result.exception
                        )
                    )
                )
            node_dict[key] = build_result.payload
        return BuildResult.success(node_dict)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _production_helper(
            cls,
            origin_node: Node,
            square_span: SquareSpan,
            node_service: NodeService,
    ) -> BuildResult[NodeTree]:
        """
        Args:
            origin_node: Node
            square_span: SquareSpan
            node_service: NodeService
            
        Returns:
            BuildResult[NodeTree]
            
        Raises:
            NodeStackServiceProductionException
        """
        method = f"{cls.__class__.__name__}._production_helper"
        
        node_tree = NodeTree(root=origin_node, branches=[])
        
        inner_ray = cls._inner_ring_ray(square_span=square_span)
        if len(inner_ray.members) > 0:
            square_span.rays.append(inner_ray)
            
        for ray in square_span.rays:
            node_pair_list_build_result = cls._produce_node_ray(
                square_ray=ray,
                origin_node=origin_node,
                node_service=node_service,
            )
            # Handle the case that the node_link_pair is not built.
            if node_pair_list_build_result.is_failure:
                # Return the exception chain on failure.
                BuildResult.failure(
                    NodeStackServiceProductionException(
                        mthd=method,
                        op=NodeStackServiceProductionException.OP,
                        msg=NodeStackServiceProductionException.MSG,
                        err_code=NodeStackServiceProductionException.ERR_CODE,
                        rslt_type=NodeStackServiceProductionException.RSLT_TYPE,
                        ex=node_pair_list_build_result.exception,
                    )
                )
            node_tree.branches.append(node_pair_list_build_result.payload)
        return BuildResult.success(node_tree)
            
    @classmethod
    @LoggingLevelRouter.monitor
    def _inner_ring_ray(cls, square_span: SquareSpan,) -> SquareRay:
        """
        If any ray's origin differs from the span's origin, put it in an
        inner_ring_ray.
        
        Args:
            square_span: SquareSpan
        
        Returns:
            SquareRay
            
        Raises:
            None
        """
        method = f"{cls.__class__.__name__}._inner_ray"
        
        inner_ring_ray = SquareRay(origin=square_span.origin, members=[])
        for ray in square_span.rays:
            if ray.origin != square_span.origin:
                inner_ring_ray.members.append(ray.origin)
        return inner_ring_ray

    @classmethod
    @LoggingLevelRouter.monitor
    def _produce_node_ray(
            cls,
            origin_node: Node,
            square_ray: SquareRay,
            node_service: NodeService,
    ) -> BuildResult[NodePairList]:
        """
        Args:
            origin_node: Node
            square_ray: SquareRay
        
        Returns:
            BuildResult[List[Dict[str, Node]]]
        
        Raises:
            NodeStackServiceProductionException
        """
        method = f"{cls.__class__.__name__}._produce_node_ray"
        
        node_pair_list: NodePairList = NodePairList()
        for member in square_ray.members:
            node_link_build_result = cls._build_node_pair(
                square=member,
                origin_node=origin_node,
                node_service=node_service,
            )
            # Handle the case that the node_link_pair is not built.
            if node_link_build_result.is_failure:
                # Return the exception chain on failure.
                BuildResult.failure(
                    NodeStackServiceProductionException(
                        mthd=method,
                        op=NodeStackServiceProductionException.OP,
                        msg=NodeStackServiceProductionException.MSG,
                        err_code=NodeStackServiceProductionException.ERR_CODE,
                        rslt_type=NodeStackServiceProductionException.RSLT_TYPE,
                        ex=node_link_build_result.exception,
                    )
                )
                # Add the new node_pairing to the list.
                node_pair_list.items.append(node_link_build_result.payload)
                # Update the origin node.
                origin_node = node_link_build_result.payload.tail
            
        # --- Send the success result to the caller. ---#
        return BuildResult.success(node_pair_list)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_node_pair(
            cls,
            head: Node,
            square: Square,
            node_service: NodeService,
    ) -> BuildResult[NodePair]:
        """
        Build a node from adjacen

        Args:
            head: Node
            square: Square
            node_service: NodeService

        Returns:
            BuildResult[Dict[str, Node]]

        Raises:
            SquareNotFoundException
            NodeStackServiceProductionException
        """
        method = f"{cls.__class__.__name__}.square_from_coord"
        
        node_build_result = node_service.builder.build(square=square,)
        # Handle the case that the node is not built.
        if node_build_result.is_failure:
            # Return the exception chain on failure.
            BuildResult.failure(
                NodeStackServiceProductionException(
                    mthd=method,
                    op=NodeStackServiceProductionException.OP,
                    msg=NodeStackServiceProductionException.MSG,
                    err_code=NodeStackServiceProductionException.ERR_CODE,
                    rslt_type=NodeStackServiceProductionException.RSLT_TYPE,
                    ex=node_build_result.exception,
                )
            )
        # --- Create the Dictionary of the head and tail node. ---#
        node_pair = NodePair(head=head, tail=node_build_result.payload)
        # node_link_pair: Dict[str, Node] = {
        #     "head": head,
        #     "tail": node_build_result.payload,
        # }
        # --- Send the success result to the caller. ---#
        return BuildResult.success(node_pair)
        
        # Handle the case that, a square is not found.
        if search_result.is_empty:
            # Return the exception chain on failure.
            SearchResult.failure(
                NodeStackServiceProductionException(
                    mthd=method,
                    op=NodeStackServiceProductionException.OP,
                    msg=NodeStackServiceProductionException.MSG,
                    err_code=NodeStackServiceProductionException.ERR_CODE,
                    rslt_type=NodeStackServiceProductionException.RSLT_TYPE,
                    ex=SquareNotFoundException(
                        var="coord",
                        val=f"{coord}",
                        msg=NodeStackServiceProductionException.MSG,
                        err_code=NodeStackServiceProductionException.ERR_CODE,
                    ),
                )
            )
        # --- Return the search success result. ---#
        return search_result
    
    @classmethod
    @LoggingLevelRouter.monitor
    def insert_adjacent_nodes(
            cls,
            graph: Graph,
            node_dict:  Dict[str, Node],
    ) -> InsertionResult:
        """
        Args:
            graph: Graph
            node_dict: Dict[str, Node]
        """
        method = f"{cls.__class__.__name__}.add_node_pair_to_graph"
        
        for key in node_dict:
            push_result = graph.vertices.push(item=node_dict[key])
            # Handle the case that the node is not in the graph.
            if push_result.is_failure:
                # Return the exception chain on failure.
                return InsertionResult.failure(
                    SquareGraphHandlerException(
                        cls_mthd=method,
                        cls_name=cls.__class__.__name__,
                        msg=SquareGraphHandlerException.MSG,
                        err_code=SquareGraphHandlerException.ERR_CODE,
                        ex=NodePairInsertionException(
                            mthd=method,
                            op=NodePairInsertionException.OP,
                            msg=NodePairInsertionException.MSG,
                            err_code=NodePairInsertionException.ERR_CODE,
                            rslt_type=NodePairInsertionException.RSLT_TYPE,
                            ex=push_result.exception
                        )
                    )
                )
        return InsertionResult.success()
    
        