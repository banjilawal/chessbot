# src/logic/span/service/operation/node/exception.py

"""
Module: logic.span.service.operation.node.operation
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from logic.graph import Graph
from logic.span import (
    PairInsertionException, NodeStackServiceProductionException, SquareGraphHandlerException,
    SquareRay, SquareSpan
)
from logic.square import Square, SquareService, SquareStackService
from logic.node import Node, NodeService,
from logic.span.service.handler import PairBuildException
from logic.system import BuildResult, InsertionResult, LoggingLevelRouter







class NodeTreeProducer:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def produce(
            cls,
            square_span: SquareSpan,
            node_service: NodeService = NodeService(),
    ) -> BuildResult[NodeTree]:
        """
        Action:
            Build a dictionary of adjacent nodes from a square hashtable., from a square hashtable.
            
        Args:
            square_span: SquareSpan
            node_service: NodeService
            
        Returns:
            BuildResult[SquareStackService]
            
        Raises:
            PairBuildException
        """
        method = f"{cls.__class__.__name__}.build_node_stack_service"
        
        # --- If the span contains any child spans, put them in a ray, then append to the parent, rays. ---#
        if square_span.has_sub_spans:
            square_span.rays.append(
                SquareRay(
                    origin=square_span.origin,
                    members=square_span.sub_span_roots
                )
            )
            # Clear the roots so they don't get added again.
            square_span.sub_span_roots.clear()
            
        # --- build the tree's root node. ---#
        root_node_build_result = node_service.build.execute(square=square_span.origin)
        # Handle the case that, the root_node is not built successfully.
        if root_node_build_result.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                SquareGraphHandlerException(
                    cls_mthd=method,
                    cls_name=cls.__class__.__name__,
                    msg=SquareGraphHandlerException.MSG,
                    err_code=SquareGraphHandlerException.ERR_CODE,
                    ex=PairBuildException(
                        mthd=method,
                        op=PairBuildException.OP,
                        msg=PairBuildException.MSG,
                        err_code=PairBuildException.ERR_CODE,
                        ex=root_node_build_result.exception
                    )
                )
            )
        return cls._production_helper(
            square_span=square_span,
            node_service=node_service,
            tree_origin=root_node_build_result.payload
        )

    
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
            tree_origin: Node
            square_span: SquareSpan
            node_service: NodeService
        Returns:
            BuildResult[NodeTree]
        Raises:
            NodeStackServiceProductionException
        """
        method = f"{cls.__class__.__name__}._production_helper"
        
        # --- Create the return target. ---#
        node_tree = NodeTree(root=tree_origin, branches=[])
        
        for ray in square_span.rays:
            pair_list_build_result = cls._produce_pair_list(
                square_ray=ray,
                origin_node=tree_origin,
                node_service=node_service,
            )
            # Handle the case that the node_link_pair is not built.
            if pair_list_build_result.is_failure:
                # Return the exception chain on failure.
                BuildResult.failure(
                    NodeStackServiceProductionException(
                        mthd=method,
                        op=NodeStackServiceProductionException.OP,
                        msg=NodeStackServiceProductionException.MSG,
                        err_code=NodeStackServiceProductionException.ERR_CODE,
                        rslt_type=NodeStackServiceProductionException.RSLT_TYPE,
                        ex=pair_list_build_result.exception,
                    )
                )
            node_tree.branches.append(pair_list_build_result.payload)
        return BuildResult.success(node_tree)


    

        # node_link_pair: Dict[str, Node] = {
        #     "head": head,
        #     "tail": node_build_result.payload,
        # }
        # --- Send the success result to the caller. ---#
        # return BuildResult.success(pair)
        
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
        method = f"{cls.__class__.__name__}.add_pair_to_graph"
        
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
                        ex=PairInsertionException(
                            mthd=method,
                            op=PairInsertionException.OP,
                            msg=PairInsertionException.MSG,
                            err_code=PairInsertionException.ERR_CODE,
                            rslt_type=PairInsertionException.RSLT_TYPE,
                            ex=push_result.exception
                        )
                    )
                )
        return InsertionResult.success()
    
        