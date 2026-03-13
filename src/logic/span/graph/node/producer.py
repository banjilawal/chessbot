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
    """
    NodePairList's physical structure can be either
    a list or tree.
    """
    items: List[NodePair]

@dataclass    
class NodeTree:
    """
    The tree might have one root or subtrees.
    """
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
            tree_origin: Node,
            square_span: SquareSpan,
            node_service: NodeService,
    ) -> BuildResult[NodeTree]:
        """
        Action:
            1.  If there are sub-spans create an innermost span of their roots which is appended
        Args:
            span_origin_node: Node
            square_span: SquareSpan
            node_service: NodeService
        Returns:
            BuildResult[NodeTree]
        Raises:
            NodeStackServiceProductionException
        """
        method = f"{cls.__class__.__name__}._production_helper"
        
        # --- If the span contains any child spans, put them in a ray, then append to the parent, rays. ---#
        sub_span_roots= cls._get_sub_span_roots(square_span=square_span)
        if not sub_span_roots.is_empty:
            square_span.rays.append(sub_span_roots)
            
        node_tree = NodeTree(root=tree_origin, branches=[])
        for ray in square_span.rays:
            node_pair_list_build_result = cls._produce_node_ray(
                square_ray=ray,
                origin_node=tree_origin,
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
    def _get_sub_span_roots(cls, square_span: SquareSpan,) -> SquareRay:
        """
        Action:
            1.  Go through the rays looking for any ray.origin != span.origin
                which indicates there's a child span.
            2.  If there is a child span put its root into child_span_roots
                which, is the span's innermost ray.
            3.  Return the ray of child_span_roots to the caller.
            
        Args:
            square_span: SquareSpan
            
        Returns:
            SquareRay
            
        Raises:
            None
        """
        method = f"{cls.__class__.__name__}._get_sub_span_roots"
        
        # --- Create the return target. ---#
        sub_span_roots_ray = SquareRay(origin=square_span.origin, members=[])
        
        # Iterate through the rays looking for child_span roots.
        for ray in square_span.rays:
            if ray.origin != square_span.origin:
                sub_span_roots_ray.members.append(ray.origin)
        # --- Return the innermost ray containing, the child-span roots. ---#
        return sub_span_roots_ray

    @classmethod
    @LoggingLevelRouter.monitor
    def _produce_node_pair_list(
            cls,
            origin_node: Node,
            square_ray: SquareRay,
            node_service: NodeService,
    ) -> BuildResult[NodePairList]:
        """
        Action:
            1.  Send an exception chain if, either
                    *   origin_node.square != square_ray.origin
                    *   a node_pair build fails.
            2.  Otherwise, start the cursor at the origin_node then, iterate through
                the ray's members.
            3.  On each iteration
                    *   Build a node pair.
                    *   Append to the node_pair_list.
                    *   Advance the cursor.
            4.  Return the success result.
            
        Args:
            origin_node: Node
            square_ray: SquareRay
            node_service: NodeService
            
        Returns:
            BuildResult[NodePairList]
            
        Raises:
            NodeStackServiceProductionException
        """
        method = f"{cls.__class__.__name__}._produce_node_pair_list"
        
        # --- Create the cursor and return target. ---#
        cursor = origin_node
        node_pair_list: NodePairList = NodePairList()

        # --- Do the node_pair building work on each ray member. ---#
        for member in square_ray.members:
            production_result = cls._produce_node_pair(
                head=cursor,
                tail_square=member,
                node_service=node_service,
            )
            # Handle the case that, there is no work product.
            if production_result.is_failure:
                # Return the exception chain on failure.
                BuildResult.failure(
                    NodeStackServiceProductionException(
                        mthd=method,
                        op=NodeStackServiceProductionException.OP,
                        msg=NodeStackServiceProductionException.MSG,
                        err_code=NodeStackServiceProductionException.ERR_CODE,
                        rslt_type=NodeStackServiceProductionException.RSLT_TYPE,
                        ex=production_result.exception,
                    )
                )
                # --- Add the pair to the list, then advance the cursor. ---#.
                node_pair_list.items.append(production_result.payload)
                cursor = production_result.payload.tail
            
        # --- Send the completed list of node_pairs ---#
        return BuildResult.success(node_pair_list)
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _produce_node_pair(
            cls,
            head: Node,
            tail_square: Square,
            node_service: NodeService,
    ) -> BuildResult[NodePair]:
        """
        Action:
            1.  If building a node from the tail_square fails send an exception chain in
                the BuildResult.
            2.  If the build was successful
                    *   Build a node_pair with the head and its new tail.
                    *   Return the work product.
        Args:
            head: Node
            tail_square: Square
            node_service: NodeService
            
        Returns:
            BuildResult[NodePair]
            
        Raises:
            SquareNotFoundException
            NodeStackServiceProductionException
        """
        method = f"{cls.__class__.__name__}._produce_node_pain"
        
        # --- Attempt building the tail node. ---#
        tail_node_build_result = node_service.builder.build(square=tail_square,)
        
        # Handle the case that, there is no work product.
        if tail_node_build_result.is_failure:
            # Return the exception chain on failure.
            BuildResult.failure(
                NodeStackServiceProductionException(
                    mthd=method,
                    op=NodeStackServiceProductionException.OP,
                    msg=NodeStackServiceProductionException.MSG,
                    err_code=NodeStackServiceProductionException.ERR_CODE,
                    rslt_type=NodeStackServiceProductionException.RSLT_TYPE,
                    ex=tail_node_build_result.exception,
                )
            )
        
        # --- Send the work product. ---#
        BuildResult.success(NodePair(head=head, tail=tail_node_build_result.payload))
        # node_link_pair: Dict[str, Node] = {
        #     "head": head,
        #     "tail": node_build_result.payload,
        # }
        # --- Send the success result to the caller. ---#
        # return BuildResult.success(node_pair)
        
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
    
        