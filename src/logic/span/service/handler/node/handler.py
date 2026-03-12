# src/logic/span/service/handler/node/handler.py

"""
Module: logic.span.service.handler.node.handler
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict

from logic.graph import Graph
from logic.span import NodePairInsertionException, SquareGraphHandlerException
from logic.square import Square
from logic.node import Node, NodeBuilder
from logic.span.service.handler import NodePairBuildException
from logic.system import BuildResult, InsertionResult, LoggingLevelRouter

class SquareGraphHandler:
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_adjacent_nodes(
            cls,
            square_dict: Dict[str, Square],
            node_builder: NodeBuilder = NodeBuilder(),
    ) -> BuildResult[Dict[str, Node]]:
        """
        Action:
            Build a dictionary of adjacent nodes from a square hashtable., from a square hashtable.
            
        Args:
            node_builder: NodeBuilder
            square_dict: Dict[str, Square]
            
        Returns:
            BuildResult[Dict[str, Node]]
            
        Raises:
            NodePairBuildException
        """
        method = f"{cls.__class__.__name__}.build"
        
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
    
        